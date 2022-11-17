import pyautogui as py
import time

BOS = int(py.prompt(title='QUANTIDADE DE REGISTROS', text='quantos registros você quer fazer?', default= '8'))
i = 0

py.alert('runing script...')

while i < BOS:
    py.click(x=645,y=342)
    time.sleep(1)
    py.click(x=520,y=491)
    time.sleep(5)
    py.click(x=641,y=427)
    time.sleep(1)
    py.click(x=521,y=597)
    time.sleep(1)
    py.click(x=526,y=520)
    time.sleep(1)
    py.click(x=544,y=749)
    time.sleep(1)
    py.click(x=519,y=627)
    time.sleep(1)
    py.click(x=510,y=734)
    time.sleep(1)
    py.click(x=534,y=739)
    time.sleep(1)
    py.click(x=528,y=793)
    time.sleep(1)
    py.click(x=630,y=941)
    time.sleep(1)
    py.click(x=630,y=941)

    py.click(x=467,y=713)
    time.sleep(1) 
    py.click(x=467,y=713)
    time.sleep(1)
    py.click(x=467,y=713)
    time.sleep(1)

    py.click(x=594,y=490)
    py.write('Manter habitos seguros no ambiente de trabalho')
    time.sleep(1)

    py.click(x=521,y=852)
    time.sleep(1)
    py.click(x=606,y=852)
    time.sleep(1)
    py.click(x=520,y=198)
    time.sleep(2)

    if i == BOS:
        break
    i += 1;

py.alert('Done!')