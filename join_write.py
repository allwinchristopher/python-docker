#!/usr/bin/python3

########## Writing the contents to a file by joining the Directory relative path and file name ############

import os

print("Setting Target File path:")

targetpath=os.path.join(os.path.dirname(__file__),"test_write_join.txt")

print("Target Path:", targetpath)

with open(targetpath,"w+") as filewrite:
   filewrite.write("Hello file is written")
   filewrite.seek(0,0)
   print(filewrite.read())
