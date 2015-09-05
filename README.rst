================
Fileflood-ignore
================

A Fileflood plugin used to ignore files that match a pattern.

Installation
------------

::

    pip install fileflood-config

Usage
-----

Ignore a specified file:

.. code-block:: python

    from fileflood_ignore import Ignore

    fileflood.use(
        Ignore('posts/badger.md')
    )

Ignore many files at once:

.. code-block:: python

    Ignore('posts/badger.md', 'foo/bar.html')

Ignore all json files:

.. code-block:: python

    Ignore('**/*.json')

License
-------

MIT