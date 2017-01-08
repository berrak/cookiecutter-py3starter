=======================
cookiecutter-py3starter
=======================

A Cookiecutter_ template for your next Python 3 project.

This is a Python 3 only, documentation ready with a developers Makefile.
With *cookiecutter-py3starter* you will be up with your next project in no time.

The emphasis for this template is *not* to support all python versions,
all platforms or use continous integration but rather to start small and grow.

*Notes*:
Inspiration and credits to Ionel Cristian Maries package *cookiecutter-pylibrary* and
naturally to the development leads, core committers and all contributors to *Cookiecutter*.

Developed on Debian 8.6 (Jessie).

Features
--------

This template includes.

* Supports modern Python 3.4+.
* A major part of the documentation with Sphinx_ done, hook it up with ReadTheDocs_.
* Run common development tasks with included *Makefile*.
* Run unittest classes and methods with Green_.
* Code skeleton includes 7 unittests to get started.
* Starting point for a CLI application or a library.
* Get started with coverage_.
* Ensure code follow best practices with *flake8* (lint) and manifest checks.
* Includes configured *bumpversion* to simplify version updates in the release process.
* Create HTML and system man pages with configured Sphinx_.
* Licensed under the Apache License.

.. contents:: Table of Contents


Project layout
--------------

The final project layout with defaults (package name = ``alfabeta``)::

    .
    ├── alfabeta
    │   ├── cli.py
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── test
    │   │   ├── __init__.py
    │   │   └── test_cli.py
    │   └── utils
    │       ├── environment.py
    │       ├── __init__.py
    │       └── test
    │           ├── __init__.py
    │           └── test_environment.py
    ├── AUTHORS.rst
    ├── CHANGELOG.rst
    ├── docs
    │   ├── changelog.rst
    │   ├── conf.py
    │   ├── development.rst
    │   ├── index.rst
    │   ├── installing.rst
    │   ├── longdescription.rst
    │   ├── Makefile
    │   ├── man1rst
    │   │   ├── alfabeta.rst
    │   │   └── index.rst
    │   ├── quickstart.rst
    │   ├── README.rst
    │   ├── requirements.txt
    │   ├── shortdescription.rst
    │   └── user_guide.rst
    ├── LICENSE
    ├── Makefile
    ├── MANIFEST.in
    ├── README.rst
    ├── requirements.txt
    ├── run_alfabeta.py
    ├── setup.cfg
    └── setup.py


Installation
------------

Install cookiecutter like documented at Cookiecutter_ or simply::

    [sudo] pip install --upgrade cookiecutter
    cookiecutter -V

You will need Git version control system, install it with::

    sudo apt-get install git

It's wise to isolate the Python development in a virtual environment::
   
    mkdir ~/py3project1
    cd py3project1
    pyvenv PY3VS
    source PY3VS/bin/activate
    (PY3VS) 

For more information, see *venv* in virtual-environment_ or::

    man pyvenv

Put an alias in your ~/.bashrc file like so::

    alias v+='source ~/py3project1/PY3VS/bin/activate'

then to activate just type v+ at the command line.


Usage and options
-----------------

The latter command will clone the cookiecutter from GitHub to ~/.cookiecutters
The resulting project is output to your current directory. Generate it with::

    (PY3VS) cd py3project1
    (PY3VS) cookiecutter gh:berrak/cookiecutter-py3starter

You will be asked for these fields:


.. list-table::
    :header-rows: 1

    * - Template variable
      - Default
      - Description

    * - ``author_name``
      - .. code::

            "Clark Kent"
      - Main author of this library or application.

    * - ``author_email``
      - .. code::

            "clark.kent@example.com"
      - Contact email of the author.

    * - ``github_username``
      - .. code::

            "clarkk"
      - GitHub user name of this project (used for GitHub link).

    * - ``project_name``
      - .. code::

            "Alfabeta Py3 Project"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``short_description``
      - .. code::

            "<project_name>"
      - One line description of the project. Text is saved in the
        generated docs-folder's shortdescription.rst.

    * - ``long_description``
      - .. code::

            "Now when we have an awesome project template generator,
             use it! All it does is project templates.
             It follows those classic words.
             It's programmed to do one thing and do it well."
             
      - Longer description of the project. Text is saved in the
        generated docs-folder's longdescription.rst.

    * - ``package_name``
      - .. code::

            "alfabeta"
      - Python package name (whatever you would import).

    * - ``repo_name``
      - .. code::

            "alfabeta"
      - Repository name on GitHub (and project's root directory name).

    * - ``website``
      - .. code::

            "https://github.com/<github_username>/<repo_name>"
      - Website of the author.

    * - ``initial_year_to_release``
      - .. code::

            "2017"
      - Initial copyright year.

    * - ``initial_version``
      - .. code::

            "0.1.0"
      - The initial released version.





Next time, there is no need to clone again. Just run::

    (PY3VS) cd py3project1
    (PY3VS) cookiecutter cookiecutter-py3starter


Project requirements
--------------------

Use *requirement.txt* to install remaining project depedencies in the virtual environment::
    
    (PY3VS) cd <project_name>
    (PY3VS) pip install --upgrade --requirement=requirements.txt
    
or run::

    (PY3VS) make requirements


Version management
------------------

Create an *empty* initial repository at GitHub. Then create a local
git repository and push it to your new GitHub repository::

    (PY3VS) git init .
    (PY3VS) git add .
    (PY3VS) git commit -m "Initial commit"
    (PY3VS) git remote add origin git@github.com:<github_username>/<repo_name>.git
    (PY3VS) git push -u origin master

On-line documentation
---------------------

Add the repo to your ReadTheDocs-account_ and turn on the ReadTheDocs service hook.


Makefile
--------

For development usage, run *make* without any arguments::

    [develop and test]----------------------------------
    requirements -- installs the project requirements
    develop ------- installs project in develop mode
    lint ---------- checks style with flake8
    test ---------- run tests with the default <python-version>
    manifest ------ check completeness of the manifest file
    coverage ------ run unit and coverage tests
    report -------- run unit test, coverage and creates html report
    clean --------- removes all build, test and Python artifacts
    [documentation]-------------------------------------
    html ---------- creates html documentation with sphinx
    man ----------- creates man pages with sphinx
    [release]-------------------------------------------
    uninstall ----- removes installed package from Python's site-packages
    dist ---------- creates source and binary wheel packages
    install ------- installs the package to the active Python's site-packages
    install-wheel - installs the wheel binary to Python's site-packages
    pypi-test ----- upload source and binary wheel packages to test PyPI
    pypi ---------- upload source and binary wheel packages to PyPI


Before submitting anything to PyPI_ please read Hynek Schlawack's `Sharing Your Labor of Love: PyPI Quick
and Dirty <https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/>`_.


Not exactly what you want?
--------------------------

Well, have a look at a-pantry-full-of-cookiecutters_

If you have criticism or suggestions please open up an Issue or Pull Request.

.. _Green: https://github.com/CleanCut/green
.. _coverage: https://coverage.readthedocs.io/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _ReadTheDocs-account: https://readthedocs.org/dashboard/import
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _virtual-environment: https://docs.python.org/3.4/library/venv.html#
.. _a-pantry-full-of-cookiecutters: https://github.com/audreyr/cookiecutter#a-pantry-full-of-cookiecutters
.. _PyPI: https://pypi.python.org/pypi
