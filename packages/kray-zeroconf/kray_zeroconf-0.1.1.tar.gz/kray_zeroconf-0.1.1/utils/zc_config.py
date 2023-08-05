import copy
import fnmatch
import sys

import yaml


def merge(destination, source):
    for key, value in source.items():
        if isinstance(value, dict):
            # get matching nodes or create one
            dest_match=fnmatch.filter(destination.keys(),key)
            if dest_match:
                for dest_key in dest_match:
                    merge(destination.get(dest_key),value)
            else:
                node = destination.setdefault(key, {})
                merge(node,value)
        elif isinstance(value,list) and key in destination:
            if isinstance(destination[key],list):
                destination[key].extend(value)
            else:
                print("Fatal: incompatible types of {} is source and {} in destination".format(value,destination[key]),flush=True)
                sys.exit(1)
        else:
            destination[key] = value

    return destination

def load_config(file):
    zc_conf = yaml.safe_load(file if file else open("zeroconf.yaml"))
    common_desc=zc_conf.get("common",{})
    services_desc = zc_conf.get("services", {})
    zc_conf['services']=services_desc
    host_desc= services_desc.get("host", {})
    services_desc['host']=host_desc
    for service, service_desc in services_desc.items():
        services_desc[service]=merge(copy.deepcopy(common_desc),service_desc)
    return zc_conf
