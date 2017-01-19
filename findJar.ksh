#!/usr/bin/ksh

if [ $# -eq 2 ]; then
  classOrPackageToSearch=$1
  jarFolder=$2
  listOfJars=$(find $jarFolder -name "*.jar")
  for jarFile in $listOfJars
    do
      echo "Checking $jarFile ..."
      classFiles=$(jar -tvf $jarFile |grep $classOrPackageToSearch |awk '{print $8}')
      for classFile in $classFiles
        do
          echo "\n\nFound $classOrPackageToSearch in package $classFile in jarfile $jarFile \n\n"
        done
    done
else
  echo "\nERROR: Incorrect arguments"
  echo "\nUSAGE: findjar.ksh [class or package name to search] [folder to search]\n"
fi
