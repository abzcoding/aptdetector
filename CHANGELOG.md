# APTDetector Changelog

Since February 07, 2016 there have been 1 releases and 14 commits for

an average of one 13-commit release every 1 weeks.
## 0.1.4
* [Stage Zero][stages] is now completed
* [BaseSniffer][basesniffer] connections can now filter to show specifiec source or destination
* fixed a problem in readthedocs

## 0.1.3
*(February 13, 2016)*
* [BaseSniffer][basesniffer] is now finished and capable of parsing a [Pcap][Pcap] file
* fixed doctests to pass travis ci
* released the new newversion to pypy

## 0.1.2

*(February 11, 2016)*

* started documentating
* fixed versioning problem

## 0.1.1

*(February 9, 2016)*

* changed the base of network scanner to [pcap-parser][pcap-parser] instead of [CapTipper][CapTipper]
* created [sniffer][URLSniffer] for basic monitoring connections in a [Pcap][Pcap] file

## 0.1.0

*(February 8, 2016)*

created the basic structure of the project.

* Used [CapTipper][CapTipper] as the base for network analysis module

## 0.0.0

*(February 7, 2016)*

Project Started.



[CapTipper]: http://captipper.readthedocs.org/en/latest/
[pcap-parser]: https://github.com/caoqianli/pcap-parser
[URLSniffer]: https://github.com/abzcoding/aptdetector/blob/master/aptdetector/network/sniffer.py
[Pcap]: https://en.wikipedia.org/wiki/Pcap
[stages]: https://github.com/abzcoding/aptdetector/blob/master/STAGES.md
