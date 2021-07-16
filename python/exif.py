import exifread
from PIL import Image
from PIL.ExifTags import TAGS

filepath = ""

for (k,v) in Image.open(filepath)._getexif().items():
    print(TAGS.get(k), ":", v)

print("*" * 50)

f = open(filepath, 'rb')
tags = exifread.process_file(f)

for tag in tags.keys():
    print(tag + ":", tags[tag])
