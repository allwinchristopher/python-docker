#!/usr/bin/python3

import os

basedir=os.path.dirname(__file__)    ###  Specifying the directory to be used for the file path
inputfilepath=f"{basedir}/input/input_file.txt"  ###  Using the 'f' string format the basedir string path
outputfilepath=f"{basedir}/output/docker_write_file.txt"

####  Using the with function to read/write file processing  #####

with open(inputfilepath) as input:
   with open(outputfilepath,"w+") as output:
       iread=input.read()
       finaloutput=output.write(iread)
       output.seek(0,0)  ## Seek function to bring back the cursor to initial state before reading the file
       print(output.read())  


