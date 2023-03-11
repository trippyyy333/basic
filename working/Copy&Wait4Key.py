import pyperclip as pc
from printy import printy
coplist=[]
start_clipboard_temp=int (0)
def copy_clipboard():
    try:
        asww = pc.waitForPaste()
        coplist.append(asww)
        print(coplist)

        check_clipboard()




    except:
        printy("problem@ check_clipboard","r")

def check_clipboard():
    try:

        copylist_len = len(coplist)
        if(copylist_len==start_clipboard_temp):
            print("youdidntcopy")
        else:
            #print("you did copy")
            pass


    except:
        printy("problem@ check_clipboard","r")






while(True):
    copy_clipboard()