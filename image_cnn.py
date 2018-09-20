from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils  import np_utils
import numpy as np

classes = env.CLASSES
num_classes = len(classes)
image_size = env.IMAGE_SIZE

# メインの関数を定義する
