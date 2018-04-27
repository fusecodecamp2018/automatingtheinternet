#! python3
# mouseNow.py - Displays the mouse cursor's current position.
# NOTE: For some reason, this does not actually print the location of the mouse when running through PyCharm. Use
# command line.
import pyautogui

print('Press Ctrl-C to quit.')
# TODO: Get and print the mouse coordinates.
try:
    while 1:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print("\nDone")


