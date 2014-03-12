#!/usr/bin/python
#===============================================================================
# @Mikematic
# 01.31.2011
# 
# FileController module consists of a set of utility methods that are required
# for comparing folders, filtering folders etc
#
#===============================================================================
import hashlib
import os.path
from mydict import mydict
import cPickle
import time

#
# Name:    getListOfFiles
#
# Desc:    This method takes a directory as parameter and returns a list of all the files in directory
#            e.g: ['/home/blackmatrix/Music/a/1.mp3' ...]
#
# Para:    @directory - path to the location of the directory that is required to produce the list
#              e.g: '/home/blackmatrix/Music/
#
def getListOfFiles(directory):
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
            else:
                files.append(fullname)
    return files

#
# Name:    getFilesNPath
#
# Desc:    This method takes a directory and returns a list containing two values.
#          the file name and full path to the file
#              e.g: [ ['plej - you.mp3', '/home/blackmatrix/Music/plej - you.mp3'] ... ]
#
# Para:    @directory - path that points to the directory that is required to generate the list
#              e.g: '/home/blackmatrix/Music/'
#
def getFilesNPath(directory):
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
            else:
                files.append([str(file), str(fullname)])
    return files

#
# Name:    getHashSum
#
# Desc:    This method takes the path to the file as parameter and returns the md5 hashsum of the
#          file.
#
# Para:    @filename - path that points to the location of the filename
#              e.g: '/home/blackmatrix/Music/plej - you.mp3'
#
def getHashSum(filename):
    m = hashlib.md5()
    filedata = file(filename, 'rb')
    while True:
        d = filedata.read(8096)
        if not d:
            break
        m.update(d)
    return str(m.digest())

#
# Name:    getHashNFileDict
#
# Desc:    This method takes a directory path as parameter and returns a dictionary(mydict) 
#          that consists a pairing of "the hash sum of the file" and  "the path to the file" 
#              e.g {'\xa1\x9b.\x8f\xb5\xaa\xe9-\nvH@\x0c\xa8\x1du', '/home/blackmatrix/Music/plej - you.mp3'...}
#
# Para:    @directory - path that points to the location of the directory to produce the hashNFile dictionary
#              e.g: '/home/blackmatrix/Music/
#
def getHashNFileDict(directory):
        hash_nfile_dict = mydict()
        listOfFiles = getListOfFiles(directory)
        for f in listOfFiles:
            key = getHashSum(str(f).strip())
            value = str(f).strip()
            if hash_nfile_dict.has_key(key):
                print 'key: %s and value: %s --Duplicate' % (key, value)
            else:
                hash_nfile_dict[key] = value
        return hash_nfile_dict
    
#
# Name:    writeHashNFileDictToFile
#
# Desc:    This method takes a dictionary of the type {"hash value of the file": "path to file"
#          and writes this dictionary into an output file using the cPickle module
#          the name of the file that is output will have the name given in the parameter fileToDumpTo
#            
#
# Para:    @hash_nfile_dict - name of the hash_nfile_dict that looks like below
#              e.g: {'\xa1\x9b.\x8f\xb5\xaa\xe9-\nvH@\x0c\xa8\x1du', '/home/blackmatrix/Music/plej - you.mp3'...} 
#          @fileToDumpTo - name of the file to dump the data to
#              e.g: 'ipodHashNFileList.dat' 
#
def writeHashNFileDictToFile(hash_nfile_dict,fileToDumpTo):
        theFile = open(fileToDumpTo,'w')
        cPickle.dump(hash_nfile_dict, theFile)
        theFile.close()
        print 'Dumping dictionary complete. Check for file %s' % fileToDumpTo

#
# Name:    loadFile
#
# Desc:    This method takes a the data file dumped by the method writeHashNFileDictToFile
#          returns the data and should be received in a mydict dictionary
#            
#
# Para:    @datafile - file to be loaded 
#
def loadFile(datafile):
    pickleddump = open(datafile)
    return cPickle.load(pickleddump)

#
# Name:    generateDictNFile
#
# Desc:    This method uses the getHashNFileDict and writeHashNFileDictToFile to combine the job of
#          producing the mydict dictionary and writing it to a file
#
# Parm:    directory - is the path to the location of the directory
#              e.g: '/home/blackmatrix/Music'
#          filename - is the name of the file to be generated
#              e.g: 'ipodDirectory.dat'
#
def generateDictNFile(directory, filename):
    print 'Started at ' , time.strftime("%I:%M:%S %p", time.localtime())
    print 'Processing folder %s' % directory
    print 'Getting hashNfile dictionary...'
    hashNfile = getHashNFileDict(directory)
    print 'Writing hashNfile directory to file'
    writeHashNFileDictToFile(hashNfile, filename)
    print 'Completed processing folder %s' % directory
    print 'Completed at ' , time.strftime("%I:%M:%S %p", time.localtime())

#
# Name:    getFileCount
#
# Desc:    Returns the number of individual music files (mp3 and m4a) in folder @directory
#
# Parm:    @directory - is the path to the location of the directory
#
def getMusicFileCount(directory):
    stack = [directory]
    files = []
    count = 0
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
            else:
                if str(fullname).lower().__contains__("m4a") or str(fullname).lower().__contains__("mp3"):
                    count +=1
                    print '%d. %s' % (count, str(fullname))                    
    print "Number of Files in directory is: %d" % count
    return count

# Name:    getFilenameFromPath
#
# Desc:    Returns the filename from a given path that is taken as parameter
#
# Parm:    @path - is the path to the location of the file
#

def getFilenameFromPath(path):
        explodedStrList = str(path).rsplit('/')
        return explodedStrList[len(explodedStrList) - 1]

