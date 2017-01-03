#
# Copyright {{ cookiecutter.author_name }}, {{ cookiecutter.initial_year_to_release }}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
utils.environment
-----------------

Utility functions for executing environment

"""

import subprocess
import sys

from {{ cookiecutter.package_name }} import __version__


def shell_python():
    """
    Deduce the default python 3 version with a shell call to the interpreter.
    """
    shellpython_version = subprocess.check_output(["python3", "-V", "/dev/null"])
    return str(shellpython_version, 'utf-8')


def {{ cookiecutter.package_name }}_version():
    """
    Canonical version of {{ cookiecutter.package_name }}
    """
    return __version__


def python_version(level='patch'):
    """
    Default version 'M.m.p' of running Python interpreter
    """
    width_dict = {'major': 1, 'minor': 3, 'patch': 5}
    return sys.version[:width_dict[level]]
