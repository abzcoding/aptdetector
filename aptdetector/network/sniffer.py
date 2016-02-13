"""``sniffer`` contains base network sniffer implemntation

but if you
want to use it, Currently there are two implementation to choose from:
* :class:`URLSniffer` - Sniff urls that are moving around in network
* :class:`FileSniffer` - Sniff files that are in the network
Both classes are :class:`BaseSniffer` subtypes
"""
# TODO(implement a test scenrario)

from aptdetector.network.parser.parse_pcap import parse_pcap_file
from aptdetector.utils.exception import FileParsingException
from aptdetector.utils.typecheck import params, returns


class BaseSniffer(object):
    """The ``BaseSniffer`` is an implementation of a bare minimum network sniffer.

    Raises:
        FileNotFoundError: pcap_file was not found on the system or you do not have permission

    >>> from aptdetector.network.sniffer import BaseSniffer
    >>> base_sniffer = BaseSniffer()
    >>> base_sniffer.pcap_file='/tmp/notexist.pcap'
    [Errno 2] No such file or directory: '/tmp/notexist.pcap'
    >>> base_sniffer.pcap_file
    >>> base_sniffer.pcap_file='examples/test.pcap'
    >>> base_sniffer.pcap_file
    'examples/test.pcap'
    >>> for pkt in base_sniffer.connections():
    ...    print(pkt)
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'NoneType' object is not iterable
    >>> base_sniffer.parse()
    >>> for pkt in base_sniffer.connections():
    ...    print(pkt)
    ...
    182.160.157.199:80 ---> 192.168.204.136:49174
    http://www.magmedia.com.au/
    182.160.157.199:80 ---> 192.168.204.136:49178
    http://www.magmedia.com.au/wp-includes/js/jquery/jquery.js?ver=1.7.2
    182.160.157.199:80 ---> 192.168.204.136:49178
    http://www.magmedia.com.au/wp-content/uploads/2014/01/MetroWest_COVER_Issue2_Feb2014.jpg
    108.61.196.84:80 ---> 192.168.204.136:49184
    http://pixeltouchstudios.tk/seedadmin17.html
    173.244.195.17:80 ---> 192.168.204.136:49185
    http://grannityrektonaver.co.vu/15c0b14drr9f_1_08282d03fb0251bbd75ff6dc6e317bd9.html
    182.160.157.199:80 ---> 192.168.204.136:49178
    http://www.magmedia.com.au/images/footer/3000melbourne.png
    182.160.157.199:80 ---> 192.168.204.136:49178
    http://www.magmedia.com.au/images/footer/3207portmelbourne.png
    182.160.157.199:80 ---> 192.168.204.136:49178
    http://www.magmedia.com.au/wp-content/uploads/2012/09/background1.jpg
    173.244.195.17:80 ---> 192.168.204.136:49185
    http://grannityrektonaver.co.vu/00015d76d9b2rr9f/1415286120
    173.244.195.17:80 ---> 192.168.204.136:49187
    http://grannityrektonaver.co.vu/00015d766423rr9f/1415286120
    173.244.195.17:80 ---> 192.168.204.136:49185
    http://grannityrektonaver.co.vu/00015d76rr9f/1415286120/5/x00809070554515d565b010b03510053535c0505;1;6
    173.244.195.17:80 ---> 192.168.204.136:49185
    http://grannityrektonaver.co.vu/00015d76rr9f/1415286120/5/x00809070554515d565b010b03510053535c0505;1;6;1
    173.244.195.17:80 ---> 192.168.204.136:49185
    http://grannityrektonaver.co.vu/00015d76rr9f/1415286120/7
    173.244.195.17:80 ---> 192.168.204.136:49185
    http://grannityrektonaver.co.vu/00015d761709rr9f/1415286120
    173.244.195.17:80 ---> 192.168.204.136:49187
    http://grannityrektonaver.co.vu/00015d76rr9f/1415286120/8
    """

    def __init__(self):
        """conversations must be none at first"""
        self.__pcap_file = None
        self.__conversations = None

    def parse(self):
        """parse the pcap file using :class:parse_pcap_file"""
        try:
            all_packets = parse_pcap_file(self.__pcap_file)
            self.__conversations = all_packets
        except FileParsingException as err:
            print(err)
        except IOError as err:
            print(err)

    @property
    @returns(str)
    def pcap_file(self):
        """returns address of Pcap file"""
        return self.__pcap_file

    @pcap_file.setter
    @params(self=object, value=str)
    def pcap_file(self, value):
        """set the address of Pcap file"""
        try:
            with open(value):
                self.__pcap_file = value
        except IOError as err:
            print(err)

    def connections(self,
                    source=None,
                    destination=None,
                    simplify=False,
                    show_port=False):
        """parsed connections.

        The ``connections`` function is a list that contains all connections
        from source to any or from any to destination

        Args:
            source (str): Source Address in Network Connections
            destination (str): Destination Address in Network Connections
            simplify (bool): should we simplify the results
            show_port (bool): should we hide port numbers
        Returns:
            a List of Lists containing all the comminucations from source or to the destination
        Raises:
            None
        """
        if source is not None:
            target = source
            target_id = 1
        elif destination is not None:
            target = destination
            target_id = 2
        else:
            target = None
            target_id = 0

        if target is None:
            return self.__conversations
        else:
            if simplify is True and show_port is True:
                # TODO(aggregate results based on source only (without any port number))
                pass
            elif simplify is True and show_port is False:
                # TODO(aggregate results based on source and it's port number)
                pass
            else:
                all_packets = []
                for pkt in self.__conversations:
                    all_packets.append((pkt.sourceHost + ":" + str(
                        pkt.sourcePort), pkt.destinationHost + ":" + str(
                            pkt.destinationPort)))
                return list(set(all_packets))
