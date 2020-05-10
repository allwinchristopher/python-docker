#!/usr/bin/python3

##############  Here we are importing the previous namemain program into another python  program
                So here in this import function __name__ will be module name (i.e) namemain ################   

import namemain

################# Here __name__  function will be assigned as __main__ = Base module #####################

print("Function is a %s function" %__name__)

if __name__ == "__main__":
   print("This function is a main function")
else:
   print("This is an imported function")

