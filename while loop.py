from gettext import install


pip install pynput
from pynput keyboard import Key, Controller
keyboard = Controller()
key = "a"
keyboard.press(key)
keyboard.release(key)