from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection
from config import env

classes = env.CLASSES
num_classes = len(classes)
image_size = env.IMAGE_SIZE

#load images
X = []
Y = []
for index, classlabel in enumerate(classes):
    photo_dir = "./images/" + classlabel
    files = glob.glob(photo_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 100: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, Y_train, Y_test)
np.save("./image.npy", xy)
