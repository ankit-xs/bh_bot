#goal - Make bh bot which scans the img and locate actions buuton and does a basic movement and spam moves
#end_goal - Afk-able (Must earn XP!!)
#https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
#https://blog.seethis.link/scan-rate-estimator/

import time
import pyautogui as p
from direct_input import PressKey, ReleaseKey, W, A, S, D, J, K, L, H, SPACE

#Functions

def key_S():
	PressKey(S)
	time.sleep(0.25)
	ReleaseKey(S)

def key_J():
	PressKey(J)

def key_K():
	PressKey(K)
	time.sleep(0.25)
	ReleaseKey(K)

def key_L():
	PressKey(K)
	time.sleep(0.25)
	ReleaseKey(K)

def key_H():
	PressKey(H)
	time.sleep(0.25)
	ReleaseKey(H)

def key_SPACE():
	PressKey(SPACE)
	time.sleep(0.25)
	ReleaseKey(SPACE)

def dlight():
	PressKey(S)
	PressKey(J)

p.click(993,509)
time.sleep(5)

dlight()
time.sleep(1)
key_SPACE()
time.sleep(1)
key_J()

# key_SPACE()

# #dlight space light

# key_J()
# key_S()
# key_SPACE()
# key_J()