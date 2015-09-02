from os.path import dirname
from os.path import join
from setuptools import setup


def read(*path):
    with open(
            join(dirname(__file__), *path),
            encoding="utf8"
    ) as fp:
        return fp.read()


setup(
    name="fileflood-ignore",
    version='0.0.1',
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
