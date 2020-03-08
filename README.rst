============================================================
TimestamPy: Automatic timestamp generation on the blockchain
============================================================

.. image:: https://img.shields.io/pypi/v/timestampy.svg
           :target: https://pypi.python.org/pypi/timestampy

.. image:: https://img.shields.io/travis/reale/timestampy.svg
           :target: https://travis-ci.org/reale/timestampy

.. image:: https://readthedocs.org/projects/timestampy/badge/?version=latest
           :target: https://timestampy.readthedocs.io/en/latest/?badge=latest


Usage
-----

TimestamPy is based on the `OpenTimestamps`_ project and on the ``inotify`` Linux kernel facility.

Install the package as follows:

    $ pip3 install timestampy

Then run:

    $ timestampy

By default, TimestamPy will watch the ``~/timestampy`` folder; each time a file is created and/or moved into it, a timestamp will be created on the Bitcoin blockchain.

.. _OpenTimestamps: https://opentimestamps.org/
