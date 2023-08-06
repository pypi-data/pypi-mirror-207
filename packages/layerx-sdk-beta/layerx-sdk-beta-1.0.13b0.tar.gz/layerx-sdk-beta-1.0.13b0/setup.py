import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.13b0'
DESCRIPTION = 'LayerX Python SDK'
LONG_DESCRIPTION = 'Python API Client to interact with LayerNext stack'

# Setting up
setup(
    name="layerx-sdk-beta",
    version=VERSION,
    author="LayerNext",
    author_email="<support@layernext.ai>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(
        include=['layerx', 'layerx.datalake', 'layerx.dataset', 'layerx.studio']),
    install_requires=['requests', 'uuid', 'python-dotenv'],
    keywords=['python', 'datalake', 'datasetsync', 'ai',
              'annotation', 'layerx', 'layernext', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
