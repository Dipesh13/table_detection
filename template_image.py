import numpy as np

arr = np.arrange(8)

x = arr.reshape(2,4)

import matplotlib.pyplot as plt

img = plt.imread('filename.png')

print(type(img))

print(img.shape)

print(img.size)

print(img)

xyz = img.flatten()

print(xyz.shape)

