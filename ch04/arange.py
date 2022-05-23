import numpy as np

batch_size = 5
A = np.arange(batch_size)
print(f'np.arangeの出力:{A}')

t = [2,3,0,1,4]
y = np.array([[1,2,3,4,5],[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45]])
B = y[np.arange(batch_size),t]

print(f'y[np.arange(batch_size),t]の出力:{B}')