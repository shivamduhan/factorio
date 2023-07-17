import pyqrcode
import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import wx
from pyzbar import pyzbar
import pytesseract
import keyboard as key
import random

# from qrtools.qrtools import QR

import cv2

class Controller:
    def __init__(self):
        pass

    def moveLeft(self, t:int): #t is the time delay between keypressed and key released
        key.press('a')
        time.sleep(t)
        key.release('a')

    def moveRight(self, t:int):
        key.press('d')
        time.sleep(t)
        key.release('d')

    def moveUp(self, t:int):
        key.press('w')
        time.sleep(t)
        key.release('w')

    def moveDown(self, t:int):
        key.press('s')
        time.sleep(t)
        key.release('s')

    def moveLU(self, t:int):
        key.press('a')
        key.press('w')

        time.sleep(t)

        key.release('a')
        key.release('w')
    def moveLD(self, t:int):
        key.press('a')
        key.press('s')

        time.sleep(t)

        key.release('a')
        key.release('s')

    def moveRU(self, t:int):
        key.press('d')
        key.press('w')

        time.sleep(t)

        key.release('d')
        key.release('w')

    def moveRD(self, t:int):
        key.press('d')
        key.press('s')

        time.sleep(t)
        key.release('d')
        key.release('s')



class Game:
    def __init__(self):
        self.app = wx.App(False)
        self.width, self.height = wx.GetDisplaySize()
        self.mon = {'top': 50, 'left': 50, 'width': 200, 'height': 200}
        self.sct = mss()

    def startGame(self):
        while 1:
            # sct_img = self.sct.grab(self.mon)
            # img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX")
            # print(pytesseract.image_to_string(img))

            curRandom = random.randint(0,7)
            curTimeDelay = random.randint(0,3)
            if curRandom == 0:
                myController.moveLeft(curTimeDelay)
            elif curRandom == 1:
                myController.moveRight(curTimeDelay)
            elif curRandom == 2:
                myController.moveUp(curTimeDelay)
            elif curRandom == 3:
                myController.moveDown(curTimeDelay)
            elif curRandom == 4:
                myController.moveRU(curTimeDelay)
            elif curRandom == 5:
                myController.moveRD(curTimeDelay)
            elif curRandom == 6:
                myController.moveLU(curTimeDelay)
            elif curRandom == 7:
                myController.moveLD(curTimeDelay)



            # random play



if __name__ == "__main__":
    myController = Controller()
    myGame = Game()
    time.sleep(5)
    myGame.startGame()

