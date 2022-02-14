import os
import sys
import yaml


class SysConfig(object):

    DEBUG = True
    BUNDLE_ERRORS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    def __init__(self, settings):
        if not os.path.isfile(settings):
            sys.exit("can not find {}, exit...".format(settings))

        with open(settings, 'r') as handle:
            conf = yaml.load(handle, Loader=yaml.SafeLoader) or {}
            for k, v in conf.items():
                setattr(self, k, v)


def get_config():
    return SysConfig("doom/settings.yaml")
