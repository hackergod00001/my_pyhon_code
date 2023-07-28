from pytube import YouTube
from sys import argv

link = argv[1]
YT = YouTube(link)

print("Title: ", YT.title)
print("Views: ", YT.views)

YD = YT.streams.get_highest_resolution()

YD.download('/Users/maste/Downloads/videos')