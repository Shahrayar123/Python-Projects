# Imports
from pytube import YouTube
import os

# Main function
def main():
	# Clear the terminal for more visibility
	os.system("cls || clear")

	# The video link
	videoLink = input("Enter the link: ")

	yt = YouTube(videoLink)
	print("Please wait...")
	# Search in all streams the video with the highest resolution
	ys = yt.streams.get_highest_resolution()

	# Download the video
	ys.download()

# Call the main function
main()
