from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection
from config import env

classes = env.CLASSES
num_classes = len(classes)
image_size = env.IMAGE_SIZE

#load images
x = []
y = []
for index, classlabel in enumerate(classes):
    photo_dir = "./images/" + classlabel
    files = glob.glob(photo_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 180: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)
        x.append(data)
        y.append(index)

x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)
xy = (x_train, x_test, y_train, y_test)
np.save("./image.npy", xy)
