from email.policy import default
import pyautogui as py
import time

OFS = 4
i = 0

py.alert('runing script...')

while i < OFS:
    #selecionando HSE OFS
    py.click(x=645,y=342)
    time.sleep(1)
    py.click(x=708,y=406)
    time.sleep(1)
    py.click(x=651,y=871)
    time.sleep(3)

    #preenchendo o OFS
    py.click(x=600,y=342)
    time.sleep(1)
    py.click(x=554,y=494)
    time.sleep(2)
    py.click(x=591,y=458)
    time.sleep(1)
    py.click(x=535,y=681)
    time.sleep(2)
    py.click(x=492,y=573)
    time.sleep(1)
    py.click(x=500,y=680)
    time.sleep(2)
    py.click(x=535,y=683)
    time.sleep(1)
    py.click(x=529,y=738)
    time.sleep(2)
    py.click(x=598,y=796)
    time.sleep(1)
    py.click(x=519,y=838)
    time.sleep(2)

    #Preenchimento do comportamento e do comentario
    py.click(x=879, y=900)
    time.sleep(1)

    behavior = py.prompt(title='escolha um dos 3', text='1- óculos de proteção, 2- colete refletivo, 3- protetor auricular', default = '1')

    if behavior == '1':
        py.click(x=513, y=344)
        time.sleep(1)
        py.write('oculos')
        py.click(x=578, y=598)
        py.write('colaborador fez o uso correto dos oculos de protecao nas areas exigidas')
        time.sleep(2)
    elif behavior == '2':
        py.click(x=513, y=344)
        time.sleep(1)
        py.write('colete refletivo')
        py.click(x=578, y=598)
        py.write('colaborador fez o uso correto do colete refletivo nas areas de transito misto')
        time.sleep(2)
    elif behavior == '3':
        py.click(x=513, y=344)
        time.sleep(1)
        py.write('protetor auricular')
        py.click(x=578, y=598)
        py.write('colaborador fez o uso correto dos protetores auriculares nas areas exigidas')
        time.sleep(2)
    
    py.click(x=629, y=954)
    time.sleep(1)
    py.click(x=512, y=943)
    time.sleep(3)

    if i == OFS:
        break
    i+=1;

py.alert('Done!')