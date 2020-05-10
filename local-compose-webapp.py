#!/usr/bin/python3

from flask import Flask
from redis import Redis

pyapp=Flask(__name__)
redis=Redis(host='127.0.0.1',port=6379)

@pyapp.route("/")

def root():
   redis.incr('webhits')
   return "The number of counts the URL has hitted is %s."  %redis.get('webhits')

@pyapp.route("/even")

def even():
   redis.set('num', '2')
   return "The num is %s" %redis.get('num') 

@pyapp.route("/odd")

def odd():
   redis.mset({'num2': '2', 'num3': '3'})
   return "The num3  is %s" %redis.get('num3')

@pyapp.route("/print")

def print():
      redis.set('num', '1')
      return "The number of printed nos: %s." %redis.incrby('num', '6')

      

if __name__ == "__main__":
   pyapp.run(host="0.0.0.0",debug=True)


