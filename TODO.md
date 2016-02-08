TODO
====

- extracting urls from network traffic
- create a workflow for automated malware detection

network
----------

~~implement network sniffer~~
- try to extend [BaseSniffer][URLSniffer] so that we can parse every single url
that was passed around in a [Pcap][Pcap] file

malware
----------

- try to connect to [Cuckoo Sandbox][Cuckoo]

[Cuckoo]: https://downloads.cuckoosandbox.org/docs/
[URLSniffer]: https://github.com/abzcoding/aptdetector/blob/master/aptdetector/network/sniffer.py
[Pcap]: https://en.wikipedia.org/wiki/Pcap
