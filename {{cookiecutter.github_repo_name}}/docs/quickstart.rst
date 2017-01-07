Quickstart
==========


Use {{ cookiecutter.package_name }} on the command line:

::

    $ {{ cookiecutter.package_name }}
    Hello world!

Show help:

::

    $ {{ cookiecutter.package_name }} --help
    usage: {{ cookiecutter.package_name }} [-h] [-V] [-c, --cowboy]
    
    optional arguments:
        -h, --help     show this help message and exit
        -V,            show the version and exit
        -c, --cowboy   cowboy greeting


Use {{ cookiecutter.package_name }} as a library:

::

    $ python3
    >>> from {{ cookiecutter.package_name }}.api.greetings import Greetings
    >>> print(Greetings())
    Hello world!
