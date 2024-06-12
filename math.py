from pynput import mouse
import keyboard
import os

osType = -1
if os.name == "nt":
    osType = 0
    print("windows detected")
elif os.name == "posix":
    osType = 1
    print("linux detected")
else:
    print("unknown os, terminating")

import tkinter as tk
import pygetwindow as gw

title = "GraphwarTool"

if osType == 0:
    print("1")
    #import win32gui
elif osType == 1:
    print("2")
    #import xlib


wx = 0
wy = 0
def callback():
    windows = gw.getWindowsWithTitle('Graphwar')
    if not windows:
        print("no window called graphwar found")
    else:
        for index, window in enumerate(windows):
            title = window.title

            window = gw.getWindowsWithTitle(title)[index]

            # Get the window rectangle
            rect = window.left, window.top, window.right, window.bottom

            wx = rect[0]
            wy = rect[1]
            w = rect[2] - wx
            h = rect[3] - wy
            print(f"Window {title}:\n")
            print(f"\tLocation: ({wx}, {wy})\n")
            print(f"\t    Size: ({w}, {h})\n")

def main():
    callback()

if __name__ == '__main__':
    main()

currentDir = 1  

def newDir(loc, dir):
    
    global currentDir
    l = f'(x{-loc:+.2f}+abs(x{-loc:+.2f}))*({(dir-currentDir)/2:.2f})'
    '(x-1+abs(x-1))'
    currentDir = dir
    return l
    
pixelToUnit = 50/851

prevX = 0
prevY = 0

def findSteepness(prevX, prevY, x, y):
    return (prevY - y)/(x-prevX)



formel = ''


def XtoUnit(x):
    return (x - wx - 25) * pixelToUnit - 25

clickCount = 0
def onClick(x, y):
    
    global prevX, prevY, formel, clickCount, currentDir
    print(f'X to unit: {XtoUnit(x):.3f}, normal x {x}')

    if(clickCount > 0):
        steepness = findSteepness(prevX, prevY, x, y)
        print(f'Steepness: {steepness:.2f}')
        
        if(clickCount > 1):
            formel += "+" + newDir(XtoUnit(prevX), steepness)
        else:
            formel += f'{steepness:.2f}x'
            currentDir = steepness
    
    prevX = x
    prevY = y
    clickCount += 1
    
def on_click(x, y, button, pressed):
    
    if pressed:
        onClick(x, y)


    
import pyperclip

def on_press(key):
    global formel, clickCount
    if key.name == "enter":
        print(formel)
        pyperclip.copy(formel)
        formel = ""
        clickCount = 0

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.on_press(on_press)

mouse_listener.start()

    
mouse_listener.join()
# formel = f'(x+abs(x))({currentDir})'

# formel += "+" + newDir(1, 0)

# for i in range(10):
#     formel += '+' + newDir(i + 5, 1)
#     formel += '+' + newDir(i + 0.5 + 5, -1)


print(formel)
    
    

