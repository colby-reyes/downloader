#%% Imports
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

print("Done importing requirements")

#%% download video
video_url = input() #'https://www.youtube.com/watch?v=YWhSQpUNGgY'
# video.streams.filter(file_extension = "mp4").all()
youtube = YouTube(video_url)
video = youtube.streams.first()
fname = input()
video.download(filename=fname)
# print(video.filesize)

#%% convert to audio
# test if this comment also prints
vid_to_convert = mp.VideoFileClip(f"/Users/colbyr/Documents/GitHub/Sticks_and_Stones.mp4")
vid_to_convert.audio.write_audiofile(f"/Users/colbyr/Documents/GitHub/Sticks_and_Stones.wav")


#%% 






########################################################################################
#                       Alternate Version                                              #
########################################################################################
""" 
The below is an alternate version of the YouTube downloader which utilizes the `requests` module

Troubleshooting:
    - In its current state, it does not produce a valid .mp4 file
"""
# file_url = "https://www.youtube.com/watch?v=YWhSQpUNGgY"
# file_name = "Sticks and Stone.mp4"

# r = requests.get(file_url, stream = True)

# # download started 
# with open(file_name, 'wb') as f: 
#     for chunk in r.iter_content(chunk_size = 1024*1024): 
#         if chunk: 
#             f.write(chunk) 
  
# print(f"{file_name} downloaded!\n")
# %%
