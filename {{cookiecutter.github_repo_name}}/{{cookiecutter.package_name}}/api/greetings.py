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
{{ cookiecutter.package_name }}.api.greetings
----------------------------------------------

Various functions and classes that defines the library API.

"""


class Greetings(object):

    def __init__(self, msg="Hello world!"):
        self.msg = msg

    def __str__(self):
        return self.msg


def howdy_greeting():
        return "Howdy cowboy!"
