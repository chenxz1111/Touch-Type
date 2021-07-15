import sys
import cv2
import time
import numpy as np
import pickle
from sklearn import svm
from board import Board
import random
import threading
from my_keyboard import MyKeyboard
from frame_data import FrameData
from data_manager import DataManager
import compress_pickle
from train import History
import docx
import os
from shutil import copyfile
import xlrd
import openpyxl as op

class Replay():

    def __init__(self, file_name):
        self.file_name = file_name
        self.init()

    def _run(self):
        self.is_running = True
        while self.is_running:
            if self.auto_play:
                self.incFrame()

    def init(self):
        self.timestamps = pickle.load(open('data/' + self.file_name + '.timestamp', 'rb'))
        self.frames = compress_pickle.load('data/' + self.file_name + '.gz')
        self.frame_id = 0
        self.auto_play = True
        self.history = History()
        self.num = 0
        self.time = 0 
        self.compt = False
        self.start = 0
        self.end = 0 
        [self.scalar, self.clf] = pickle.load(open('model/tap.model', 'rb'))

    def incFrame(self):
        if self.frame_id + 1 < len(self.frames):
            frame = self.frames[self.frame_id]
            self.history.updateFrame(frame)
            key_contacts = self.history.getKeyContact(frame)
            for contact in key_contacts:
                if(iswords(contact.x, contact.y) == True):
                    timestamp = self.frames[self.frame_id].timestamp
                    if(self.compt == False):
                        self.start = timestamp
                        self.num += 1
                        self.compt = True
                    else:
                        self.end = timestamp
                        self.num += 1
                else:
                    if(self.compt == True):
                        if(self.end - self.start > 0):
                            self.time += self.end - self.start
                        self.compt = False
                        self.num -= 1
            self.frame_id += 1
        else:
            self.is_running = False
    
def iswords(x, y):
    if(x > 3.0/23.7 and x < (3.0 + 17.8)/ 23.7 and y > 4.35/13.7 and y < (4.35 + 1.65) / 13.7):
        return True
    if(x > 3.45/23.7 and x < (3.45 + 9 * 1.77)/ 23.7 and y > 6.0/13.7 and y < (6.0 + 1.7) / 13.7):
        return True
    if(x > 4.3/23.7 and x < (4.3 + 7 * 1.78)/ 23.7 and y > 7.7/13.7 and y < (7.7 + 1.65) / 13.7):
        return True
    return False


if __name__ == "__main__":
    
    keyboard = MyKeyboard()
    file_name = DataManager(is_write=False).getFileName()
    replay = Replay(file_name)
    replay._run()
    print(replay.num / replay.time * 60)
    print('time:',replay.time)
    print('num', replay.num)
    work_book = xlrd.open_workbook('xdata.xlsx')
    wb = op.load_workbook("xdata.xlsx")
    sh=wb["Sheet1"]
    n = int(file_name[-3])
    m = int(file_name[-1])
    print(n, m)
    sh.cell(10 + (n - 1) * 75+(m -1) * 15,8,replay.num / replay.time * 60)
    wb.save("xdata.xlsx")