#!/usr/bin/ksh

folderToSearch=/home/mikematic/
listOfPDFs=$(find $folderToSearch -name "*.pdf")
for PDF in $listOfPDFs
do
	scp "$PDF" /home/mikematic/temp
done
