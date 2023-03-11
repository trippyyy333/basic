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
from notifypy import Notify
from win10toast_click import ToastNotifier
import os

from win10toast import *
biglist = []
bigie = ['https://www.youtube.com/watch?v=fD2UExUhq-s', 'https://www.youtube.com/watch?v=PVjiKRfKpPI', 'https://www.youtube.com/watch?v=XfdgwJenJKY&list=TLPQMTkwNjIwMjIJlYcQjtj8LQ&index=4', 'https://www.youtube.com/watch?v=vOQNH8m6WoI']
copylist=[]


def toastnoti1():

    try:

        toaster = ToastNotifier()

        # showcase
        toaster.show_toast(
            "sorry fetch",  # title
            "Click to open URL! >>",  # message
            icon_path='C:\\Users\\mazen\\OneDrive\\Pictures\\icon\\5.ico',  # 'icon_path'
            duration=5,
            # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True,
            # True = run other code in parallel; False = code execution will wait till notification disappears
        )




    except:
        printy("sorry at toast noti","r")


def toastnoti():
    def open_urld():
        try:
            print("dgvfsd")
            # os.startfile(download_destination)
            print('Opening URL...')
        except:

            print('Failed to open URL. Unsupported variable type.')

    try:

        toaster = ToastNotifier()

        # showcase
        toaster.show_toast(
            "Music done",  # title
            "Click to open URL! >>",  # message
            icon_path='Z:\\projects\\working\\alien2.ico',  # 'icon_path'
            duration=5,
            # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True,
            # True = run other code in parallel; False = code execution will wait till notification disappears
             #callback_on_click=
        )




    except:
        printy("sorry at toast noti","r")


def toastnoti2():
    def open_urld():
        try:
            print("dgvfsd")
            # os.startfile(download_destination)
            print('Opening URL...')
        except:

            print('Failed to open URL. Unsupported variable type.')

    try:

        toaster = ToastNotifier()

        # showcase
        toaster.show_toast(
            "Music done",  # title
            "Click to open URL! >>",  # message
            icon_path='C:\\Users\\mazen\\OneDrive\\Pictures\\icon\\1.ico',  # 'icon_path'
            duration=1,
            # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True,
            # True = run other code in parallel; False = code execution will wait till notification disappears
             #callback_on_click=
        )
        pass




    except:
        printy("sorry at toast noti","r")


def checkclipboard(num):
    try:
        temp=False

        for i in range (num):
            lencopy = len(copylist)
            if lencopy==num:
                temp=False
                break
            else:
                asww=pc.waitForNewPaste()
                copylist.append(asww)
                toastnoti2()
                i=+1
                continue


        printy(copylist)
    except:
        toastnoti1()
        printy("sorry at audio", "r")


def checkclipboard2(num):
    temp=False
    while(not temp):

        for i in range (2):
            lencopy = len(copylist)
            if lencopy==num:
                temp=True
                break
            else:
                asww=pc.waitForNewPaste()
                copylist.append(asww)
                i=+1
                temp=False
                continue


    printy(copylist)





def pause3():

    rk = keyboard.record(until='enter')
    print("past sis pressed")
def pastepause(rkk):
    rkk =keyboard.is_pressed('esc')
    if (not rkk):
        print("still")
        pass


def pause():
    print("ggv")

def main():
    try:
        fal = False
        while(not fal):
            print("h/")
            inputlinks=str(input("yourlinks seperate with enter"))
            pause3()
            biglist.append(inputlinks)
            pastepause(fal)

        printy(biglist,"")




    except Exception as ex:
        printy(ex,"r>")


def animation():
    widgets = ['please wait: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(5):
        time.sleep(0.1)
        bar.update(i)
def main5():
    try:
        print("h/")
        i=False
        while (not i):
            link = str(input("input link: "))
            rk = keyboard.record(until='shift')
            if link.startswith("http"):
                print("append")

                biglist.append(link)
            else:
                i=True

                pass
        printy(biglist,"p>")
        return biglist

    except Exception as ex:
        printy(ex, "r>")



def downloadyt(bigie):
    global out_file
    try:
        print("downloadyoutube/")
        lenbigi=len(bigie)

        print(bigie)
        ii=0
        #print("Enter the destination (leave blank for current directory)")
        #destination = str(input(">> ")) or 'Q:\\programs\\quran\\mppfol\\'
        for i in range(lenbigi):
            ytt=bigie[i]
            #print(ytt)
            #printy(type(ytt),"r>")

            # extract only audio
            try:
                yt=YouTube(str(ytt))
                video = yt.streams.filter(only_audio=True).first()
                size= video.filesize
                sizekb = int(size) / 1024
                printy(sizekb)


            except:
                printy("problem at fettching","r")
            # check for destination to save file


            try:
                # download the file
                dest = 'Z:\\home\\songs'
                animation()
                out_file = video.download(output_path=dest)

                animation()
            except:
                printy("problem at download","r")


            # save the file
            try:
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

            except:
                printy("problem at saving,probably there", "r")
                toastnoti1()

            # result of success
            printy(yt.title + " ✔✔\n","p>")
            toastnoti()
            i=i+1
        printy("we are done","c")
        os.startfile(dest)

    except Exception as ex:
        printy(ex, "r")
def downloadytttt():
    try:
        print("download yt")
        yt = YouTube(
            str(input("Enter the URL of the video you want to download: \n>> ")))

        # extract only audio
        printy(yt,"r")
        printy(type(yt),"c")
        video = yt.streams.filter(only_audio=True).first()
        #print(video)
        pause3()

        # check for destination to save file
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'

        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

    except Exception as ex:
        printy(ex, "r>")


def main22():
    try:
        yt = YouTube(
            str(input("Enter the URL of the video you want to download: \n>> ")))

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # check for destination to save file
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
        dest='Q:\\programs\\quran\\mppfol\\'

        # download the file
        out_file = video.download(output_path=dest)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

    except Exception as ex:
        printy(ex, "r>")


def main222():
    try:
        print("h/")

    except Exception as ex:
        printy(ex, "r>")


if __name__ == '__main__':

    #main5()
    #animation()
    #print(bigie)
    take = int(input("how many: "))
    checkclipboard(take)
    #main5()
    downloadyt(copylist)
    #main22()