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

import unittest

from {{ cookiecutter.package_name }}.main import Greetings
from {{ cookiecutter.package_name }}.main import howdy_greeting


class TestMain(unittest.TestCase):
    """
    Test main's library classes and functions.

    """

    def test_main_greetings(self):
        msg = str(Greetings())
        self.assertEqual(msg, "Hello world!")

    def test_main_greetings_again(self):
        msg = str(Greetings("Hello again!"))
        self.assertEqual(msg, "Hello again!")

    def test_main_howdy(self):
        self.assertEqual(howdy_greeting(), "Howdy cowboy!")
