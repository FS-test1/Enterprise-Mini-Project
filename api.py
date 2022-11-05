#!/usr/bin/env python3
import json
from urllib.request import urlopen
import socket

#pulling public ip results
response = urlopen('http://ipwho.is/')
ipwhois = json.load(response)

def private():
  name = socket.gethostname()
  host = (f'Hostname: {name}')    
  ipadr = socket.gethostbyname(name)
  ip = (f'Private IP: {ipadr}')
  privinfo = (f'{host} {ip}')
  return privinfo

def public():
#filter ipwhois results
  city = (ipwhois['city'])
  state = (ipwhois['region_code'])
  time = (ipwhois['timezone']['current_time'])
  pubIP = (ipwhois['ip'])
  pubinfo = (f'Your public IP info: {pubIP} You are in: {city}, {state}, {time}')
  return pubinfo

def hostinfo():
  privhost = private
  pubhost = public
  print(f'{privhost()}\n{pubhost()}')

  
'''
if __name__ == '_main_':
  hostinfo()

  print('Your public IP info:') 
  print(pubIP)
  print('You are in:')
  print(f'{city}, {state} {time}')
'''
  
#print(private())
#gethost()
#publichost()
