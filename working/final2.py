from printy import *
import pyautogui
import time
import keyboard
import wget

import progressbar
import time

# importing packages
from pytube import YouTube
import os
import pyperclip as pc

biglist = []
keysave = []
copylist = []
esc_button = 'esc'


def keycheck():
    keycheck_temp = 0
    for i in keysave:
        if keysave[keycheck_temp] == esc_button:
            print("esc is pressed")
    keycheck_temp = keycheck_temp + 1
    keycheck()


def keyboardsave(keysave):
    az = keyboard.record()
    keysave.append(az)


def pausehotkey(i):
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
            print('space was pressed')
            itrr=True
            return itrr

def pastepause():
    keyboard.record(until=esc_button)
    rkk = keyboard.is_pressed('esc')
    if (not rkk):
        print("still")
        pass

def main5():
    try:
        print("h/")
        i=False
        while (not i):
            rk = keyboard.record(until='shift')
            asww = pc.waitForNewPaste()
            copylist.append(asww)
            if rk.startswith("http"):
                print("append")

                biglist.append(rk)
            else:
                i=True

                pass
        printy(biglist,"p>")
        return biglist

    except Exception as ex:
        printy(ex, "r>")




def checkclipboard():
    temp = 'false'
    if (temp == 'false'):
        pastepause()

        asww = pc.waitForNewPaste()
        copylist.append(asww)
        i = +1

    printy(copylist)


def main():
    try:
        print("h/")

    except Exception as ex:
        printy(ex, "r>")


if __name__ == '__main__':
    # pastepause()
    # checkclipboard()
    # main()

    #main5()
    # animation()
    # print(bigie)
    # take = int(input("how many: "))
    # checkclipboard(take)
    # main5()
    # downloadyt(copylist)
    # main22()
