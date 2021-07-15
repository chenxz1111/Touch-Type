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

lv = 0
lan = 0
lan1 = 0
lan2 = 0

class Replay():
    def __init__(self):
        self.init()

    def init(self):
        global lv
        # grc gyz hxz hyq hyw jy lc lhh lyq lzc plh pzh swn syt xcn
        global lan
        global lan1
        global lan2
        self.timestamps = pickle.load(open( 'data/lzc/2' +  '.timestamp', 'rb'))
        self.frames = compress_pickle.load( 'data/lzc/2' +  '_labeled.gz')
        self.frames2 = compress_pickle.load('data/lzc/2'+ '_checked.gz')
        self.frame_id = 0
        self.frame_id2 = 0
        self.history = History()
        [self.scalar, self.clf] = pickle.load(open('model/tap.model', 'rb'))
        while self.frame_id + 1 < len(self.frames):
            frame = self.frames[self.frame_id]
            self.history.updateFrame(frame)
            self.key_contacts = self.history.getKeyContact(frame)
            for contact in self.key_contacts:
                feature = self.scalar.transform([contact.feature])[0]
                pred = self.clf.predict([feature])[0]
                if pred != contact.label:
                    lv += 1
            self.frame_id += 1
        while self.frame_id2 + 1 < len(self.frames2):
            frame2 = self.frames2[self.frame_id2]
            self.history.updateFrame(frame2)
            self.key_contacts = self.history.getKeyContact(frame2)
            for contact in self.key_contacts:
                feature = self.scalar.transform([contact.feature])[0]
                pred = self.clf.predict([feature])[0]
                if pred != contact.label:
                    lan += 1
                    if contact.label == 0:
                        lan1 += 1
                    if contact.label == 1:
                        lan2 += 1
            self.frame_id2 += 1

if __name__ == "__main__":
    replay = Replay()
    print(lv - lan,lan,lan1,lan2)
