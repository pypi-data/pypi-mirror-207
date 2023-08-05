import os
import shutil
import sys


def pre_process_configs():
    if not 'CONFIG_LINKS' in os.environ:
        return
    if not 'CONFIG_DIR' in os.environ:
        print("Fatal: no CONFIG_DIR variable provided to process config links",flush=True)
        sys.exit(1)
    print("Parsing config links ...")
    config_dir=os.environ['CONFIG_DIR']
    config_map={link.split(":")[0]:link.split(":")[1] for link in os.environ['CONFIG_LINKS'].replace("CONFIG_DIR",config_dir).split(",")}
    print("Copying config files ...",flush=True)
    for copy_from,copy_to in config_map.items():
        dirname = os.path.dirname(copy_to)
        if not os.path.exists(dirname):
            print("Creating directory {}".format(dirname))
            os.makedirs(dirname)
        print("Copying file {} to {}".format(copy_from,copy_to),flush=True)
        shutil.copy(copy_from,copy_to)