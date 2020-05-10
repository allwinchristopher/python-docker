#!/usr/bin/python3

####### Listing out of directories and file in python #########

import os

basedir=os.path.dirname(__file__)
dirlist=os.listdir(basedir)

for list in dirlist:
   print("File/Dir list:",list)
