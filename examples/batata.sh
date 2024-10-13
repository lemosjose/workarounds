#/!/bin/bash
#
#
#
while true
do 
	rsync -av --timeout=900 $1 $2
	sleep 1
done

