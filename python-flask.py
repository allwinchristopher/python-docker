#!/usr/bin/python3

from flask import Flask  #### Importing python Flask module to create flask web server 

allweb=Flask(__name__)   ###  Create an instance of web application using Flask class and naming it to allweb(web application name)
 
@allweb.route("/")          ### Default web application route to root directory
 
def web():                 ### Define a function to server files for root directory
  return "Hello World"


@allweb.route("/test")

def test():
   return "Function is tested"

if __name__ == "__main__":   ### Validates the __name__ variable matches with the __main__ function as its base main program
  allweb.run(debug=True)
