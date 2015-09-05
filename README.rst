=============
rucola-ignore
=============

A Rucola plugin used to ignore files that match a pattern.

Installation
------------

::

    pip install rucola-config

Usage
-----

Ignore a specified file:

.. code-block:: python

    from rucola import Ignore

    rucola.use(
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