import pyautogui as py
import time

OFS = int(py.prompt(title='QUANTIDADE DE REGISTROS', text='quantos registros você quer fazer?', default= '8'))
i = 0

py.alert('RUNNING SCRIPT...')

while i < OFS:
    #selecionando o ofs de QA
    py.click(x=619,y=789)
    time.sleep(1)
    py.click(x=624,y=493)
    time.sleep(3)
    py.click(x=527,y=359)
    time.sleep(1)
    py.click(x=523,y=581)
    time.sleep(1)
    py.click(x=533,y=468)
    time.sleep(1)
    py.click(x=529,y=688)
    time.sleep(1)
    py.click(x=513,y=578)
    time.sleep(1)
    py.click(x=483,y=692)
    time.sleep(1)

    #selecionando o tipo de ofs
    ofstype = int(py.prompt(title='escolha um dos 2', text='1- Reforçado, 2- Em risco', default = '1'))

    if ofstype == 1:
        py.click(x=483,y=692)
        time.sleep(1)
        py.click(x=459,y=756)
        time.sleep(1)

        behavior = int(py.prompt(title='escolha um dos 3', text='1- Deixar o lixo aberto, 2- Touca,avental e luva nitrilica, 3- Portas de transição abertas', default = '1'))

        if behavior == 1:
            py.click(x=479,y=815)
            py.write('lixo')
            py.click(x=880,y=892)
            time.sleep(1)
            py.click(x=565,y=480)
            py.write('colaborador manteve a tampa dos lixos fechadas')
            py.click(x=589,y=636)
            time.sleep(1)
            py.click(x=594,y=965)
            time.sleep(2)
            py.click(x=508,y=962)
            time.sleep(1)

        elif behavior == 2:
            py.click(x=479,y=815)
            py.write('Touca')
            py.click(x=880,y=892)
            time.sleep(1)
            py.click(x=565,y=480)
            py.write('colaborador fez o uso correto da toca e avental na area de envase')
            py.click(x=589,y=636)
            time.sleep(1)
            py.click(x=594,y=965)
            time.sleep(2)
            py.click(x=508,y=962)
            time.sleep(1)

        elif behavior == 3:
            py.click(x=479,y=815)
            py.write('porta')
            py.click(x=880,y=892)
            time.sleep(1)
            py.click(x=565,y=480)
            py.write('colaborador manteve as portas de transição fechadas')
            py.click(x=589,y=636)
            time.sleep(1)
            py.click(x=594,y=965)
            time.sleep(2)
            py.click(x=508,y=962)
            time.sleep(1)
    
    elif ofstype == 2:
        
        py.click(x=483,y=692)
        time.sleep(1)
        py.click(x=464,y=799)
        time.sleep(1)

        behavior = int(py.prompt(title='escolha um dos 3', text='1- Deixar o lixo aberto, 2- Touca,avental e luva nitrilica, 3- Portas de transição abertas', default = '1'))

        if behavior == 1:
            py.click(x=479,y=815)
            py.write('lixo')
            py.click(x=880,y=892)
            time.sleep(1)
            py.click(x=565,y=480)
            py.write('colaborador não manteve a tampa dos lixos fechadas')
            py.click(x=589,y=636)
            time.sleep(1)
            py.click(x=594,y=965)
            time.sleep(2)
            py.click(x=508,y=962)
            time.sleep(1)
        
        elif behavior == 2: 
            py.click(x=479,y=815)
            py.write('Touca')
            py.click(x=880,y=892)
            time.sleep(1)
            py.click(x=565,y=480)
            py.write('colaborador não fez o uso correto da toca e avental na area de envase')
            py.click(x=589,y=636)
            time.sleep(1)
            py.click(x=594,y=965)
            time.sleep(2)
            py.click(x=508,y=962)
            time.sleep(1)

        elif behavior == 3:
            py.click(x=479,y=815)
            py.write('porta')
            py.click(x=880,y=892)
            time.sleep(1)
            py.click(x=565,y=480)
            py.write('colaborador não manteve as portas de transição fechadas')
            py.click(x=589,y=636)
            time.sleep(1)
            py.click(x=594,y=965)
            time.sleep(2)
            py.click(x=508,y=962)
            time.sleep(1)
    
    if i == OFS:
        break
    i+=1;

py.alert('DONE!')
