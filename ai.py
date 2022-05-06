# first open terminal and run this command 
# python -m pip install pyautogui

# lets start 
# first we are going to import Pyautogui module
import pyautogui as pg

# let store message in any variable 
li ="Hi i am faizan  "

# let call function click from pyautogui
# this function will click right button of mouse 
# so before running this 
# you should place your mouse courser on app which you want to run so it click on right place

pg.click()
# Now i am going to call 2nd function which will write text
i = 1
for i in range(50):
    pg.write(li)

    pg.press('enter') 
    pg.sleep(3)

# finally function pg.press which take keyboard key name as input
# it will presss enter 

