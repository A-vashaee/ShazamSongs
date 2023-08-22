
# pip install google-api-python-client
# pip install pytube

import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from googleapiclient.discovery import build

root = tk.Tk()
root.withdraw()  # Hide the main tkinter window
    
shazamlibrary = filedialog.askopenfile(title="Select the shazamlibrary csv file")
df = pd.read_csv(shazamlibrary)

# make a dataframe from original dataset
# row_ite = range(1, len(df['Shazam Library']))
row_ite = range(1, 50)
new_data = []  

for x in row_ite:
    test_data = np.array((df['Shazam Library'][[x]].index)[0])
    test_data = pd.Series(test_data.reshape(1, 5)[0])
    new_data.append(test_data)  # Append the series to the list

# Concatenate all the series into a single DataFrame
new_data_df = pd.concat(new_data, axis=1, ignore_index=True)

# Transpose the DataFrame to get each series as a row
new_data_df = new_data_df.T

# Assign the columns of the dataframe
new_data_df.columns = list((df['Shazam Library'][[0]].index)[0])

final_df = new_data_df[['Title', 'Artist']]
final_df = final_df.drop_duplicates()
# final_df

# two functions that creat search for youtube links and put them in a list
# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
API_KEY = 'AIzaSyCPpvWr49X1uE0AMiPmQfx0q3M1WRE0-f0'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_youtube_link(song):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    search_response = youtube.search().list(
        q=f"{song}",
        part='id',
        type='video',
        maxResults=1
    ).execute()

    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return "Not found"


def youtube_links(df):
    youtubeLinks = []
    for songs in df.itertuples():
        youtube_link = search_youtube_link(songs[1]+' '+songs[2])
        youtubeLinks.append(youtube_link)
    return youtubeLinks

links_list = youtube_links(final_df)
links_list
