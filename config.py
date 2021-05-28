import configparser
from configparser import NoOptionError, NoSectionError

def import_conf(section, name):
    conf = configparser.ConfigParser()
    conf.read("settings.ini")
    
    try:
        out = conf.get(section, name)
        return out
    except (NoSectionError, NoOptionError):
        out = None
        return out 