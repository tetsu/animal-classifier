from PIL import Image
import os, glob
import numpy as np
from sklearn import cross_validation

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

#load images
X = []
Y = []
for index, class in enumerate(classes):
    photo_dir = "./" + class
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
