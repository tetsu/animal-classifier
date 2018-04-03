# Download specified photo from Flickr

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
from config import env

#flickr API info
key = env.FLICKR_KEY
secret = env.FLICKR_SECRET
waitTime = 0.5

#image folders
animalName = sys.argv[1]
saveDir = "./" + animalName
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalName,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license'
)

photos = result['photos']
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = saveDir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(waitTime)
