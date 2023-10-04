The Hypermodern Python Project
==============================

.. toctree::
    :hidden:
    :maxdepth: 1

    license


The example project for the
`Hypermodern Python <https://cjolowicz.github.io/posts/hypermodern-python-01-setup/>`_ article series.
The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/>`_.


Installation
------------

To install this project, run this command in your terminal

.. code-block:: console

    $ pip install franco-hypermodern-python


Usage
-----

.. code-block:: console

    $ franco-hypermodern-python [OPTIONS]

.. option:: -l <language>, --language <language>

    The Wikipedia language edition,
    as identified by its subdomain on
    `wikipedia.org <https://www.wikipedia.org/>`_.
    By default, the English Wikipedia is selected.

.. option:: --version

    Display the current version and exit.

.. option:: --help

    Display a short usage message and exit.
