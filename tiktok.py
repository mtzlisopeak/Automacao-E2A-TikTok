import pyautogui as gui from time import sleep import os

valid_actions = 0 invalid_actions = 0

class Robot: def init(self): pass

def click_image(self, image_path, confidence=0.9, grayscale=True):
    elapsed = 0
    while elapsed < 10:
        try:
            location = gui.locateCenterOnScreen(
                image_path,
                confidence=confidence,
                grayscale=grayscale
            )
            gui.click(location, duration=0.5)
            return
        except:
            sleep(1)
            elapsed += 1

def confirm_action(self):
    global valid_actions
    gui.hotkey('ctrl', 'w')
    robot.click_image('img/confirmar.png')  # keep your image names or rename accordingly
    valid_actions += 1

def skip_action(self):
    global invalid_actions
    gui.hotkey('ctrl', 'w')
    robot.click_image('img/pular.png')  # keep your image names or rename accordingly
    invalid_actions += 1

robot = Robot()

os.system('cls')

while True: robot.click_image('img/acessar.png') try: robot.click_image('img/seguir.png') sleep(2) except: pass

gui.hotkey('ctrl', 'r')
sleep(5)

try:
    gui.locateCenterOnScreen('img/msg.png', confidence=0.9, grayscale=True)
    robot.confirm_action()
except:
    robot.skip_action()

os.system('cls')
print(f'Valid actions: {valid_actions}\nInvalid actions: {invalid_actions}')
sleep(15)
