# encoding: utf-8
from zest.releaser import pypi


def datacheck(data):
    config = pypi.PypiConfig()
    marker = config.development_marker()
    version = data['version']
    tag_already_exists = data['tag_already_exists']
    if tag_already_exists:
        raise RuntimeError("This tag already exists: %s" % version)
    if marker in version:
        raise RuntimeError("Invalid Version. This version contains the development marker: %s" % version)
