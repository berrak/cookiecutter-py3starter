.. _`Installation`:

Installation
============


Do I need to install pip to install {{ cookiecutter.package_name }}?
------------------------------------------------------------------------

``pip`` is installed if you're using Python 3 >=3.4
binaries downloaded from `python.org <https://www.python.org>`_. 

Additionally, ``pip`` will already be installed if you're working with ``virtualenv``
or ``pyvenv``.


Using Linux Package Managers
----------------------------

``pip`` may also be installed by your Package Manager, test with:

::

    $ apt-cache policy python3-pip


Install {{ cookiecutter.package_name }}
------------------------------------------------------------------------

With pip:

::

    $ pip install {{ cookiecutter.package_name }}


Uninstalling {{ cookiecutter.package_name }}
-------------------------------------------------------------------------

Uninstall {{ cookiecutter.package_name }} like so:

::

    $ pip uninstall {{ cookiecutter.package_name }}


Python and OS Compatibility
----------------------------

{{ cookiecutter.package_name }} works with CPython versions 3.4.

Test of compatibility with additional Python versions will be added.
