from pytube import YouTube
from pathlib import Path

download_path = str(Path.home() / "Downloads")

# ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

# Showing details
print("Title: ", yt.title)
print("Author: ", yt.author)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
print("Description of video: ", yt.description)

user_input = input("Do you want a description of video?y/n ")

user_input2 = input("Do you want audio only? y/n")

if user_input2 == 'y' or 'Y':
    print("Downloading audio only")
    yt.streams.get_audio_only().download(download_path)
    print("Download completed!!")
else:
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download(download_path)
    print("Download completed!!")

