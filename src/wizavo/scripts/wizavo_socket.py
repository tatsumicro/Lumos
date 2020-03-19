# -*- coding: UTF-8 -*-
#
# update: 2018/07/19 
# created by: tatsumi
#
#!/usr/bin/env python

# socket
from datetime import datetime
import socket
import binascii

# subprocess
import subprocess

# threading
import time
import threading


global isInitialized


def create( string ):
    if len( string ) > 0:
        client.sendall( string.encode('utf-8') )
        wavfile = client.recv( max_size )
        return wavfile
    else:
        return ""


def init( init_address, init_port ):
    global isInitialized

    global address
    global max_size
    global server
    global client
    global addr
    
    print( "init_address and init_port" )
    print( init_address )
    print( init_port )
    address = ( init_address, init_port )
    max_size = 1000
    print( 'Starting the server at', datetime.now() )
    print( 'Waiting for a client to call.' )
    isInitialized = True
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server.bind( address )
    server.listen( 5 )
    client, addr = server.accept()


def destroy():
    client.close()
    server.close()


def sample():
    set_address = 'localhost'
    port = int( open('port.txt').read() )
    print type( port )
    init( set_address, port )
    wavfile = create_wav( "こんにちは" )
    # wavfileを再生


