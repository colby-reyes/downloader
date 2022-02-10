#%% Imports
# system management packages
import sys 
import os
import shutil
import math
import datetime

# plots
#import matplotlib.pyplot as plt
#%matplotlib inline

# special packages
from pytube import YouTube

print("Done importing requirements")

#%% download video
#video_url = input() #'https://www.youtube.com/watch?v=YWhSQpUNGgY'
video_url = 'https://www.youtube.com/watch?v=jvM9AfAzoSo'
# video.streams.filter(file_extension = "mp4").all()
youtube = YouTube(video_url)
video = youtube.streams.first()
fname = '/Users/colbyr/Downloads/ADHD_Relief.mp4'
video.download(filename=fname)
songfile_name = f"{fname[:-4]}.m4a"

os.system(f"ffmpeg -i {fname} {songfile_name}")


""" 
TODO: edit id3 tags
	- mutagen or eyed3? -> see jupyter notebook
TODO: enable playback of "reyesinrsm@cox.net" songs on this Mac
	- try to remove or change ID3 tags:
		account_id      : reyesinrsm@cox.net
    	copyright       : ℗ (c) 2006 Disciple
    	creation_time   : 2028-08-06T12:00:05.000000Z
    	iTunSMPB        :  00000000 00000840 00000210 00000000009199B0 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
    	iTunNORM        :  00002A25 00002BC3 000072DF 0000789E 00026754 0002646D 00007FFF 00007FFF 0000829D 00008584
    	 iTunMOVI        : <?xml version="1.0" encoding="UTF-8"?>
                    : <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
                    : <plist version="1.0">
                    : <dict>
                    : 	<key>asset-info</key>
                    : 	<dict>
                    : 		<key>flavor</key>
                    : 		<string>1:128</string>
                    : 	</dict>
                    : </dict>
                    : </plist>
    - edit genres
    	- reduce genres to "Worship", "Rock", and "Binaural/Isochronic"
    - will probably need to change and re-add to itunes/music (see below)
"""

"""
TODO: make sure moving to music works
"""

try:
	# move to "Automatically Add to Itunes" folder
	os.cp(songfile_name, '/Users/colbyr/Music/iTunes/iTunes Media/Automatically Add to Music.localized')
except Error as e:
	print(f"Could not copy file to iTunes: {e}")


# # convert to audio with moviepy
# import moviepy.editor as mp

# vid_to_convert = mp.VideoFileClip(f"/Users/colbyr/Downloads/NiteCode_studymusic.mp4")
# vid_to_convert.audio.write_audiofile(f"/Users/colbyr/Downloads/Intense_BinauralFocus.m4a")


########################################################################################
#                       Alternate Version                                              #
########################################################################################
""" 
The below is an alternate version of the YouTube downloader which utilizes the `requests` module

Troubleshooting:
    - In its current state, it does not produce a valid .mp4 file
"""
#%% Imports
# # system management packages
# import sys 
# import os
# import shutil
# import math
# import datetime

# # plots
# import matplotlib.pyplot as plt
# %matplotlib inline

# # image operation
# import cv2
# import numpy as np
# import moviepy.editor as mp

# # special packages
# from pytube import YouTube
# import requests
# import re

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
