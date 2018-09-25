# Download specified photo from Flickr

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
from config import env

# env data
classes = env.CLASSES
per_page = env.NUMBER_OF_IMAGES

# Flickr API info
key = env.FLICKR_KEY
secret = env.FLICKR_SECRET
wait_time = 0.5

def downloader(image_class):
    # Assign or create an image folder
    image_dir = "./images/" + image_class
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Flickr image search
    flickr = FlickrAPI(key, secret, format='parsed-json')
    result = flickr.photos.search(
        text = image_class,
        per_page = per_page,
        media = 'photos',
        sort = 'relevance',
        safe_search = 1,
        extras = 'url_q, license'
    )

    # Extract search result JSON
    photos = result['photos']

    # Download images
    print('Started downloading "' + image_class + '" images')
    for i, photo in enumerate(photos['photo']):
        if 'url_q' in photo:
            if i % 10 == 0:
                max_num = i+10 if i+10 < len(photos['photo']) else len(photos['photo'])
                print("Downloading " + str(i) + " to " + str(max_num) \
                    + " of " + str(len(photos['photo'])))
            url_q = photo['url_q']
            filepath = image_dir + '/' + photo['id'] + '.jpg'
            if os.path.exists(filepath): continue
            urlretrieve(url_q, filepath)
            time.sleep(wait_time)

    print('"' + image_class + '" images downloaded.')

    return True

def main():
    if len(sys.argv) >= 2:
        downloader(sys.argv[1])
    else:
        for image_class in classes:
            downloader(image_class)

if __name__ == "__main__":
    main()
