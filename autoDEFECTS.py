import pyautogui as py
import time

defects = int(py.prompt(title='QUANTIDADE DE REGISTROS', text='quantos registros você quer fazer?', default= '8'))
i = 0

py.alert('runing script...')

while i < defects:
    py.click(x=1160,y=92)
    time.sleep(1)
    py.click(x=289,y=321)
    py.write('Bandeja de nylon estava suja')

    py.click(x=296,y=567)
    py.click(x=282,y=655)
    py.click(x=278,y=623)
    py.click(x=278,y=657)
    py.click(x=253,y=666)
    py.click(x=266,y=713)
    py.click(x=266,y=715)
    py.click(x=265,y=756)
    py.click(x=264,y=766)
    py.click(x=280,y=808)

    time.sleep(1)
    py.click(x=1144,y=79)
    py.click(x=1202,y=95)
    time.sleep(5)

    if i == defects:
        break
    i+=1;

py.alert('Done!')