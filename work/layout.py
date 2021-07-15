#!/usr/bin/python3.7
import numpy
from pynput.keyboard import Key, Controller
import time

class Layout():
    def __init__(self):
        lines = open('model/layout.txt', 'r').readlines()

        tags0 = lines[0].split()
        H, W = float(tags0[0]), float(tags0[1])

        self.mapping = []
        self.del_time = 0
        self.del_state = False
        self.start_time = 0
        self.end_time = 0
        self.back_times = 0

        for line in lines[1:]:
            tags = line.split()
            px0,py, length, width, letters = float(tags[0]), float(tags[1]), float(tags[2]), float(tags[3]), tags[4]
            px = px0
            for ch in letters:
                self.mapping.append((px/W, py/H, length/W, width/H, ch))
                px += length
        
        for i in range(len(self.mapping)):
            x, y, l, w, ch = self.mapping[i]

            if ch in 'qwertyuiopasdfghjklzxcvbnm`1234567890-=[];,.':
                key = ch
            if ch == 'B':
                key = Key.backspace
            if ch == 'S':
                key = Key.shift
            if ch == 'E':
                key = Key.enter
            if ch == '_':
                key = Key.space
            if ch == 'T':
                key = Key.tab
            if ch == 'C':
                key = Key.ctrl
            if ch == 'A':
                key = Key.alt
            if ch == 'M':
                key = Key.cmd
            if ch == 'U':
                key = Key.up
            if ch == 'D':
                key = Key.down
            if ch == 'L':
                key = Key.left
            if ch == 'R':
                key = Key.right
            if ch == '<':
                key = Key.esc
            
            self.mapping[i] = (x, y, l, w, key)

    def decode(self, x0, y0):
        key = None
        num = []
        for ch in '1234567890':
            tmp = ch
            num.append(tmp)

        for (x,y,l,w,k) in self.mapping:
            if (x < x0 and x0 < x + l) and (y < y0 and y0 < y + w):
                key = k
                if self.start_time == 0:
                    self.start_time = time.perf_counter()
                    #print(self.start_time)
                else:
                    self.end_time = time.perf_counter()
                    #print(self.end_time)
                if key == Key.backspace:
                    self.back_times += 1
                    if self.del_state == True:
                        self.del_time += 1
                if key in num:
                    self.del_state = True
                elif key == Key.space:
                    self.del_state = True
                elif key != Key.backspace:
                    self.del_state = False
                break

        return key
