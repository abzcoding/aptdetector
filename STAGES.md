# Project Stages

In this project we've tried to identify threats by using network analysis. to overcome the difficulties of the real world we've tried to break the project into multiple stages , so that if we couldn't finish the project , somebody else might get intersted and carry on the job.



## Stage Zero

In the very fist steps we must be capable of watching the network for any malware moving around, before any system gets infected.

* parse a [Pcap][pcap] file that was sniffed from network to get all passed URLs
* it must be capable of filtering the result by source or destination



## Stage One

We want to generalize the malware detection part eventually , but right now i think the [Cuckoo Sandbox][cuckoo] would be sufficient.

* create a workflow to analyse urls and files using [Cuckoo Sandbox][cuckoo]
* it must be capable of passing the urls that were sniffed from [Stage Zero][stagezero] to [Cuckoo Sandbox][cuckoo]



## Stage Two

Some of the current malwares in the wild are just a mutation of older ones, but due to lack of signature they cannot be detected , but maybe adding blacklisted hosts and community signature would help us to overcome that problem.

* use [Blacklists][blacklist] and [Signatures][signature] to increase the malware detection rate



## Stage Three

Some malwares would use known ports with their own protocol so they can evade detection , for example if some host is talking on port 443 but not using the https protocol, it is a little bit suspicious! don't you agree with me?

* use protocol analysis to detect unusual activity on known ports



## Stage Four

Many of the infected hosts will talk to [botnet C&C servers][botcnc] using [API][api] Call

* analyse http headers for any unsual http api call



## Stage Five

Many of the infected hosts contact their [botnet C&C servers][botcnc] periodically and/or with similar Packets , so in this stage we will introduce ways to detect those patterns and mark them as suspecius traffic.

* ***Time Based*** : infected host asks for specific (non whitelisted) dns name priodically.
* ***Dns Answer Based*** : in case many Dns name requests ends up with the same IP address (many APTs would try to hide by using different dns names for their C&C servers).
* ***TTL Value Based*** : packets that are transfered between infected hosts and C&C server have a very low TTL to be effective in running commands.
* ***Domain Name Based*** : another possible method is to check the percentage of meaningfull name in dns name.



## Stage Six

Do all the previous steps in *Realtime* (not from a saved [Pcap][pcap] file)

* another plus in this stage would be to check for any [IRC][irc] traffic to mark them as suspicious.



## Stage Seven

Use [WhiteList][whitelist] and [Machine Learning][maclearn] Algorithms to Lower down the [False Positives][falsepositive] .

## Stage Eight

If we're 100% sure that a network is clean ; for example in an Industrial Network when it's completely off the grid, and we've not connected any device to it; we can Train our program to consider all traffic in that stage clean , and the when we've connected our network to outside world we can use [Anomaly Detection][anomalydet] to increase our [Zero Day][zeroday] detection rate.



## Stage Nine

use [Traffic Classification][trafclass] to Manually analyse the suspecouis categories.



## Stage Ten

use [Dynamic Analyses][dynanal] and [Sandboxing][sandbox] to increase malware detection rate.



## ETC

and many other ideas that will be added gradually...

[cuckoo]: https://downloads.cuckoosandbox.org/docs/
[pcap]: https://en.wikipedia.org/wiki/Pcap
[blacklist]: https://zeltser.com/malicious-ip-blocklists/
[signature]: http://sanesecurity.com/
[botcnc]: https://en.wikipedia.org/wiki/Botnet#Organization
[api]: https://en.wikipedia.org/wiki/Application_programming_interface
[irc]: https://en.wikipedia.org/wiki/Internet_Relay_Chat
[falsepositive]: https://en.wikipedia.org/wiki/False_positives_and_false_negatives#False_positive_error
[whitelist]: https://en.wikipedia.org/wiki/Whitelist
[maclearn]: https://en.wikipedia.org/wiki/Machine_learning
[anomalydet]: https://en.wikipedia.org/wiki/Anomaly_detection
[zeroday]: https://en.wikipedia.org/wiki/Zero-day_(computing)
[trafclass]: https://en.wikipedia.org/wiki/Traffic_classification
[dynanal]: http://opensecuritytraining.info/MalwareDynamicAnalysis.html
[sandbox]: https://blog.avast.com/2012/11/16/what-is-the-avast-autosandbox-and-how-does-it-work/
[stagezero]: https://github.com/abzcoding/aptdetector/blob/master/STAGES.md
