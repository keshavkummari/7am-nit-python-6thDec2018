'''
Module: OS.walk

dirpath
dirnames
filenames

3-tuples (dirpath, dirnames, filenames)

Module : fnmatch:


#program to find specific file in directory:

import fnmatch
import os

rootpath= 'c:\\'

pattern = '*.mp3'

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        print(os.path.join(root,filename))


#program to find multiple file extensions in the directory

import fnmatch
import os
rootpath= 'c:\\'
images = ['*.jpg', '*.tif', '*.doc']
matches = []
for root,dirnames,filenames in os.walk(rootpath):
    for extensions in images:
            for filename in fnmatch.filter(filenames,extensions):
                matches.append(os.path.join(root, filename))
                print(os.path.join(root,filename)) #or print(matches)

#create, Read and write, seek a file

'''