from pytube import YouTube
import os

# Take in URL from YouTube.com to be converted to MP3
url = YouTube(str(input("Enter URL of youtube video: \n ")))
video = url.streams.filter(only_audio=True).first()  # Only take audio from YouTube video

print("Select a Folder:  (leave blank to save in current directory)")
folder = str(input(" ")) or '.'

# Save file to selected folder
out = video.download(output_path=folder)
base, ext = os.path.splitext(out)
mp3File = base + '.mp3'
os.rename(out, mp3File)
print(url.title + " download complete.")
