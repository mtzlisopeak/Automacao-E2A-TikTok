import pyautogui as bot
from time import sleep
import os

validas = 0
invalidas = 0

class Robot:
    def init(self):
        pass

    def clicar(self, img, confidence=0.9, grayscale=True):
        tempo = 0
        while tempo < 10:
            try:
                localizacao_img = bot.locateCenterOnScreen(img, confidence=confidence, grayscale=grayscale)
                bot.click(localizacao_img, duration=0.5)
                return
            except:
                sleep(1)
                tempo += 1

    def confirmar_acao(self):
        global validas
        bot.hotkey('ctrl', 'w')
        robo.clicar('img/confirmar.png')
        validas += 1

    def invalidar_acao(self):
        global invalidas
        bot.hotkey('ctrl', 'w')
        robo.clicar('img/pular.png')
        invalidas += 1

robo = Robot()

os.system('cls')

while True:
    robo.clicar('img/acessar.png')
    try:
        robo.clicar('img/seguir.png')
        sleep(2)
    except:
        pass
    bot.hotkey('ctrl', 'r')
    sleep(5)
    try:
        bot.locateCenterOnScreen('img/msg.png', confidence=0.9, grayscale=True)
        robo.confirmar_acao()
    except:
        robo.invalidar_acao()
    os.system('cls')
    print(f'Validas: {validas}\nInvalidas: {invalidas}')
    sleep(15)
