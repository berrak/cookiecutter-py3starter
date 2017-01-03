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
{{ cookiecutter.package_name }}.cli
-----------------------------------

Entry for the `{{ cookiecutter.package_name }}` CLI.

"""

import os
import sys
import argparse

from {{ cookiecutter.package_name }}.utils.environment import {{ cookiecutter.package_name }}_version
from {{ cookiecutter.package_name }}.utils.environment import python_version

from {{ cookiecutter.package_name }}.main import Greetings
from {{ cookiecutter.package_name }}.main import howdy_greeting


def pgm_location():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(argv=sys.argv):

    parser = argparse.ArgumentParser()
    parser.add_argument("-V", "--version", help="show the version and exit", action="store_true")

    arg = parser.parse_args()

    # Never executes when used with option -h/--help
    if arg.version:
        message = '{{ cookiecutter.package_name }} v{} from {} (Python {})'
        print(message.format({{ cookiecutter.package_name }}_version(), pgm_location(), python_version()))
        sys.exit(0)

    # Process other arguments

    # CLI call's from {{ cookiecutter.package_name }} library API
    greetings = Greetings()
    print(greetings)
    print(howdy_greeting())

    return 0


if __name__ == '__main__':
    sys.exit(main(0))
