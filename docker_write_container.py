#!/usr/bin/python3

import os

wfiledir=os.path.dirname(__file__)

wfilepath=f"{wfiledir}/output/docker_write_file.txt"

with open(wfilepath) as wfile:
   
   wread=wfile.read()
   print("File written to the container is:", wread)
   




