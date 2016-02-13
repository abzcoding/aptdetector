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
        """string representation of :class:TcpPacket object"""
        res = str(self.sourceHost + ":" + str(self.sourcePort) + " ---> " +
                  self.destinationHost + ":" + str(
                      self.destinationPort) + "\n" + self.request)
        return res

    @returns(bool)
    def valid_ip(self, addr):
        """check for valid ip"""
        try:
            socket.inet_aton(addr)
            return True
        except socket.error:
            return False

    @property
    @returns(str)
    def sourceHost(self):
        """sample"""
        return self.__sourceHost

    @sourceHost.setter
    @params(self=object, value=str)
    def sourceHost(self, value):
        """sample"""
        if self.valid_ip(value):
            self.__sourceHost = value

    @property
    @returns(int)
    def sourcePort(self):
        """sample"""
        return self.__sourcePort

    @sourcePort.setter
    @params(self=object, value=int)
    def sourcePort(self, value):
        """sample"""
        self.__sourcePort = value

    @property
    @returns(str)
    def destinationHost(self):
        """sample"""
        return self.__destinationHost

    @destinationHost.setter
    @params(self=object, value=str)
    def destinationHost(self, value):
        """sample"""
        if self.valid_ip(value):
            self.__destinationHost = value

    @property
    @returns(int)
    def destinationPort(self):
        """sample"""
        return self.__destinationPort

    @destinationPort.setter
    @params(self=object, value=int)
    def destinationPort(self, value):
        """sample"""
        self.__destinationPort = value

    @property
    @returns(str)
    def request(self):
        """sample"""
        return self.__url

    @request.setter
    @params(self=object, value=str)
    def request(self, value):
        """sample"""
        self.__url = value
