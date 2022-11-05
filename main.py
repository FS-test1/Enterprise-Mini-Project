#!/usr/bin/env python3
import portedcs as ported
from api import public, private
from flask import Flask

class get:
    def stepone():
        print("Please enter you name to proceed")
        name = ported.getname()
        print('Please enter your age')
        ported.getage()
        return name
    def steptwo():
        print('Would you like to see you Private host information? YES or NO')
        answer = input()
        answer = answer.upper()
        if answer == 'YES':
            stwo = private()
        else:
            stwo = ("you chose not to see your private host info")
        return stwo
    def stepthree():
        print("Would you like to see the full details of your IP?")
        answer = input()
        answer = answer.upper()
        if answer == 'YES':
            sthree = public()
        else:
            sthree = ('you chose not to see your public IP info')
        return sthree

na = get.stepone
n = (f'Hello Welcome {na()}')
s_two = {get.steptwo()}
print(s_two)
print(s_two, sep=' ', end='\n')

s_three = {get.stepthree()}

app = Flask(__name__)
@app.route("/", methods=['GET'])
def func():
    fun = (f'{n}<br>{s_two}<br>{s_three}')
    return fun
func()
@app.route("/headers/<string:name>",
methods=['GET'])
def headers(name):
  return name

app.run(host='0.0.0.0', port=8000)

if __name__ == "_main_":
    get()
