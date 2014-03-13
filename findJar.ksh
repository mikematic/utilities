#!/usr/bin/ksh

folderToSearch=/app/WebSphere/was7x/Was70Install/java/jre
listOfJars=$(find $folderToSearch -name "*.jar")
for jarFile in $listOfJars
do
	classFiles=$(jar -tvf $jarFile |grep Debug |awk '{print $8}')
	for classFile in $classFiles
	do
		#if [[ -z "$classFile" ]]; then
		#echo "classFile is null"
		#else
	 	#echo "$classFile"
		#fi
		echo "$classFile in $jarFile"
	done	
done
