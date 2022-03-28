import pyautogui
from pymouse import PyMouse
import pydirectinput

def calculate_distance(xyxyclist):
    if len(xyxyclist)==0:
        return
    lately_c_distance = float('inf')
    num = None
    for step, (xyxycdict) in enumerate(xyxyclist):
        x1 = xyxycdict["x1"]
        y1 = xyxycdict["y1"]
        x2 = xyxycdict["x2"]
        y2 = xyxycdict["y2"]
        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)
        x_frame_core = x1 + (x_distance / 2)
        y_frame_core = y1 + (y_distance / 2)
        x_core, y_core = 960,540
        x_distance = abs(x_frame_core - x_core)
        y_distance = abs(y_frame_core - y_core)
        c_distance = (x_distance**2 + y_distance**2)**0.5
        if lately_c_distance > c_distance:
            lately_c_distance = c_distance
            num = step
    print(xyxyclist[num])
    x1 = xyxyclist[num]["x1"]
    y1 = xyxyclist[num]["y1"]
    x2 = xyxyclist[num]["x2"]
    y2 = xyxyclist[num]["y2"]
    x_distance = abs(x1 - x2)
    y_distance = abs(y1 - y2)
    x_frame_core = x1 + (x_distance / 2)
    y_frame_core = y1 + (y_distance / 2)
    # pyautogui.moveTo(x_frame_core, y_frame_core, duration=1)
    # win32api.SetCursorPos((x_frame_core, y_frame_core))
    # print(int(x_frame_core),int(y_frame_core))
    # PyMouse().move(int(x_frame_core),int(y_frame_core))
    pydirectinput.click(int(x_frame_core), int(y_frame_core))
    return x_frame_core,y_frame_core
