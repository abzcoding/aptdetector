"""``sniffer`` contains base network sniffer implemntation, but if you
want to use it, Currently there are two implementation to choose from:
  * :class:`URLSniffer` - Sniff urls that are moving around in network
  * :class:`FileSniffer` - Sniff files that are in the network
Both classes are :class:`BaseSniffer` subtypes
"""

# TODO(implement a test scenrario)

from aptdetector.network.pcap_parser_wrapper import parse_pcap_file
from aptdetector.utils.exception import FileParsingException
from aptdetector.utils.typecheck import accepts, returns
from overloading import overloaded, overloads

__all__ = ('BaseSniffer', 'URLSniffer')


class BaseSniffer(object):
    """The ``BaseSniffer`` is an implementation of a bare minimum network sniffer.

    Raises:
        FileNotFoundError: pcap_file was not found on the system or you do not have permission


    >>> base_sniffer = BaseSniffer()
    <BaseSniffer object at 0x123283922>
    >>> base_sniffer.pcap_file='/tmp/notexist.pcap'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: '/tmp/notexist.pcap'
    >>> base_sniffer.pcap_file
    None
    >>> base_sniffer.pcap_file='/tmp/a.pcap'
    >>> base_sniffer.pcap_file
    <_io.TextIOWrapper name='/tmp/a.pcap' mode='r' encoding='UTF-8'>
    """

    def __init__(self):
        """conversations must be none at first"""
        self.__pcap_file = None
        self.__conversations = None

    def run(self):
        """parse the pcap file using :class:parse_pcap_file"""
        try:
            parse_pcap_file(self.__pcap_file)
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
    @accepts(object, str)
    def pcap_file(self, value):
        """set the address of Pcap file"""
        try:
            with open(value):
                pass
        except IOError:
            raise FileNotFoundError
        self.__pcap_file = value

    @overloaded
    def connections(self):
        """connections"""
        # TODO(check the performance of this function)
        # not order preserving
        return list(set(self.__conversations))

    @overloads(connections)
    def connections(source=None,
                    destination=None,
                    simplify=False,
                    show_port=False):
        """The ``connections`` function is

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
            # target_id = 1
        elif destination is not None:
            target = destination
            # target_id = 2
        else:
            target = None
            # target_id = 0

        if target is None:
            return list()
        else:
            if simplify is True and show_port is True:
                # TODO(aggregate results based on source only (without any port number))
                pass
            elif simplify is True and show_port is False:
                # TODO(aggregate results based on source and it's port number)
                pass
            else:
                # TODO(show all conversations, do not simplify anything)
                pass


class URLSniffer(BaseSniffer):
    """:class:``URLSniffer`` is an implementation of the :class:``BaseSniffer``

    this class will identify the urls that are passing around in the network

    Raises:
        FileNotFoundError: pcap_file was not found on the system or you do not have permission

    >>> sniffer = URLSniffer()
    <URLSniffer object at 0x123283922>
    >>> sniffer.pcap_file='/tmp/sample.pcap'
    >>> sniffer.connections()
    {'10.66.133.90:56240':'220.181.90.14:443' ,'10.66.133.90:5620':'220.181.90.13:80' ,'10.66.133.90:47526':'220.181.90.13:80'}
    >>> sniffer.connections(source='10.66.133.90')
    {'10.66.133.90:56240':['220.181.90.14:443'] ,['10.66.133.90:5620':'220.181.90.13:80']}
    >>> sniffer.connections(source='10.66.133.90',simplify=True,show_port=True)
    {'10.66.133.90':['220.181.90.14:443','220.181.90.13:80']}
    >>> sniffer.connections(source='10.66.133.95',simplify=True)
    None
    >>> sniffer.connections(destination='220.181.90.14',simplify=True,show_ports=False)
    {'220.181.90.14':['10.66.133.90']}
    """

    def __init__(self):
        """sample"""
        BaseSniffer.__init__(self)
