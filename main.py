import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv('./train.csv')
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0,1000].T
data_dev