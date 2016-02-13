.. aptdetector documentation master file, created by sphinx-quickstart on Thu Feb 07 09:18:01 2016.

aptdetector
===========

*Advanced Persistent Threat Detection by Using Network Analysis*

**aptdetector** is a humble try to gather all means of malware detection

from network analysis in one place, for educational purposes only.
what has been done so far:
* :class:`Network Sniffer <aptdetector.network.sniffer>`, sniff network for passing urls and files

APTDetector is tested against Python 3.4, 3.5, and PyPy

See what's new by checking `checking the CHANGELOG`_.

.. _checking the CHANGELOG: https://github.com/abzcoding/aptdetector/blob/master/CHANGELOG.md

Installation
------------

APTDetector can be added to a project in a few ways. There's the obvious one::

    pip install aptdetector

Then, aptdetector is just an import away::

    from aptdetector.network.sniffer import URLSniffer
    sniffer = URLSniffer
    sniffer.pcap_file = 'sample.pcap'
    sniffer.connections(source='10.66.133.90',simplify=True,show_port=True)

However, due to the nature of utilities, application developers might
dependencies. See the :ref:`Integration <arch_integration>` section of the docs

Disclaimer
----------

Please do not use this program in production!!
it's an educational project only.

References
----------

I've based my work loosely on some respectful papers
that i've linked below:

- `Packet sniffing a brief introduction`_.
- `Persistent threats and how to monitor and deter them`_.
- `Effective and Efficient Malware Detection at the End Host`_.
- `Detecting APT Activity with Network Traffic Analysis`_.
- `Inspecting DNS Flow Traffic for Purposes of Botnet Detection`_.
- `Clustering Analysis of Network Traffic for Protocol- and Structure-Independent Botnet Detection`_.
- `Capturing System-Wide Information Flow for Malware Detection and Analysis`_.

.. _Packet sniffing a brief introduction: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&amp;arnumber=1166620&amp;url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F45%2F26303%2F01166620.pdf%3Farnumber%3D1166620
.. _Persistent threats and how to monitor and deter them: http://www.sciencedirect.com/science/article/pii/S1353485811700861
.. _Effective and Efficient Malware Detection at the End Host: https://www.usenix.org/legacy/event/sec09/tech/full_papers/kolbitsch.pdf
.. _Detecting APT Activity with Network Traffic Analysis: http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp-detecting-apt-activity-with-network-traffic-analysis.pdf
.. _Inspecting DNS Flow Traffic for Purposes of Botnet Detection: http://geant3.archive.geant.net/Media_Centre/Media_Library/Media%20Library/gn3_jra2_t4_M4_deliverable.pdf
.. _Clustering Analysis of Network Traffic for Protocol- and Structure-Independent Botnet Detection: http://usenix.org/legacy/event/sec08/tech/full_papers/gu/gu_html/index.html
.. _Capturing System-Wide Information Flow for Malware Detection and Analysis: http://dl.acm.org/citation.cfm?id=1315261

.. _gaps:

Gaps
----

Found something missing in the in ``aptdetector``? something is broken in ``aptdetector``?
First, take a moment to read the very brief :doc:`architecture` statement to make
sure the functionality would be a good fit.

Then if you are very motivated, submit `a Pull Request`_. Otherwise,
submit a short feature request on `the Issues page`_, and we will
figure something out.

.. _a Pull Request: https://github.com/abzcoding/aptdetector/pulls
.. _the Issues Page: https://github.com/abzcoding/aptdetector/issues

Section listing
---------------

.. toctree::
   :maxdepth: 4

   architecture
   aptdetector

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
