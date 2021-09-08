#%% imports
from pytube import YouTube
import os
# define Music library location
music_db_path = f"{os.getenv('HOME')}Music/iTunes/iTunes Media/Music"

# define preset variables
artist_name = "Switchfoot"
album_name = "Fading West"

# define data structure
videos = {"Switchfoot": 
			{
				"album": album_name,
				"tracks":
				{
					"track_titles": [

					], 
					"track_urls": [

					]
				}
			}
		}
os.getenv('USER')


# %%

def check_artist_existence(artist_name, music_db_path=f"{os.getenv('HOME')}/Music/iTunes/iTunes Media/Music"):
	db_path = music_db_path
	artist = artist_name
	if artist in os.listdir(db_path):
		pass
	else:
		print(f"{artist} not found in Music Library. Creating new folder...")
		#os.mkdir(artist)
	print(f"{artist} folder already in Music Library")

# %%
check_artist_existence("Switchfoot")

#%% cycle through and download

for k,i in videos.items():
	print(f"artist: {k}")
	check_artist_existence(k)

	print(f"album: {i['album']}")
	print(f"{i['tracks']}")


