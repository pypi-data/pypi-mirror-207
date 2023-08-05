import re
from abc import abstractmethod
from utils.stringcalc import evaluate
from lxml import etree
import sys
import configparser
import json
import yaml

class XPathUpdater():
    @abstractmethod
    def update(self, config, xpath, format_mask, params):
        pass

class XMLUpdater(XPathUpdater):

    def update(self, config, xpath, format_mask, params):
        split = xpath.split("/")
        if split[-1].startswith("@"):
            node_xpath="/".join(split[0:-1])
            attr=split[-1][1:]
            node = config.xpath(node_xpath)[0]
            node.attrib[attr]=process_mask(format_mask,params)
        else:
            node=config.xpath(xpath)[0]
            node.text=process_mask(format_mask,params)


class DictUpdater(XPathUpdater):

    def lookup(self,split,node,parent,key):
        if not split:
            return parent,node,key
        name=split[0]
        in_brackets = re.search(r"\[(.+)\]", name)
        if not in_brackets:
            return self.lookup(split[1:],node[name],node,name)
        else:
            arg=in_brackets.group(1)
            if not arg.startswith("@"):
                print("Search of attributes only is supported for dict configs",flush=True)
                sys.exit(1)
            attr=arg[1:].split("=")[0]
            look=arg[1:].split("=")[1].strip("'")
            next_node=None
            if isinstance(node,list):
                for child in node:
                    if child[attr]==look:
                        next_node=child
                        key=node.index(child)
                        break
                if not next_node:
                    return None,None,None
                return self.lookup(split[1:], next_node, node,key)
            else:
                for child in node.values():
                    if child[attr]==look:
                        next_node=child
                        break
                if not next_node:
                    return None,None,None
                return self.lookup(split[1:], next_node, node,look)



    def update(self, config, xpath, format_mask, params):
        split = xpath.strip("/").split("/")
        parent,node,key=self.lookup(split,config,None,None)
        if node:
            parent[key]= self.finalize_value(format_mask, params)

    def finalize_value(self, format_mask, params):
        return process_mask(format_mask, params)


class CPUpdater(DictUpdater):

    def finalize_value(self, format_mask, params):
        return str(process_mask(format_mask, params))


class Config():


    def __init__(self, updater, file, new_file, xpath_tasks, params) -> None:
        super().__init__()
        self.params = params
        self.xpath_tasks = xpath_tasks
        self.new_file = new_file
        self.file = file
        self.updater = updater

    @abstractmethod
    def parse(self):
        pass

    def process(self):
        self.config = self.parse()
        for task_name,task in self.xpath_tasks.items():
            self.updater.update(self.config,task['xpath'],task['format'],self.params)

        self.dump()

    @abstractmethod
    def dump(self):
        pass


class YAMLConfig(Config):

    def parse(self):
        return yaml.safe_load(open(self.file))

    def dump(self):
        yaml.safe_dump(self.config, open(self.new_file, 'w'), default_flow_style=False, encoding='utf-8', allow_unicode=True)

class JSONConfig(Config):

    def parse(self):
        return json.load(open(self.file))

    def dump(self):
        json.dump(self.config, open(self.new_file, 'w'), indent=2)

class XMLConfig(Config):

    def parse(self):
        return etree.parse(self.file)

    def dump(self):
        open(self.new_file,"w").write(etree.tostring(self.config, encoding="unicode", pretty_print=True))

class CPConfig(Config):

    def __init__(self, updater, file, new_file, xpath_tasks, params) -> None:
        super().__init__(updater, file, new_file, xpath_tasks, params)


    def parse(self):
        parser = configparser.ConfigParser()
        parser.optionxform = lambda option: option
        parser.read(self.file)
        return parser

    def dump(self):
        self.config.write(open(self.new_file,"w"))

def process_mask(var_mask,params):

    number= var_mask.startswith("#(") and var_mask.endswith(")")
    print("Var mask {}      params {}   number {}".format(var_mask,str(params),str(number)),flush=True)
    processed_mask=var_mask.format_map(params)
    #print("Processed_mask {} ".format(processed_mask),flush=True)
    processed_mask = try_calculate(processed_mask if not number else processed_mask[2:-1])
    #print("Calculated_mask {} ".format(processed_mask),flush=True)
    final_try=None
    try:
        final_try=evaluate(processed_mask)
    except Exception as error:
        pass
    #print("Final try {} not None {}".format(final_try,final_try is not None),flush=True) 
    result=processed_mask if final_try is None else float(evaluate(processed_mask)) if "." in processed_mask else int(evaluate(processed_mask))
    print("Final try {} result {}".format(final_try,result),flush=True)
    return result


def try_calculate(processed_mask):
    if "#(" in processed_mask:
        split=[m.start() for m in re.finditer('#\(',processed_mask)]
        out=[processed_mask[0:split[0]]]
        for k in range(len(split)):
            start=split[k]
            next=split[k+1] if k<len(split)-1 else len(processed_mask)
            stack=[start+1]
            for i in range(start+2,next):
                if processed_mask[i]=="(":
                    stack.append(i)
                elif processed_mask[i]==")":
                    stack.pop()
                    if not stack:
                        out.append(try_calculate(processed_mask[start+2:i]))
                        break
            if stack:
                raise ValueError("Calculation of the value of string {} is failed: part {} is incorrect".format(processed_mask,processed_mask[start:next]))
            out.append(processed_mask[i+1:next])
        return "".join(out)

    try:
        evaluate_result=evaluate(processed_mask)
        calc_result = evaluate_result if evaluate_result else processed_mask
        processed_mask = str(calc_result)
    except Exception as error:
        pass
    return processed_mask


def parse_configs(params, zc_conf):
    xmlUpdater=XMLUpdater()
    dictUpdater=DictUpdater()
    cpUpdater=CPUpdater()

    updaters={"yaml":dictUpdater,"json":dictUpdater,"xml":xmlUpdater,"cf":cpUpdater}
    configFactory={"yaml":YAMLConfig,"json":JSONConfig,"xml":XMLConfig,"cf":CPConfig}


    if not 'goals' in zc_conf:
        return
    goals= zc_conf['goals']
    configs_processed=[]
    for config, goal in goals.items():
        updater=updaters[goal['type']]
        config_processor=configFactory[goal['type']](updater, goal['input-config'], goal['output-config'], goal['xpath-tasks'], params)
        config_processor.process()
        configs_processed.append(goal['output-config'])
    return configs_processed


def main():
    params={"host": "new_host", "port": "new_port"}
    parse_configs(params, zc_conf)

if __name__ == '__main__':
    main()









