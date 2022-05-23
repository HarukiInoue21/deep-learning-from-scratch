import numpy as np

def sum_squared_error(y,t):
    return 0.5*np.sum((y-t)**2)

t =[0,0,1,0,0,0,0,0,0,0]#2を正解とする#

#2の確率が最も高い#
y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
A = sum_squared_error(np.array(y1),np.array(t))
print(f'2の確率が最も高い場合の損失関数:{A}')

#7の確率が最も高い場合#
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
B = sum_squared_error(np.array(y2),np.array(t))
print(f'7の確率が最も高い場合の損失関数:{B}')