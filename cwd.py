#!/usr/bin/python3

import os

AbsolutePath=os.path.dirname(__file__)
print("Absolute-Dir-Path:",AbsolutePath)
print("AbsoluteFileRelativePath:", __file__)

#  Getting file absolute path

print("AbsolutePath:", os.path.abspath(__file__))

print("AbsoluteFileBasePath:", os.path.basename(__file__))
Currentdirectory=os.getcwd()
print("CurrentDir:",Currentdirectory)
