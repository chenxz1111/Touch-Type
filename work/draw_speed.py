import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_preprocessing():
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    g_user = ["lzp", "xt", "xjj", "zzy", "lry", "lmm", "lq", "zwx"]
    lines = [line.strip() for line in open('./data/data_wpm.txt').readlines()]
    data = []

    i = 0
    while i < len(lines):
        name = lines[i]
        i += 1
        for j in range(5):
            day = j + 1
            is_P = int(name in p_user)
            wpm = float(lines[i + 1])
            cer = float(lines[i + 2])
            uer = float(lines[i + 3])
            i += 4
            for j in range(8):
                if name == p_user[j]:
                    subject = j + 1
                if name == g_user[j]:
                    subject = j + 9
            data.append([name, day, is_P, wpm, cer, uer])
    
    return data

def drawing(data):
    xs = []
    ys = []
    stds = []

    for day in range(1, 6):
        li = []
        for model in range(2):
            for i in range(len(data)):
                if data[i][1] == day and data[i][2] == model:
                    li.append(data[i][3])
        xs.append(day)
        ys.append(np.mean(li))
        stds.append(np.std(li))
    
    fig=plt.figure(figsize = (8, 5))
    colors = ['#37ACCB', '#FB9100', '#B0C915']
    model_name = ['General', 'Personal']
    fmts = ['o', 'x']
    plt.ylim(0, 25)
    plt.ylabel('WPM', fontsize=16)
    plt.xticks([1, 2, 3, 4, 5], ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'], fontsize=16)
    plt.yticks(fontsize=16)

    plt.plot(xs, ys, color=colors[0], label=model_name[0])
    (_, caps, _) = plt.errorbar(xs, ys, fmt=fmts[0], yerr=stds, color=colors[0], markersize=4, capsize=4)
    for cap in caps:
        cap.set_markeredgewidth(1)

    plt.grid(axis='y', linestyle='-.')
    #plt.legend(loc = 'lower right', fontsize=16)
    plt.show()

if __name__ == "__main__":
    data = []
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    name = 'gyz'
    session =  1
    board = 2
    speed = 3
    uer = 4
    cer = 5
    data.append([name, session, board, speed,uer,cer])
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    name = 'g2yz'
    session =  1
    board = 2
    speed = 3
    uer = 4
    cer = 5
    data.append([name, session, board, speed,uer,cer])
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    name = 'gy34z'
    session =  1
    board = 2
    speed = 3
    uer = 4
    cer = 5
    data.append([name, session, board, speed,uer,cer])
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    name = 'gy3z'
    session =  121
    board = 22
    speed = 33
    uer = 43
    cer = 53
    data.append([name, session, board, speed,uer,cer])
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    name = 'gy2z'
    session =  14
    board = 2
    speed = 3
    uer = 44
    cer = 52
    data.append([name, session, board, speed,uer,cer])
    p_user = ["gyz", "syt", "xcy", "ljs", "lw", "cwh", "wjs", "lsm"]
    name = 'gyz1'
    session =  1
    board = 24
    speed = 3
    uer = 42
    cer = 523
    data.append([name, session, board, speed,uer,cer])
    drawing(data)
