import pyautogui as py
import time

i = 0
sheet = int(py.prompt(title='QUANTAS LINHAS DE MATERIAL PARA CONSUMIR?', text='DIGITE QUANTAS LINHAS DE MATERIAL TEM PARA CONSUMIR'))

py.alert('prepare your machine')
time.sleep(3)
py.alert('runing script!')

while i < sheet:
    py.click(x=211, y=275)
    time.sleep(1)
    py.hotkey('ctrl', 'c')
    time.sleep(1)
    py.hotkey('alt', 'tab')
    time.sleep(1)
    py.write('lv90')
    time.sleep(2)
    
    py.press(['enter','enter','enter','enter','enter','enter'])
    time.sleep(2)

    py.rightClick(x=418, y=148)
    time.sleep(1)
    py.press(['enter','enter'])
    time.sleep(1)
    py.hotkey('alt', 'tab')
    time.sleep(1)
    py.rightClick(x=14,y=275)
    time.sleep(2)
    py.click(x=75,y=439)
    time.sleep(1)

    if i == sheet:
        break
    i+=1;
        

py.alert('done!')