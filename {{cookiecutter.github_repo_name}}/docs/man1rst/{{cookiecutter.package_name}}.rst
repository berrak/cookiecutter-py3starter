

SYNOPSIS
--------

.. code::

    {{ cookiecutter.package_name }} [options]

    {{ cookiecutter.package_name }} --help


DESCRIPTION
-----------

.. include:: ../longdescription.rst

Update this text in the 'docs/longdescription.rst' dokument and re-run *make man* and *make html*.

OPTIONS
-------

To see all options available in your installation, run::

    {{ cookiecutter.package_name }} --help

All options available as of {{ cookiecutter.package_name }} v\ |release|::

    -V, --version         show {{ cookiecutter.package_name }} version number and exit
    -h, --help            show this help message and exit
    

EXAMPLES
--------

Show usage::

    {{cookiecutter.package_name}} --help

Show program version::

    {{cookiecutter.package_name}} --version


SEE ALSO
--------

{{ cookiecutter.project_name }} Homepage: {{ cookiecutter.website }}

{{ cookiecutter.package_name }} documentation: https://{{ cookiecutter.github_repo_name }}.readthedocs.io


BUGS
----

Please report all bugs to https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/issues/
