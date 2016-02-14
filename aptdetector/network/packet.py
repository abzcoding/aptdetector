"""sample"""
import socket

from aptdetector.utils.typecheck import params, returns


class TcpPacket(object):
    """mimic a TcpPacket as we need it"""

    def __init__(self):
        """initialize a :class:`TcpPacket`"""
        # splited = str(value).split('-')
        self.__sourceHost = None
        self.__sourcePort = None
        self.__destinationHost = None
        self.__destinationPort = None
        self.__url = None

    def __str__(self):
        """string representation of :class:`TcpPacket` object"""
        res = str(self.sourceHost + ":" + str(self.sourcePort) + " ---> " +
                  self.destinationHost + ":" + str(
                      self.destinationPort) + "\n" + self.request)
        return res

    @params(self=object, target_id=int, show_port=bool, reverse=bool)
    def create_packet(self,
                      target_id,
                      show_port={bool: False},
                      reverse={bool: False}):
        """create an address based on target_id"""
        if (target_id == 1 and reverse is False) or (target_id == 2 and
                                                     reverse is True):
            if show_port:
                return self.sourceHost + ":" + str(self.sourcePort)
            else:
                return self.sourceHost
        elif (target_id == 2 and reverse is False) or (target_id == 1 and
                                                       reverse is True):
            if show_port:
                return self.destinationHost + ":" + str(self.destinationPort)
            else:
                return self.destinationHost
        else:
            return None

    @classmethod
    @returns(bool)
    def valid_ip(cls, addr):
        """check for valid ip

        Args:
            addr    (str):  an string that need to be checked
        Returns:
            True if addr is a valid ip address , False otherwise
        """
        try:
            socket.inet_aton(addr)
            return True
        except socket.error:
            return False

    @property
    @returns(str)
    def sourceHost(self):
        """get source host's ip"""
        return self.__sourceHost

    @sourceHost.setter
    @params(self=object, value=str)
    def sourceHost(self, value):
        """set source host's port"""
        if TcpPacket.valid_ip(value):
            self.__sourceHost = value

    @property
    @returns(int)
    def sourcePort(self):
        """get source host's port"""
        return self.__sourcePort

    @sourcePort.setter
    @params(self=object, value=int)
    def sourcePort(self, value):
        """set source host's port"""
        self.__sourcePort = value

    @property
    @returns(str)
    def destinationHost(self):
        """get destination host's ip"""
        return self.__destinationHost

    @destinationHost.setter
    @params(self=object, value=str)
    def destinationHost(self, value):
        """set destination host's ip"""
        if TcpPacket.valid_ip(value):
            self.__destinationHost = value

    @property
    @returns(int)
    def destinationPort(self):
        """get destination host's port"""
        return self.__destinationPort

    @destinationPort.setter
    @params(self=object, value=int)
    def destinationPort(self, value):
        """set destination host's port"""
        self.__destinationPort = value

    @property
    @returns(str)
    def request(self):
        """get requested url address"""
        return self.__url

    @request.setter
    @params(self=object, value=str)
    def request(self, value):
        """set requested url address"""
        self.__url = value
