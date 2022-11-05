#!/usr/bin python3
#import date and time and assign to variable
from datetime import datetime

time = datetime.now()
now = time.strftime('%m/%d/%Y %I:%M:%S %p')#set format of time 

def welcome():
    print('Well Hello There ')
def time():
    print(f'The current time is {now}')
def getname():
    print('Enter your name:')#get input name to print 
    name = input()
    return(name)
def getage():
    print('Enter your age:')#get input age to print 
    age = input()
    return age
def start():     
    welcome()
    time()
    n = getname
    na = (f"Username is: {n()}")
    print(na)
    a = getage
    ag = (f'Your age is: {a()}') 
    print(ag)
