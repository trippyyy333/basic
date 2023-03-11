from printy import *
import keyboard
import pyperclip as pc
import time
import shutil
import random
import pyautogui
import os
link_list=[]
save_name = "grrg"
def maitr():
    try:
        file1 = open(r"C:\Users\mazen\Desktop\copier.txt")
        Liness = file1.readlines()
        count = -1


        for line in Liness:
            count += 1
            #print("Line{}: {}".format(count, line.strip()))
            link_list.append(line.strip())
        first_ele = link_list[0]
        last_ele = link_list[-1]
        printy(link_list,"y")
        printy(first_ele,"m")
        printy(last_ele,"m>")

        printy("jgv")
        sa=" len(link_list)-1"

        linesie = len(link_list)-1
        #printy(linesie)
        ds=str(linesie)+str(sa)
        printy(ds,"n")
        count2 = 0

        for count2 in range(linesie):
            tryter(count2)
        tryter(-1)







    except:
        printy("dasa")

def pause2():
    rk = keyboard.record(until='shift')


def tryter(count2):
    try:



        coopytext = str(link_list[count2])
        printy(count2)
        #print(coopytext)
        pc.copy(coopytext)
        print(coopytext)
        #a2 = pc.paste()
        pause2()
        #input("press")

        return count2
    except:
        print("pasteproblem")


def clearfile(name):
    filename = str(name) + str(".txt")
    file = open(filename, "r+")
    file.truncate(0)
    file.close()


def sstable(namer,caser):
    try:
        #API_KEY = "o.GVZrbiVF4S58asf6FsZaYsQoiquCkMxW"
        #txt = "this is a test warning before a game will begin"
        #drop = random.randrange(100)
        #drop_str = str(drop)
        #ima_name = str("\\_lister") + str(drop) + (".txt")

        #print(ima_name)

        directory = 'Z:\\projects\\lister\\New folder'
        number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])
        ima_name = str("\\_lister") + str(number_of_files) + (".txt")
        temp= number_of_files+1
        strtemp= str(temp)
         



        #pyautogui.screenshot(r"Z:\\projects\\lister\\New folder" + ima_name)
        tio = ('Z:\\projects\\lister\\New folder\\_lister') + strtemp + '.txt'
        namer = strtemp
        #print(ima_name, type(ima_name))
        #print(tio)
        printy(namer,"r")


        #to send the picture
        #pb = PushBullet(API_KEY)
        #with open(tio, "rb") as pic:
            #file_data = pb.upload_file(pic, tio)

        #push = pb.push_file(**file_data)

        #caser= caser+1
        dontdo(namer,caser,tio,strtemp,ima_name)


        return namer,tio

    except:
        printy("dontsay ")
def dontdo(namer,caser,tio,strtemp,ima_name):
    try:

        if caser ==1:
            #namer = "dacger"
            destination = "C:\\Users\\mazen\\Documents\\try\\getthis"
            mainfile ='C:Users//mazen//Desktop//copier.txt'
            d2 = "Z:\\projects\\lister\\New folder"
            d2 = "Z:\\projects\\lister\\New folder\\cp.txt"
            #sstable(namer)
            printy("fsf")
            printy(namer,"m")
            printy(tio,"w")
            fileinfolder = str(destination)+str(namer)
            printy(fileinfolder)
            try:

                shutil.copy2(mainfile, tio)
                printy("[y]%File copied successfully:@%  "+str(ima_name),predefined="c")
            except:
                printy("problem with printing","rU")



            #printy(caser)

        if caser == 2:
            printy("fseef")

    except:
        printy("Easyboy ","yU")




def main():
    while True:
        caser = 1
        fs="gs"

        maitr()
        sstable(fs,caser)
        #clearfile(name="copier")
        link_list.clear()
        time.sleep(1)




if __name__ == "__main__":
    main()