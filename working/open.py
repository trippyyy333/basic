from printy import *
import pyfiglet
import keyboard
import pyautogui
import mouse
import time
import webbrowser
import _pyinstaller_hooks_contrib
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

#import pysimplegui-exemakerpip install pysimplegui-exemaker




"""
discreet tut:   https://courses.nu.edu.eg/course/view.php?id=5033
discreet lect:  

calclus 2 :https://courses.nu.edu.eg/course/view.php?id=5316

prob: https://courses.nu.edu.eg/course/view.php?id=5333
csci311:  https://courses.nu.edu.eg/course/view.php?id=4744

csci217: https://courses.nu.edu.eg/course/view.php?id=4711
"""

def WhatCourse():
    result = pyfiglet.figlet_format("M O O D L E")
    #res2 = pyfiglet.print_figlet("mad", font=)
    res2 = pyfiglet.print_figlet("m a d", font="doh", colors="RED")
    resr = pyfiglet.figlet_format()
    printy(result, "c")
    printy(result, "c>")
    printy(result, "<c")
    printy(result, "r")
    printy(result, "")


def opencourse(course,type):
    try:
        if type ==1:


            #printy("ht")


            pyautogui.hotkey('win','r')
            pyautogui.write(course)
            pyautogui.hotkey('enter')

        if type==2:
            ba=webbrowser.open(course)

            #log.click()


    except:
        printy("Course Problem","rBU")


def switch(case):

    try:
        printy("b")
        if case ==1:
            #you choose calclus 2

            course_link = "https://courses.nu.edu.eg/course/view.php?id=5316"
        elif case == 2:
            # you choose Probability
            course_link = "https://courses.nu.edu.eg/course/view.php?id=5333"
            return course_link

        elif case == 3:
            # you choose discreet
            course_link = "https://courses.nu.edu.eg/course/view.php?id=5033"
        elif case == 4:
            # you choose CSCI311
            course_link = "https://courses.nu.edu.eg/course/view.php?id=4744"
        elif case == 5:
            # you choose CSCI217
            course_link = "https://courses.nu.edu.eg/course/view.php?id=5333"
        elif case == 0:
            # you choose main
            course_link = "https://courses.nu.edu.eg/"


        #printy(course_link)
        return course_link

    except:
        printy("switch prob","rBU")

def meeti(course_link):

    try:
        web = webdriver.Firefox("Z:\projects\PROG\geckodriver.exe")
        web.maximize_window()

        web.get(course_link)
        course = "https://courses.nu.edu.eg/course/view.php?id=3465"
        a = "https://www.youtube.com/watch?v=_RHIECWv728&ab_channel=Wegz%D9%88%D9%8A%D8%AC%D8%B2"
        # web=webdriver.Chrome()

        time.sleep(1)
        usernam = web.find_element_by_id("username")
        passw = web.find_element_by_id("password")
        subm = web.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/section/div[2]/div[2]/div/div/div/div/div/div[1]/form/button')

        name = "maz.sarwat"
        passwor = "%#3er@Wqe1"

        usernam.send_keys(name)
        passw.send_keys(passwor)
        subm.click()
        #time.sleep(100)

    except:
        printy("meeting wrong","rU")



def portal(course_link):

    try:
        web = webdriver.Chrome("Z:\projects\PROG\chromedriver.exe")
        name = "maz.sarwat"
        passwor = "%#3er@Wqe1"
        course = "https://register.nu.edu.eg/PowerCampusSelfService/"
        a = "https://www.youtube.com/watch?v=_RHIECWv728&ab_channel=Wegz%D9%88%D9%8A%D8%AC%D8%B2"
        # web=webdriver.Chrome()
        web.maximize_window()

        web.get(course_link)
        time.sleep(1)
        usernam = web.find_element_by_id('txtUsername')
        next = web.find_element_by_xpath('/html/body/div/div[1]/main/div[1]/div/div/div/div/div/div/div/div[2]/div/button')
        usernam.send_keys(name)
        next.click()
        time.sleep(1)

        passw = web.find_element_by_xpath('/html/body/div/div[1]/main/div[1]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/input')
        passw.send_keys(passwor)
        signin_button = web.find_element_by_xpath('/html/body/div/div[1]/main/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/button')
        signin_button.click()
        time.sleep(100)
        action = ActionChains(web)

        action.key_down(Keys.CONTROL).send_keys('Space').key_up(Keys.CONTROL).perform()




    except:
        printy("portal wrong","rU")



def start():
    #course_link = "https://courses.nu.edu.eg/"
    #course_link = ""

    res2r = pyfiglet.figlet_format("M O O D L E  -  COURSES", font="bubble")
    printy(res2r,"c")

    printy("|----------------------------------------------------------------------------------------------------------------|","c>")
    #print("| TIME NOW IS : ",  "                                                                                              |")
    #print('| TIME TO START THE MEETING: ',  "                                                                                 |")
    #print("| TIME TO END THE MEETING : ",  "                                                                                  |")
    #print("| TIME TO Half THE MEETING : ","                                                                                  |")
    print("|                                                                                                                |")
    print("|                                                                                                                |")
    printy(
        "|choose your course from : CalCLus2(1), ProbAbilty(2), Discreet(3),  CSCI311(4), CSCI217(5) , Mail(6)            |","c>")
    printy("|________________________________________________________________________________________________________________|","c")

    course_search = inputy("Which Course How many  do you want? : " , predefined="cUB", type="int", condition="+")
    #printy(course_search)
    #print(type(course_search))
    #switch(course_search)
    case = course_search

    if case == 1:
        # you choose calclus 2
        printy("you choose calclus 2","y")
        #homework
        course_link = "https://courses.nu.edu.eg/course/view.php?id=5316&section=11"
        #course_link = "https://courses.nu.edu.eg/course/view.php?id=5316"
    elif case == 2:
        # you choose Probability
        printy("you choose Probability", "y")
        course_link = "https://courses.nu.edu.eg/course/view.php?id=5333"
        #return course_link

    elif case == 3:
        # you choose discreet
        printy("you choose discreet", "y")
        course_link = "https://courses.nu.edu.eg/course/view.php?id=5033"
    elif case == 4:
        # you choose CSCI311
        printy("you choose CSCI311", "y")
        course_link = "https://courses.nu.edu.eg/course/view.php?id=4744"
    elif case == 5:
        # you choose CSCI217
        printy("you choose CSCI217", "y")
        course_link = "https://courses.nu.edu.eg/course/view.php?id=4711"
    elif case == 6:
        # you choose CSCI217
        printy("you choose Mail", "y")
        course_link = "https://outlook.office.com/mail/"
    elif case == 7:
        # you choose CSCI217 teams
        printy("you choose csci217 teams", "y")

        course_link = "https://courses.nu.edu.eg/mod/url/view.php?id=189819&redirect=1"
        meeti(course_link)
        return
    elif case == 8:
        # you choose CSCI217 teams
        printy("you choose power campus", "y")

        course_link = "https://register.nu.edu.eg/PowerCampusSelfService/Registration/Schedule"
        portal(course_link)
        return

    elif case == 0:

        # you choose main
        printy("you choose Main", "y")
        course_link = "https://courses.nu.edu.eg/"


    printy(course_link,"r")
    opencourse(course_link,type=2)






def main():

    #printy("hello","n")

    while True:
    #res2r = pyfiglet.figlet_format("M O O D L E  -  COURSES", font="bubble")
        start()

if __name__ == "__main__":

    main()
