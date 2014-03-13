#!/usr/bin/sh

file="/home/mikematic/temp/netstat.out"
hostname=`hostname`
#netstat -Aan | grep ESTABLISHED | awk '{print $1}' > netstat.out`
while read line
do
theAddress=`netstat -Aan | grep "$line" | awk '{print $5}'`
theProcess=`rmsock "$line" tcpcb`
#echo "The Address: $theAddress is $1 to $theProcess"
echo "$theProcess....Local address: $theAddress ($hostname)"
done <"$file"
