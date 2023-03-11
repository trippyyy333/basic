import pyperclip as pc
from printy import *
copylist=[]

def checkclipboard(num):
    temp=False

    for i in range (num):
        lencopy = len(copylist)
        if lencopy==num:
            temp=False
            break
        else:
            asww=pc.waitForNewPaste()
            copylist.append(asww)
            i=+1
            continue


    printy(copylist)


take = int(input("how many: "))
checkclipboard(take)