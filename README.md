# Keras Image Classifier
Classify images by Deep Learning using Keras with TensorFlow backend.

## How to Setup

1. Download Anaconda from [anaconda.com](https://www.anaconda.com/), and install it.
1. Setup new python environment with Anacond-Navigator
1. Open a terminal window, and do following installations
1. Add TensorFlow module to your Python environment by typing following command in terminal.

    ```
    pip install tensorflow
    ```

1. Add FlickrAPI module to your Python environment by typing following command in terminal.

    ```
    pip install flickrapi
    ```

1. Add pillow module to your Python environment by typing following command in terminal.

    ```
    pip install pillow
    ```

1. Add Scikit-Learn module to your Python environment by typing following command in terminal.

    ```
    pip install sklearn
    ```

1. Add keras module to your Python environment by typing following command in terminal.

    ```
    pip install keras
    ```

1. Add Flask module to your Python environment by typing following command in terminal.

    ```
    pip install Flask
    ```

1. Go to your working folder, and clone this repository by typing following command in terminal.

    ```
    git clone git@github.com:tetsu/animal-classifier.git
    ```

1. Create a [Flickr](https://www.flickr.com/) account, and enter Flickr Key and Secret in `config/env_sample.py`, and rename the file to `env.py`.

    ```python
    FLICKR_KEY = "{your flickr key}"
    FLICKR_SECRET = "{your flickr secret}"
    CLASSES = ["monkey", "boar", "crow"]
    IMAGE_SIZE = 50
    NUMBER_OF_IMAGES = 400
    ```

1. Go to the top folder of this project, and download images of assigned classes by typing following command in terminal.

    ```
    python download.py
    ```

1. Check folders under "images" folder, and remove images that are not proper for learning, such as unclear images, wrong images, images with other animals or breeds, etc.

1. Convert images to NUMPY data to use on Keras by typing following command in terminal.

    ```
    python gen_data.py
    ```

1. Train model, generate trained neural network h5 file, and evaluate the result by typing following command in terminal.

    ```
    python image_cnn.py
    ```

1. Classify an image by typing following command in terminal.

    ```
    python predict.py {an image file path}
    ```

1. Run Flask app by typing following command in terminal
    ```
    FLASK_APP=index.py flask run
    ```
