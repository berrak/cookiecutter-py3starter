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
{{ cookiecutter.project_name }} setup.

"""
import re
import codecs
import os

from setuptools import setup


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    # https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    """
    Build a path from *file_paths* and search for a ``__version__``
    string inside.
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open('docs/shortdescription.rst') as description_file:
    SHORT_DESCRIPTION = description_file.read().replace('.. :shortdescription:', '')

with open('docs/longdescription.rst') as long_description_file:
    LONG_DESCRIPTION = long_description_file.read().replace('.. :longdescription:', '')

# The full canonical version information, including alpha/beta/rc/git tags.
FULL_VERSION = find_version('{{ cookiecutter.package_name }}/__init__.py')
# Short X.Y version.
MAJOR_MINOR_VERSION = FULL_VERSION.rsplit(u".", 1)[0]

# TODO: put package requirements here
INSTALL_REQUIRES = ['cookiecutter']

TESTS_REQUIRE = ['green>=2.5', 'coverage>=4.2', 'flake8>=3.0', 'check-manifest>=0.31']

setup(
    name='{{ cookiecutter.package_name }}',
    packages=[
        '{{ cookiecutter.package_name }}',
    ],
    package_dir={'{{ cookiecutter.package_name }}': '{{ cookiecutter.package_name }}'},
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.__main__:main',
        ]
    },
    version=FULL_VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='{{ cookiecutter.website }}',
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    license='Apache License, Version 2.0',
    zip_safe=False,
    python_requires='>3.0,!=3.1.*,!=3.2.*,!=3.3.*',
    keywords=('{{ cookiecutter.package_name }}, Python, project template, package, packaging'),
    tests_require=TESTS_REQUIRE
)
