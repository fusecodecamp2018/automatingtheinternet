import pyautogui
import time

# Wait for 5 seconds. During this time, open up the painting program you want to use.
time.sleep(5)

# click to put drawing program in focus
pyautogui.click()

# this value will be used to determine the starting size
distance = 200

# let's draw!
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)  # move right

