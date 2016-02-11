Architecture
============

``aptdetector`` is trying to have minimalist architecture: remain as consistent, and
self-contained as possible, with an eye toward maintaining its range
of use cases and usage patterns as wide as possible.

.. _arch_integration:

Integration
-----------

Right now the malware module is heavily dependent on `Cuckoo Box`_.
but in the future i'll try to create an API and make that part optional.

.. _Cuckoo Box: https://downloads.cuckoosandbox.org/docs
