import pyautogui
import time

# Sleep for 5 seconds. During this time, open up your text editor of choice
time.sleep(5)

# Click somewhere to bring focus
pyautogui.click(550, 150)

# Type away!
pyautogui.typewrite('Hello world!')

# Use keyboard shortcuts at all? Give them a try!
pyautogui.hotkey('alt', 'shift', 'ctrl', 'right')
pyautogui.hotkey('alt', 'shift', 'ctrl', 'right')

time.sleep(2)

pyautogui.hotkey('alt', 'shift', 'ctrl', 'left')
pyautogui.hotkey('alt', 'shift', 'ctrl', 'left')