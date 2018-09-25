# Download specified photo from Flickr

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
from config import env

# Flickr API info
key = env.FLICKR_KEY
secret = env.FLICKR_SECRET
wait_time = 0.5

# Assign or create an image folder
image_class = sys.argv[1]
image_dir = "./images/" + image_class
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Flickr image search
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = image_class,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license'
)

# Extract search result JSON
photos = result['photos']

# Download images
pprint('Downloading ' + image_class)
for i, photo in enumerate(photos['photo']):
    if 'url_q' in photo:
        url_q = photo['url_q']
        filepath = image_dir + '/' + photo['id'] + '.jpg'
        if os.path.exists(filepath): continue
        urlretrieve(url_q, filepath)
        time.sleep(wait_time)

pprint(image_class + ' download completed.')
