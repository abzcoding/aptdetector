[![PyPI](https://img.shields.io/pypi/v/aptdetector.svg)](https://pypi.python.org/pypi/aptdetector) ![Python versions](https://img.shields.io/pypi/pyversions/aptdetector.svg) [![Build Status](https://travis-ci.org/abzcoding/aptdetector.svg?branch=master)](https://travis-ci.org/abzcoding/aptdetector) [![Coverage Status](https://coveralls.io/repos/github/abzcoding/aptdetector/badge.svg?branch=master)](https://coveralls.io/github/abzcoding/aptdetector?branch=master)

# This project is no longer maintained
---
## aptdetector

*Advanced Persistent Threat Detection by Using Network Analysis*

**aptdetector** is a simple try to gather all means of malware detection
from network analysis in one place, for educational purposes only.

* used [pcap-parser][pcap-parser] as the base for network analysis module
* use [Cuckoo Sandbox][Cuckoo] as automated malware detection

aptdetector is tested against Python 3.4, 3.5, and PyPy.
[Full and extensive docs would be available at Read The Docs.][rtd]
See what's new by checking the [CHANGELOG][changelog].

[rtd]: https://aptdetector.readthedocs.org/en/latest/
[changelog]: https://github.com/abzcoding/aptdetector/blob/master/CHANGELOG.md
[pcap-parser]: https://github.com/caoqianli/pcap-parser
[Cuckoo]: https://downloads.cuckoosandbox.org/docs/

## Installation

aptdetector can be added to a project in a few ways. There's the obvious one:
```sh
    pip install aptdetector
```

then, [thanks to PyPI][aptdetector_pypi], aptdetector is just an import away:

``` python
    import aptdetector
```

and if that did not work, you can use:
``` sh
    git clone https://github.com/abzcoding/pcap-parser.git
    cd pcap-parser
    python setup.py install
    cd ../
    git clone https://github.com/abzcoding/aptdetector.git
    cd aptdetector
    python setup.py install
```

However, due to the nature of utilities, application developers might
dependencies. See the [Integration][integration] section of the docs

[aptdetector_pypi]: https://pypi.python.org/pypi/aptdetector
[integration]: https://aptdetector.readthedocs.org/en/latest/architecture.html#integration

## Status

**Stage Zero** is now completed. you can use [v0.1.4](https://pypi.python.org/pypi/aptdetector/0.1.4) of software to test it:
``` python
    from aptdetector.network.sniffer import BaseSniffer
    sni = BaseSniffer()
    sni.pcap_file='examples/test.pcap'
    sni.parse()
    print(sni.connections(source='173.244.195.17',show_port=True,simplify=True))
    print(sni.connections(destination='192.168.204.136',show_port=False,simplify=True))
```
you can check out the [Stages](https://github.com/abzcoding/aptdetector/blob/master/STAGES.md) if you want to get a sense of project roadmap.

## Disclaimer

Please do not use this program in production!!
it's an educational project only.


## References

I've based my work loosely on some respectful papers
that i've linked below:

* [Packet sniffing a brief introduction][packetsniff]
* [Persistent threats and how to monitor and deter them][persistentthreat]
* [Effective and Efficient Malware Detection at the End Host][effectivemalware]
* [Detecting APT Activity with Network Traffic Analysis][detectingapt]
* [Inspecting DNS Flow Traffic for Purposes of Botnet Detection][inspectingdns]
* [BotMiner: Clustering Analysis of Network Traffic for Protocol- and Structure-Independent Botnet Detection][botminer]
* [Panorama: Capturing System-Wide Information Flow for Malware Detection and Analysis][panorama]

[packetsniff]: http://ieeexplore.ieee.org/xpl/login.jsp?tp=&amp;arnumber=1166620&amp;url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F45%2F26303%2F01166620.pdf%3Farnumber%3D1166620
[persistentthreat]: http://www.sciencedirect.com/science/article/pii/S1353485811700861
[effectivemalware]: https://www.usenix.org/legacy/event/sec09/tech/full_papers/kolbitsch.pdf
[detectingapt]: http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp-detecting-apt-activity-with-network-traffic-analysis.pdf
[inspectingdns]: http://geant3.archive.geant.net/Media_Centre/Media_Library/Media%20Library/gn3_jra2_t4_M4_deliverable.pdf
[botminer]: http://usenix.org/legacy/event/sec08/tech/full_papers/gu/gu_html/index.html
[panorama]: http://dl.acm.org/citation.cfm?id=1315261

## Gaps

Found something missing in the in `aptdetector`? something is broken in `aptdetector`?
If you are very motivated, submit [a Pull Request][prs]. Otherwise,
submit a short feature request on [the Issues page][issues], and we will
figure something out.

[architecture]: https://aptdetector.readthedocs.org/en/latest/architecture.html
[issues]: https://github.com/abzcoding/aptdetector/issues
[prs]: https://github.com/abzcoding/aptdetector/pulls
