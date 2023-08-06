from setuptools import setup
import os


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1]) + version_tuple[-1])
    return '.'.join(map(str, version_tuple))


init = os.path.join(
    os.path.dirname(__file__), '__init__.py'
)

version_line = list(
    filter(lambda l: l.startswith('VERSION'), open(init))
)[0]

PKG_VERSION = get_version(eval(version_line.split('=')[-1]))
setup(
    name="mathexternal",
    description="External functionality for int type",
    long_description="""MathExternal class add __len__ method for int base type""",
    version=PKG_VERSION
)