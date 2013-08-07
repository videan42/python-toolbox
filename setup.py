#!/usr/bin/env python

import os
import sys
from distutils.core import setup

THISDIR = os.path.dirname(os.path.abspath(__file__))
if THISDIR not in sys.path:
    sys.path.insert(0, THISDIR)

from darkstarlabs import toolbox

setup(
    name='DarkstarToolbox',
    version=toolbox.__version__,
    description=toolbox.__doc__,
    author=toolbox.__author__,
    author_email=toolbox.__email__,
    url=toolbox.__url__,
    packages=['darkstarlabs.toolbox'],
)
