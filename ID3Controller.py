#!/usr/bin/python
#===============================================================================
# @Mikematic
# 01.31.2011
# Module to extract the ID3 Tag (v1, v2.2, v2.3, v2.4)
# Module uses the mutagen tag library found at /usr/local/lib/python2.6/dist-package/mutagen
#
#===============================================================================

import os.path
import FileController
from mutagen.mp3 import MP3
import mutagen.easyid3
from mutagen.easymp4 import EasyMP4
import cPickle
import mydict

#===============================================================================
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

def compareFolders(folder1, folder2):
    folder1files = getFilesNPath(folder1)
    folder2files = getFilesNPath(folder2)
    fileset1 = list(folder1files)
    fileset2 = list(folder2files)
    for file1 in folder1files:
        for file2 in folder2files:
            if file1[0] == file2[0]:
                fileset1.remove(file1)
                fileset2.remove(file2)
            else:
                continue
    print '############  Files in folder1 but not folder2  ####################'
    for file in fileset1:
        print file
    print '############  Files in folder2 but not folder1  ####################'
    for file in fileset2:
        print file
    
#===============================================================================
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

def getID3Tag(file):
    ##audio.keys() list of keys...
    title = 'n.a'
    album = 'n.a'
    artist = 'n.a'
    genre = 'n.a'
    if str(file).lower().endswith('mp3'):
        try:
            audio = mutagen.easyid3.EasyID3(file)
            try:
                title = audio['title'][0]
            except:
                title = u'n.a'
            try:
                artist = audio['artist'][0]
            except:
                artist = u'n.a'
            try:
                album = audio['album'][0]
            except:
                album = u'n.a'
            try:
                genre = audio['genre'][0]
            except:
                genre = u'n.a'
        except:
            print "Cant get tag for ---> %s" % str(file)
            id3Tag = {'title': title, 'artist': artist, 'album': album, 'genre': genre, 'filename': file}
    elif str(file).lower().endswith('m4a'):
        try:
            audio = EasyMP4(file)
            try:
                title = audio['title'][0]
            except:
                title = u'n.a'
            try:
                artist = audio['artist'][0]
            except:
                artist = u'n.a'
            try:
                album = audio['album'][0]
            except:
                album = u'n.a'
            try:
                genre = audio['genre'][0]
            except:
                genre = u'n.a'
        except:
            print "Cant get tag for ---> %s" % str(file)
            id3Tag = {'title': title, 'artist': artist, 'album': album, 'genre': genre, 'filename': file} 
    else:
        "print '%s is neither an mp3 or mp4' % file"
    id3Tag = {'title': title, 'artist': artist, 'album': album, 'genre': genre, 'filename': file} 
    return id3Tag

def getListOfTags(directory):
    files = getListOfFiles(directory)
    listOfTags = []
    for file in files:
        tag = getID3Tag(file)
        listOfTags.append(tag)
    return listOfTags

def compareDirectoriesOnHash(dir1, dir2):
    filesInDir1 = getFilesNPath(dir1)
    filesInDir2 = getFilesNPath(dir2)
    filesInDir1nmd5 = {}
    filesInDir2nmd5 = {}
    print '########### Begin processing Dir 1 Files... ######################'
    for file in filesInDir1:
        filesInDir1nmd5[file[1]] = FileController.getHashSum(file[1])
    print '########### Completed processing Dir 1 files ###########'
    print '########### Begin processing Dir 2 files... ################'
    for file in filesInDir2:
        filesInDir2nmd5[str(file[1]).strip()] = FileController.getHashSum(file[1])
    print '########### Completed processing Dir 2 files ###########'

    print '########### Begin comparing md5sums ####################'
    temp1 = dict(filesInDir1nmd5)
    temp2 = dict(filesInDir2nmd5)
    for dictkey1 in temp1.iterkeys():
        for dictkey2 in temp2.iterkeys():
            if temp1[dictkey1] == temp2[dictkey2]:
                filesInDir1nmd5.__delitem__(dictkey1)
                filesInDir2nmd5.__delitem__(dictkey2)
    print '########### Completed comparing md5sums'
    print '############ Files in Dir 1 but not in Dir 2 ########################'
    if filesInDir1nmd5 == {}:
        print 'No files in Dir 1 that are not in Dir 2'
    else:    
        for key in filesInDir1nmd5.iterkeys():
            print key
    print '############ Files in Dir 2 but not in Dir 1 ##################################'
    if filesInDir2nmd5 == {}:
        print 'No files in Dir 2 that are not in Dir 1'
    else:
        for key in filesInDir2nmd5.iterkeys():
            print key
    
#
# method getHasNFileDict takes the directory path (e.g: /home/blackmatrix/Music) as parameter
# method iterates through a directory and returns a dictionary
# of the pairing of hashsum of file values with 
# the full path of the file e.g {'\xa1\x9b.\x8f\xb5\xaa\xe9-\nvH@\x0c\xa8\x1du', '/home/blackmatrix/Music/plej - you.mp3'}
# n.b The dictionary used below is mydict. An extended module of the built-in dict class
#
def getHashNFileDict(directory):
        hash_nfile_dict = mydict()
        listOfFiles = getListOfFiles(directory)
        for f in listOfFiles:
            key = FileController.getHashSum(str(f).strip())
            value = str(f).strip()
            if hash_nfile_dict.has_key(key):
                print 'key: %s and value: %s --Duplicate' % (key, value)
            else:
                hash_nfile_dict[key] = value
        return hash_nfile_dict
    
#
# method writeHashNFileDictToFile takes the mydict hash_nfile_dict and name of the file to dump to
# method writes the mydict key-value pairs into a file by the name given in the second parameter
#
def writeHashNFileDictToFile(hash_nfile_dict,fileToDumpTo):
        theFile = open(fileToDumpTo,'w')
        cPickle.dump(hash_nfile_dict, theFile)
        theFile.close()
        print 'Dumping dictionary complete. Check for file %s' % fileToDumpTo
        
def compareMyPickleDumps(dump1, dump2):
        #Compare them using binary search to reduce time to O(n/2) from O(n^2)
        #Sort the binary hashes and do high low search
        pickledDump1 = open(dump1)
        pickledDump2 = open(dump2)        
        pickledDict1 = cPickle.load(pickledDump1)
        pickledDict2 = cPickle.load(pickledDump2)
        tempdict1 = dict(pickledDict1)
        tempdict2 = dict(pickledDict2)
        for key1 in pickledDict1:
            for key2 in pickledDict2:
                if pickledDict1[key1] == pickledDict2[key2]:
                    if tempdict1.has_key(key1):
                        tempdict1.__delitem__(key1)
                    else:
                        print 'Duplicate in dump2 of: %s' % key2
                    if tempdict2.has_key(key2):
                        tempdict2.__delitem__(key2)
                    else:
                        print 'Duplicate in dump1 of: %s' %key1
                else:
                    continue
        #=======================================================================
        # print 'Files in %s but not in %s' % (dump1, dump2)
        # for key in tempdict1:
        #    print '%s' % key
        # print '\n \n \n'
        # print 'Files in %s but not in %s' % (dump2, dump1)
        # for key in tempdict2:
        #    print '%s' % key        
        #=======================================================================
        return {dump1:tempdict1, dump2:tempdict2}

