Quickstart
==========

First, :doc:`Install {{ cookiecutter.package_name }} <installing>`.

Use {{ cookiecutter.package_name }} on the command line:

::

    $ {{ cookiecutter.package_name }}
    Hello world!
    Howdy cowboy!

Show help:

::

    $ {{ cookiecutter.package_name }} --help
    usage: {{ cookiecutter.package_name }} [-h] [-V]
    
    optional arguments:
      -h, --help     show this help message and exit
      -V, --version  show the version and exit


Use {{ cookiecutter.package_name }} as a library:

::

    $ python3
    >>> from {{ cookiecutter.package_name }}.main import Greetings
    >>> print(Greetings())
    Hello world!
