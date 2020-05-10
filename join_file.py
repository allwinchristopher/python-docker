#!/usr/bin/python3

########## Reading the contents of a file by joining the Directory relative path and file name ############

import os

print("Setting Target File path:")

targetpath=os.path.join(os.path.dirname(__file__),"test_join.txt")

print("Target Path:", targetpath)

with open(targetpath) as fileread:
   fileread.seek(0,0)
   print(fileread.read())
