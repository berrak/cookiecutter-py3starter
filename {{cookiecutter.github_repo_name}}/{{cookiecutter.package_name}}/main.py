#!/usr/bin/env python3
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
{{ cookiecutter.package_name }}.main
------------------------------------

CLI can import `{{ cookiecutter.package_name }}` to access
various functions and classes that defines the library API.

The code in this module is also a good example of how to use
{{ cookiecutter.package_name }} as a library rather than a script.
"""


class Greetings(object):

    def __init__(self, msg="Hello world!"):
        self.msg = msg

    def __str__(self):
        return self.msg


def howdy_greeting():
        return "Howdy cowboy!"
