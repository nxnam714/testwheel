import logging
import setuptools.command.egg_info as egg_info
from setuptools import setup, find_packages, find_namespace_packages
from distutils import log
import setuptools



logging.basicConfig(
    format='%(module)-15s %(lineno)-8s %(message)s',
    style="%",
    level=logging.DEBUG
)

setattr(setuptools, "logging", logging)
logger = logging.getLogger(__name__)
log.info = logger.info

public = False
if public:
    o_manifest_maker = egg_info.manifest_maker

    class manifest_maker(o_manifest_maker):
        template = "MANIFEST.pub"

    egg_info.manifest_maker = manifest_maker
    exclude = ("*.internal", "*.internal.*")
else:
    exclude = ()

packages = find_namespace_packages(
    where=".",
    include=("testWheel", "testWheel.*", ),
    exclude=exclude,
)
print(packages)
setup(
    name='testWheel',  # Name of your package
    version='1.0',     # Version number
    packages=packages,
    include_package_data=True,
)
