from pynput import keyboard
import threading
import time

FLAG = 1

def press(key):
    # if key == keyboard.Key.c:
        FLAG = 0



def on_release(key):
    # if key == keyboard.Key.c:
        FLAG = 1

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        while 1:
            print(FLAG)

if __name__ == '__main__':
    # thread = myThread(j
    with keyboard.Listener(on_press=press, on_release=on_release) as listener:
        listener.join()

