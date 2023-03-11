import os
from pushbullet import PushBullet
from subprocess import call
import pyautogui
import time


API_KEY = "o.GVZrbiVF4S58asf6FsZaYsQoiquCkMxW"
txt = "this is a test warning before a game will begin"
import random

drop = random.randrange(100)

print('Beginning file download with urllib2...')

url = 'https://query1.finance.yahoo.com/v7/finance/download/ETH-USD?period1=1486944000&period2=1644710400&interval=1d&events=history&includeAdjustedClose=true'
urllib.request.urlretrieve(url, '/Users/scott/Downloads/cat.jpg')

"""
		bet = " your program will start shortly"
		text = "hiii"
		pb = Pushbullet(API_KEY)
		push = pb.push_note('pleasse remember 👽👽👽', bet)

"""