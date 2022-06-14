import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist



(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

a = x_test.shape
print(a)