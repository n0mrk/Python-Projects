#!/usr/bin/python

print "Start backup sync of Man Movies!"

import os
import shutil
sourcePath = r'/plexmedia/Movies/ManMovies'
destPath = r'/backups/plexmedia/Movies/ManMovies'

# Find files in first directory
files1 = []
for root,  dirs,  files in os.walk(sourcePath):
    files1.extend(files)
    
#print "Files in:",  root,  [f for f in files1]

# Find files in second directory
files2 = []
for root, dirs, files in os.walk(destPath):
    files2.extend(files)
    
#print "Files in:", root,   [f for f in files2]

#Compare the two diretories
print "Files not in:", root,   [f for f in files1 if f not in files2]

#loop through all files in the source directory - files1
for f in files1: 
    oldLoc =  sourcePath +'/' + f
    #print "oldLoc:",  oldLoc
 
    newLoc = destPath + '/' + f
    #print "newLoc:",  newLoc
    
    if f not in files2:
        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc,  newLoc)
                print('File '+ f + ' copied.')
            except IOError:
                print('File "' + f + '" already exists, or other bone-head mistake!')

print "All done!"
    


    
