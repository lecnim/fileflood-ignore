from os.path import dirname
from os.path import join
import re
from setuptools import setup


def read(*path):
    with open(
            join(dirname(__file__), *path),
            encoding="utf8"
    ) as fp:
        return fp.read()


def find_version(*path):
    version_file = read(*path)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="fileflood-ignore",
    version=find_version('fileflood_ignore.py'),
    license="MIT",

    description="A Fileflood plugin used to ignore files that match a pattern.",
    long_description=read("README.rst") + '\n\n' + read("CHANGES.rst"),

    author="Kasper Minciel",
    author_email="kasper.minciel@gmail.com",

    url="https://github.com/lecnim/fileflood-ignore",

    py_modules=['fileflood_ignore'],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',

    classifiers=[
        "Environment :: Plugins"
    ],
    install_requires=["fileflood"]
)
