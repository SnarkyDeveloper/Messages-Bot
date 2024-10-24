import requests
from utils.extensionUtils import filePath, imageDownloader


tiktokHelp = "Returns the video of a tiktok"

def tiktok(*args):
    if len(args) == 1:
        return "Enter a URL of a TikTok video"
    response = requests.get(f'https://tikwm.com/api/?url='+args).json()
    fileUrl = response["play"]
    fileLocation = filePath("tiktok/video.mp4")
    title = response[title]

    imageDownloader(fileLocation, fileUrl)

    return fileLocation, title