#!/bin/bash

loops=$1
echo "starting reactor $loops times"
for ((loop=1;loop<=$loops;loop++))
do
 echo "Loop number: $loop !!!"
 for ((client=50;client<=1000;client+=50))
 do
	echo "CMD EXEC: sudo python tcpclient.py -t 300 -c $client"
	sudo python tcpclient.py -t 300 -c $client
 	sleep 1
 done
done
