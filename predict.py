from keras.models import load_model
from PIL import Image
import sys
import numpy as np
from config import env

classes = env.CLASSES
image_size = env.IMAGE_SIZE

def main():
    image = Image.open(sys.argv[1])
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    x = []
    x.append(data)
    x = np.array(x)
    model = load_model('./image_cnn.h5')

    result = model.predict([x])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    print("{0} ({1} %)".format(classes[predicted], percentage))

if __name__ == "__main__":
    main()
