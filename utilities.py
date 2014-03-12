#!/usr/bin/python
#===============================================================================
# @Mikematic
# 02.12.2011
# 
# Utilities module that has a list of methods required extensively but temporarily
#===============================================================================

import mydict
import FileController
import ID3Controller

def checkForConsistency():
    ipod = mydict(FileController.loadFile('ipod.dat'))
    added = mydict(FileController.loadFile('added.dat'))    
    notadded = mydict(FileController.loadFile('notadded.dat'))
    toprated = mydict(FileController.loadFile('top_rated_01242010.dat'))
    ipodbkup = mydict(FileController.loadFile('ipodbkup.dat'))
    
    print len(ipod)
    print len(added)
    print len(notadded)
    print len(toprated)
    print len(ipodbkup)
    print'#########'
    print len(added.minus(ipod)) #should be 0
    print len(ipod.intersection(notadded)) #should be 0
    print len(added.intersection(notadded)) #should be 0

def checkFilesByTag():
    #
    # Compares the list of tracks in ipodtag with the one in local tag and prints out the ones
    # that exist in both
    #
    ipodtags = ID3Controller.getListOfTags("/media/MIKEMATIC'S/iPod_Control/Music/")
    localtags = ID3Controller.getListOfTags('/home/blackmatrix/Music/not_added/temp/')
    ############ 
    for tag1 in ipodtags:
        artist = str(tag1['artist']).strip()
        title = str(tag1['title']).strip()
        if artist != 'n.a' and title !='n.a':
            for tag2 in localtags:
                if str(tag2['artist']).strip() == artist and str(tag2['title']).strip() == title:
                    print 'Artist: %s and Song: %s ----exists in local' % (artist, title)
