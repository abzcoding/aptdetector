"""parse_pcap

parsing a pcap file so that later we would be able to use
the urls that was found to check for any harmfull activity

>>> from aptdetector.network.parser.parse_pcap import parse_pcap_file
>>> parse_pcap_file()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: parse_pcap_file() missing 1 required positional argument: 'file_path'
"""
from collections import OrderedDict
import io
import struct

from aptdetector.network.parser.httpparser import HttpType, HttpParser
from aptdetector.network.packet import TcpPacket
from aptdetector.utils.exception import FileParsingException

from pcapparser.constant import FileFormat
from pcapparser import packet_parser
from pcapparser import pcap, pcapng, utils
from pcapparser.utils import is_request


def get_file_format(infile):
    """get cap file format by magic num.

    Args:
        infile (file): saved Pcap file that is ready to be parsed
    Returns:
        file format and the first byte of string
    Raises:
        :class:FileParsingException when file is empty or too small
    """
    buf = infile.read(4)
    if len(buf) == 0:
        raise FileParsingException(str(infile) + " is empty")
    if len(buf) < 4:
        raise FileParsingException(str(infile) + " is too small")
    magic_num, = struct.unpack(b'<I', buf)
    if magic_num == 0xA1B2C3D4 or magic_num == 0x4D3C2B1A:
        return FileFormat.PCAP, buf
    elif magic_num == 0x0A0D0D0A:
        return FileFormat.PCAP_NG, buf
    else:
        return FileFormat.UNKNOWN, buf


class Stream(object):
    """stream handler

    handle the problem of tcp window and reassembling
    a packet by using tcp sequence number and keeping
    track of last ack sequence number
    """

    def __init__(self):
        """initialize :class:`Stream` object"""
        self.receive_buf = []
        self.status = 0
        self.last_ack_seq = 0

    def append_packet(self, packet):
        """packet appender

        if the packet is after last ack sequence then
        it's a new packet so add it to buffer , and we
        will deal with it later

        Args:
            packet (TcpPack): packet that need to be appended
        """
        if packet.seq >= self.last_ack_seq and packet.body:
            self.receive_buf.append(packet)

    def retrieve_packet(self, ack_seq):
        """packet reassmbler

        read all packets till now and reassmble a packet
        based on it's ack sequence number

        Args:
            ack_seq (int): ack sequence number
        Returns:
            the whole packet that were reassembled
        """
        if ack_seq <= self.last_ack_seq:
            return None

        self.last_ack_seq = ack_seq
        data = []
        new_buf = []
        for packet in self.receive_buf:
            if packet.seq < ack_seq:
                data.append(packet)
            else:
                new_buf.append(packet)
        self.receive_buf = new_buf
        if len(data) <= 1:
            return data
        data.sort(key=lambda pct: pct.seq)
        new_data = []
        last_packet_seq = None
        for packet in data:
            if packet.seq != last_packet_seq:
                last_packet_seq = packet.seq
                new_data.append(packet)
        return new_data


class TcpConnection(object):
    """pcap tcp parser

    parse a pcap file and creates :class:`TcpPacket`
    objects from that by the help of packetparse project
    """

    def __init__(self, packet):
        """initialize :class:`TcpConnection`

        Args:
            packet (TcpPack): packet that need to be appended
        """
        self.up_stream = Stream()
        self.down_stream = Stream()
        self.client_key = packet.source_key()

        self.is_http = None
        self.http_parser = HttpParser()
        self.on_packet(packet)

    def on_packet(self, packet):
        """parse a :class:`TcpPack` object.

        change attributes(ack, sin, fin , ...) of a :class:`TcpPack` object

        Args:
            packet (TcpPack): packet that need to be appended
        Returns:
            a tcp request header
        """
        all_packets = None
        if self.is_http is None and packet.body:
            self.is_http = is_request(packet.body)

        if self.is_http is False:
            return

        if packet.source_key() == self.client_key:
            send_stream = self.up_stream
            confirm_stream = self.down_stream
            pac_type = HttpType.RESPONSE
        else:
            send_stream = self.down_stream
            confirm_stream = self.up_stream
            pac_type = HttpType.REQUEST

        if len(packet.body) > 0:
            send_stream.append_packet(packet)
        if packet.syn:
            pass
        if packet.ack:
            packets = confirm_stream.retrieve_packet(packet.ack_seq)
            if packets:
                for packet in packets:
                    tcp = self.http_parser.send(pac_type, packet.body)
                    if tcp is not None:
                        all_packets = tcp
        if packet.fin:
            send_stream.status = 1
        return all_packets

    def closed(self):
        """check if this is the end of a conversation

        Returns:
            True if the connection is closed , False otherwise
        """
        return self.up_stream.status == 1 and self.down_stream.status == 1

    def finish(self):
        """if the connection was :func:`closed` then it is finished"""
        self.http_parser.finish()


def parse_pcap_file(file_path):
    """pcap parser.

    parse a pcap file to get a list :class:`TcpPacket` objects

    Args:
        file_path (str): address of the Pcap file that is ready to be parsed
    Returns:
        list of :class:TcpPacket of found conversations in the Pcap file
    Raises:
        :class:FileParsingException if either file format were not recognized or file was not found
    """
    conn_dict = OrderedDict()
    all_packets = []
    try:
        with io.open(file_path, "rb") as infile:
            file_format, head = get_file_format(infile)
            if file_format == FileFormat.PCAP:
                pcap_file = pcap.PcapFile(infile, head).read_packet
            elif file_format == FileFormat.PCAP_NG:
                pcap_file = pcapng.PcapngFile(infile, head).read_packet
            else:
                FileParsingException("unknown file format.")
            for tcp_pac in packet_parser.read_tcp_packet(pcap_file):
                key = tcp_pac.gen_key()
                # we already have this conn
                if key in conn_dict:
                    url = conn_dict[key].on_packet(tcp_pac)
                    if url is not None:
                        packet = TcpPacket()
                        packet.request = url
                        splited = str(key).split('-')
                        packet.sourceHost = splited[0].split(':')[0]
                        packet.destinationHost = splited[1].split(':')[0]
                        packet.sourcePort = splited[0].split(':')[1]
                        packet.destinationPort = splited[1].split(':')[1]
                        all_packets.append(packet)
                    # conn closed.
                    if conn_dict[key].closed():
                        conn_dict[key].finish()
                        del conn_dict[key]
                # begin tcp connection.
                elif tcp_pac.syn and not tcp_pac.ack:
                    conn_dict[key] = TcpConnection(tcp_pac)
                elif utils.is_request(tcp_pac.body):
                    # tcp init before capture, we start from a possible http request header.
                    conn_dict[key] = TcpConnection(tcp_pac)
    except (FileNotFoundError, FileParsingException):
        raise FileParsingException("parse_pcap failed to parse " + str(
            file_path))
    # finish connection which not close yet
    for conn in conn_dict.values():
        conn.finish()
    return all_packets
