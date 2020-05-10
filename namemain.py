#!/usr/bin/python3

##############  Here the placeholder value is __main__ as this program is not being imported from any other program. #############

print("Function is a %s function" %__name__)

################   Here the __name__ value is set to __main__ fuction as it is a base main program #################

if __name__ == "__main__":
   print("This function is a main function")
else:
   print("This is an imported function")
