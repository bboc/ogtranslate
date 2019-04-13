import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ogtranslate",
    version="0.01",
    packages=find_packages(exclude='tests'),
    install_requires=['polib'],
    author="Bernhard Bockelbrink",
    author_email="bernhard.bockelbrink@gmail.com",
    description="Translate text in OmniGraffle Documents.",
    long_description=read("README.md"),
    license="http://www.opensource.org/licenses/mit-license.php",
    keywords="omnigraffle translation gettext i18n command",
    url="https://github.com/bboc/ogtranslatet",
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Operating System :: MacOS :: MacOS X',
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities"
    ],
    entry_points={
        'console_scripts': [
            'ogtrans = omnigraffle_translate.translate:main',
        ],
    },
    test_suite='tests',
    zip_safe=True,
)
