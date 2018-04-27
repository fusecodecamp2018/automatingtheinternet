# this tells python we want to use the pyautogui library
import pyautogui

# **********************************************************************************************************************
# These are some global settings that pyautogui uses
# **********************************************************************************************************************

# pause for 1 second after every call to pyautogui
pyautogui.PAUSE = 1

# add in a failsafe - you can abort the program by moving the mouse to the upper left corner of the screen
pyautogui.FAILSAFE = True

# **********************************************************************************************************************

# get the width and height of the screen from pyautogui
width, height = pyautogui.size()

# **********************************************************************************************************************
# Let's try to move the mouse around
# **********************************************************************************************************************

# The moveTo function is used to move the mouse to a specific version on the screen.
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# The moveRel function is used to move the mouse to a position that is relative to the current position.
for j in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
