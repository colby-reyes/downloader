# system management packages
import sys 
import os
import shutil
import math
import datetime

# plots
import matplotlib.pyplot as plt
#%matplotlib inline

# image operation
import cv2
import moviepy.editor as mp

# special packages
from pytube import YouTube
import requests
import re

video_url = 'https://www.youtube.com/watch?v=YWhSQpUNGgY'
# video.streams.filter(file_extension = "mp4").all()
youtube = YouTube(video_url)
video = youtube.streams.first()
video.download(filename="Sticks_and_Stones")
print(video.filesize)


# file_url = "https://www.youtube.com/watch?v=YWhSQpUNGgY"
# file_name = "Sticks and Stone.mp4"

# r = requests.get(file_url, stream = True)

# # download started 
# with open(file_name, 'wb') as f: 
#     for chunk in r.iter_content(chunk_size = 1024*1024): 
#         if chunk: 
#             f.write(chunk) 
  
# print(f"{file_name} downloaded!\n")