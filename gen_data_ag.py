from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection
from config import env

classes = env.CLASSES
num_classes = len(classes)
image_size = env.IMAGE_SIZE
num_test = 100

#load images
x_train = []
x_test = []
y_train = []
y_test = []

for index, classlabel in enumerate(classes):
    photo_dir = "./images/" + classlabel
    files = glob.glob(photo_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 180: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_test:
            x_test.append(data)
            y_test.append(index)
        else:
            for angle in range(-20, 20, 5):
                # Multiply images by rotating
                img_r = image.rotate(angle)
                data = np.asarray(img_r)
                x_train.append(data)
                y_train.append(index)

                # Multipy images by transposing
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                x_train.append(data)
                y_train.append(index)


x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

xy = (x_train, x_test, y_train, y_test)
np.save("./image_ag.npy", xy)
