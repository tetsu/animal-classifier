from keras.models import load_model
from PIL import Image
import sys
import numpy as np
from config import env

classes = env.CLASSES
image_size = env.IMAGE_SIZE

def main(s=None):
    if s != None:
        filepath = s
    elif len(sys.argv) >= 2:
        filepath = sys.argv[1]
    else:
        print("Please indicate image file path.")
        return False

    result = predict(filepath)
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    print("{0} ({1} %)".format(classes[predicted], percentage))
    return True

def predict(filepath):
    image = Image.open(filepath)
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    x = [data]
    x = np.array(x)
    model = load_model('./image_cnn.h5')

    result = model.predict([x])[0]
    return result


if __name__ == "__main__":
    main()
