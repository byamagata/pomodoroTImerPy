#pomodoro timer
import time
import datetime as dt
import io
from imagesearch import *
import pyautogui
from playsound import playsound
import pywin32_system32
import win32gui, win32com
from os import system


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def work(passtime):
    workTimer = dt.timedelta(minutes=passtime)
    doneTimer = dt.timedelta(minutes = 0)
    while workTimer != doneTimer:
        if workTimer.seconds == 0:
          break
        print(workTimer, end='\r')
        time.sleep(1)
        second = dt.timedelta(seconds = -1)
        workTimer = workTimer + second    

def rest(passtime):
    restTimer = dt.timedelta(minutes=passtime)
    while True:
        if restTimer.seconds == 0:
         break
        print(restTimer, end='\r')
        time.sleep(1)
        second = dt.timedelta(seconds = -1)
        restTimer = restTimer + second 


def openSpotify():
    pos = imagesearch('spotify_open.png')
    if pos[0] != -1: #spotify is already open
        pos = imagesearch('spotify_play_button.png')
        if pos[0] != -1: #spotify is not playing click the play buttons
            pyautogui.moveTo(pos[0]+15, pos[1]+15)
            pyautogui.click()
    else: #spotify is not open
        pos = imagesearch('spotify_min.png')
        if pos[0] != -1: #shouldnt be, it was already closed
            pyautogui.moveTo(pos[0]+15, pos[1]+15)
            pyautogui.click()
            pos = imagesearch('spotify_play_button.png')
            if pos[0] != -1: #spotify is not playing click the play buttons
                pyautogui.moveTo(pos[0]+15, pos[1]+15)
                pyautogui.click()
    #closeAllWindows()

def closeAllWindows():
    pyautogui.hotkey('win', 'd')

def hideWindow():
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "pomodoro timer" in i[1].lower():
            win32gui.ShowWindow(i[0], 0)
        

def showWindow():
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "pomodoro timer" in i[1].lower():
            win32gui.ShowWindow(i[0], 1)


def main():
    #set window name
    system("title "+"Pomodoro Timer")

    #get input for how long for work and how long for breaks
    print('Pomodoro Work Helper\n')
    while True:
        workInput = input('>Input work time: ')
        try:
            workTime = int(workInput)
            break
        except:
            print('\n\n was not a number, please try again\n\n')

    while True:
        breakInput = input('>Input break time: ')
        try:
            breakTime = int(breakInput)
            break
        except:
            print('\n\n was not a number, please try again\n\n')

    answer = 'y'
    restanswer = 'y'
    #start the timer
    while answer == 'y':
        openSpotify()
        hideWindow()
        work(workTime)
        showWindow()
        # when the timer finishes, wait for a second and play the sound
        playsound('chimesound.wav')
        answer = input('>Would you like to continue working?(y/n) ')
        if answer == 'y':
            continue
        else:
            while restanswer == 'y':
                rest(breakTime)
                playsound('chimesound.wav')
                answer = 'y'
                restanswer = input('>Do you need more rest time?(y/n) ')
                if restanswer != 'y':
                    break

if __name__ == "__main__":
    main()







#TODO:
#add functionality to ask if spotify is open or in the taskbar
#add functionality to hide or open window at certain times
# bugfix: step through openspotify to see if we can actually open the window
# add to github