#create a program to download videos from youtube
import pytube
from pytube import YouTube

#ask the user for the link of the video
link = input("Enter the link of the video you want to download: ")

#download the video to the downloads folder
YouTube(link).streams.first().download(r"C:\Users\misandfo\Downloads")
print("Video downloaded successfully")
