import pyautogui
import time
import schedule
from pushbullet import Pushbullet
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
engine.say('sedkii')
engine.say('kfaya oloaya')
engine.runAndWait()
API_KEY = "o.GVZrbiVF4S58asf6FsZaYsQoiquCkMxW"
txt = "this is a test warning before a game will begin"

bet = " your program will start shortly"
text = "hiii"
pb = Pushbullet(API_KEY)
push = pb.push_note('keep ringing', bet)

def tom():
    while True:
        engine.say('Mazen')
        engine.runAndWait()


def dam():
 pb = Pushbullet(API_KEY)
 push = pb.push_note('test dam', "baammmm")


schedule.every().day.at('05:57').do(dam)
schedule.every().day.at('12:55').do(tom)

while True:

    schedule.run_pending()