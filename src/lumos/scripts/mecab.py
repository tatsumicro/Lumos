# -*- coding: UTF-8 -*-
#
# update: 2018/07/19 
# created by: tatsumi
#
import sys
import codecs
import MeCab

import re # split
import pprint # pretty print


def mecab_parse( str_in ):
    mec = MeCab.Tagger()
    p = mec.parse( str_in )
    return p


# MeCabを用いた形態素解析
def parse( str_in ):
    p = mecab_parse( str_in )
    array = p.split( "\n" )
    matrix = [ re.split('[\t,]', array[i]) for i in range(0, len(array) - 2) ]
    return matrix


def decode( str_or_list ):
    return str( str_or_list ).decode('string-escape')


def test():
    str_temp = raw_input( ">" )
    str_res = parse( str_temp )
    print( decode(str_res) )
