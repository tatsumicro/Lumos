# -*- coding: utf-8 -*-

import abc

class Connector(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def connect(self, com_port, baudrate, timeout):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def send_data(self, data):
        pass

    @abc.abstractmethod
    def receive_data(self, read_byte_size):
        pass
