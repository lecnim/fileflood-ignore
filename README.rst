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

    .. code-block:: python

    from fileflood_ignore import Ignore

    fileflood.use(Ignore('**/*.json'))


License
-------

MIT