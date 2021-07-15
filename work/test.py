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

timestamps = pickle.load(open('data/czf/3-5' + '.timestamp', 'rb'))
print(timestamps)
      