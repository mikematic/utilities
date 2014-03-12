#!/bin/sh

filename='greymatrix.dat'

while read line;
do
theFile=${line##*/}
greppedFile=`grep "$theFile" backup.dat.stripped`
if [ "$greppedFile" != "" ]; then
	#"File found do nothing"
	a=1
else
	echo "File not Found: " $line
fi
done<$filename
