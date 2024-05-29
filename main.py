# Import the necessary modules
import pytube
from pytube import YouTube

# Function to download a video from YouTube

def download_video(link):
    try:
        yt = YouTube(link)
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        # Download the video
        stream.download(r"C:\Users\misandfo\Downloads")
        print("Video downloaded successfully")
    except pytube.exceptions.PytubeError as e:
        print("An error occurred: ", e)
    except Exception as e:
        print("An unexpected error occurred: ", e)

# Main function
def main():
    # Prompt the user for a video link
    link = input("Enter the link of the video you want to download: ")
    # Download the video
    download_video(link)

# If this script is the main entry point, run the main function
if __name__ == "__main__":
    main()