#! /Users/stephenlang/anaconda/bin/python
# selectiveCopy.py - Walks through a folder tree and searches for files with a certain 
# file extension (such as .pdf or .jpeg).  These files will be copied from whatever
# location they are in to a new folder.

import os, shutil, re

#TODO: Take in a folder and a file extension as arguments
#TODO: Walk the folder tree
    #use os.walk
#TODO: Make a regex to match the file extention
#TODO: copy the files that have the given extension
    #use shutil.copy(source,destination)

def selectiveCopy(source, destination, extention):
    #check source validity
    if os.path.isdir(source) and os.path.isdir(destination):
        #create regex
        extRegex = re.compile(r'.*(\.'+extention+')')

        #loop through the Source Directory
        for foldername, subfolders, filenames in os.walk(source):
            print('The current folder is: '+ foldername)
            for filename in filenames:
                mo = extRegex.search(filename)

                #Skip files without the correct extention
                if mo == None:
                    continue
                    
                #move files that match the extention
                shutil.copy(os.path.join(source,filename),destination)
    else:
        print('The source and/or the destination provided does not exist.')

selectiveCopy(os.path.join('.','Source'),os.path.join('.','Destination'),'txt')