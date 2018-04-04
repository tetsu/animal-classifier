# Animal Classifier
Classify animal photos by Deep Learning.

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

1. Go to your working folder, and clone this repository by typing following command in terminal.

    ```
    git clone git@github.com:tetsu/animal-classifier.git
    ```

1. Create a [Flickr](https://www.flickr.com/) account, and enter Flickr Key and Secret in `config/env_sample.py`, and rename the file to `env.py`.

    ```python
    FLICKR_KEY = "{your flickr key}"
    FLICKR_SECRET = "{your flickr secret}"
    ```

1. Download monkey images by typing following command in terminal.

    ```
    python download.py monkey
    ```
