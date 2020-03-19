# -*- coding: utf-8 -*-

import serial
from connector import Connector

DEFALUT_TIMEOUT = 3

class SerialConnector(Connector):
    """Serial connector class"""
    __slots__ = ['is_connected', 'com_port', 'baudrate', 'timeout']

    def __init__(self):
        self._ser = serial.Serial()
        self._is_connected = False

    def connect(self, com_port, baudrate, timeout):
        self._ser.port = com_port
        self._ser.baudrate = baudrate
        self._ser.timeout = timeout
        self._ser.open()
        self._is_connected = True
        return True

    def disconnect(self):
        self._ser.close()
        self._is_connected = False

    def clear_recieve_buffer(self):
        self._ser.flushInput()

    def send_data(self, data):
        if self._is_connected == False:
            raise Exception('Serial port has not connected yet!')

        self._ser.write(data)
        return True

    def receive_data(self, read_byte_size):
        if self._is_connected == False :
            raise Exception('Serial port has not connected yet!')

        return self._ser.read(read_byte_size)

if __name__ == '__main__':
    main()
