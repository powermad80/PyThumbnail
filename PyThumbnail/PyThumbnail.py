import PIL
import http
import requests
import shutil
import os
import io
from PIL import Image

def thumbnail(url, filename):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        i = Image.open(io.BytesIO(r.content))
        i = i.resize((100, 100))
        i.save("thumbnails/" + filename + ".png")