import pyautogui as py
import time

BOS = 8
i = 0

py.alert('runing script...')

while i < BOS:
    py.click(x=640,y=719)
    time.sleep(1)
    py.click(x=616,y=668)
    time.sleep(1)
    py.click(x=557,y=412)
    time.sleep(1)
    py.click(x=520,y=603)
    time.sleep(1)
    py.click(x=554,y=532)
    time.sleep(1)
    py.click(x=534,y=758)
    time.sleep(1)
    py.click(x=510,y=662)
    time.sleep(1)
    py.click(x=483,y=726)
    time.sleep(1)
    py.click(x=594,y=967)
    time.sleep(1)
    py.click(x=645,y=342)
    time.sleep(2)

    py.click(x=478,y=726)
    time.sleep(1)
    py.click(x=478,y=726)
    time.sleep(1)
    py.click(x=478,y=726)
    time.sleep(2)

    py.click(x=638,y=947)
    time.sleep(1)
    py.click(x=518,y=199)
    time.sleep(1)

    if i == BOS:
        break
    i+=1;

py.alert('Done!')