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
utils.test_environment
----------------------

Test functions for the executing environment

"""

import unittest

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.utils.environment import {{ cookiecutter.package_name }}_version
from {{ cookiecutter.package_name }}.utils.environment import python_version
from {{ cookiecutter.package_name }}.utils.environment import shell_python


class TestUtilsEnvironment(unittest.TestCase):
    """
    Test utils functions.
    - show released program version
    - show Python version

    """

    def test_program_version(self):
        self.assertEqual({{ cookiecutter.package_name }}_version(), __version__)

    def test_python_version(self):
        self.assertIn(python_version(), shell_python())

    def test_python_major_version(self):
        self.assertEqual(python_version('major'), '3')
