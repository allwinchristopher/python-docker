#!/usr/bin/python3

from flask import Flask, render_template    ######## Importing the Flask & render_template module to server the html files for web server

allhtml=Flask(__name__)

@allhtml.route("/")
def root():

  return render_template("webapp.html")     ############ Create a folder "template" in the source directory and place html files there as "render_template" function will look for html file under templates directory


@allhtml.route("/python")

def python():
  return render_template("python.html")


if __name__ == "__main__":

   allhtml.run(debug=True)
     


