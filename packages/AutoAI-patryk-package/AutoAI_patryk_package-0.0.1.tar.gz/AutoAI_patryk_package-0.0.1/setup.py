from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Auto_AI_patryk'
LONG_DESCRIPTION = 'Package contain helping functions for creating ML models'

setup(
    name="AutoAI_patryk_package",
    version=VERSION,
    author="patryk",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'machine_learning', 'auto'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
