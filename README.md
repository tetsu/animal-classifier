# Animal Classifier
Classify animal photos.

## How to Setup

1. Download Anaconda from [anaconda.com](https://www.anaconda.com/), and install it.
1. Setup new python environment with Anacond-Navigator
1. Open a terminal window, and do following installations
1. Add TensorFlow:

    ```
    pip install tensorflow
    ```

1. Add FlickrAPI:

    ```
    pip install flickrapi
    ```

1. Clone this repository

    ```
    git clone git@github.com:tetsu/animal-classifier.git
    ```

1. create `config`, `monkey`, and `boar` folders
1. Create `env.py` under `config` folder with Flickr account. Type following data in `env.py`.

    ```python
    FLICKR_KEY = "{your flickr key}"
    FLICKR_SECRET = "{your flickr secret}"
    ```

1. Download monkey images

    ```
    python download.py monkey
    ```
