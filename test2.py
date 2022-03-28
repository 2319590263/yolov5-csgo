import cv2
import numpy as np
import pyautogui

if __name__ == '__main__':
    img = pyautogui.screenshot(region=[0, 0, 1920, 700])  # x,y,w,h
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()