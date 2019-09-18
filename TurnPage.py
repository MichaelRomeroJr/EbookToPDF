# -*- coding: utf-8 -*-
from PyUserInput import pymouse
from pynput.mouse import Listener
from pynput.mouse import Button, Controller
from time import sleep

def Click(x,y):
    mouse = Controller()
    mouse.position = (x, y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    return

def listen_to_mouse():
    from pynput import mouse
    global xposition
    global yposition
    
    def on_click(x, y, button, pressed):
        global xposition
        global yposition        
        if pressed:
            xposition, yposition = x,y
            
        if not pressed: # Stop listener
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join() 
    
    return xposition, yposition

def GetTurnPageCoordinates():
    """Once the user clicks the 'next' page on their kindle
        grab coordinates of mouse cursor to auto click next pages"""
    x,y = listen_to_mouse()
    
    sleep(5) #Wait for user to go back to cover page
    
    return x,y 