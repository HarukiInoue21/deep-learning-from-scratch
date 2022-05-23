import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y + delta))

t =[0,0,1,0,0,0,0,0,0,0]#2を正解とする#

#2の確率が最も高い#
y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
A = cross_entropy_error(np.array(y1),np.array(t))
print(f'2の確率が最も高い場合の損失関数:{A}')

#7の確率が最も高い場合#
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
B = cross_entropy_error(np.array(y2),np.array(t))
print(f'7の確率が最も高い場合の損失関数:{B}')
