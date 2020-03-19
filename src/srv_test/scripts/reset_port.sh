#!/bin/sh
PORT_OLD=`cat port.txt`

PORT_NEW=$(($PORT_OLD + 1))
echo $PORT_NEW
if [ $PORT_NEW -gt 65535 ]; then
  PORT_NEW=49152
fi

echo $PORT_NEW > port.txt
cat port.txt
