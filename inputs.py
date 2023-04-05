import keyboard
import pynput as input

mouseListener = input.mouse.Listener(supress = True)
keyboardListener = input.keyboard.Listener(supress = True)

def stopMouse():
    mouseListener.start()

def startMouse():
    mouseListener.stop()

def stopKeyboard():
    keyboardListener.start()

def startKeyboard():
    keyboardListener.stop()