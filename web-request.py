#!/usr/bin/python3

import os
import requests as r 

req=r.get("http://www.google.com")
reqerr=r.get("http://www.webcode.me/news")

URL=req.url

print("Response code for %s is %s" %(URL,req.status_code))
print("Response code for %s is %s" %(reqerr.url,reqerr.status_code))
