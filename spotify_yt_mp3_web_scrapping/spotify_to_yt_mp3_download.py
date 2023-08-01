from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
from pytube import YouTube
import requests
import pandas
import os

# ? this is just a sample web scraping code for single mp3 file to download but you can edit this file if you need.


def DownloadVideosFromTitles(los):
    ids = []
    for index, item in enumerate(los):
        vid_id = ScrapeVidId(item)
        ids += [vid_id]
    print("Downloading songs")
    DownloadVideosFromIds(ids)


def DownloadVideosFromIds(lov):
    SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs"))
    try:
        os.mkdir(SAVE_PATH)
    except:
        print("download folder exists")
    # url input from user
    yt = YouTube(str(lov))
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    # download the file
    out_file = video.download(output_path=SAVE_PATH)
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


def ScrapeVidId(query):
    print("Getting video id for: ", query)
    BASIC = "http://www.youtube.com/results?search_query="
    DOWN_VID_PART1 = "https://www.youtube.com/watch?v="
    URL = (BASIC + query)
    URL.replace(" ", "+")
    page = requests.get(URL)
    session = HTMLSession()
    response = session.get(URL)
    response.html.render(sleep=1)
    soup = BeautifulSoup(response.html.html, "html.parser")

    results = soup.find('a', id="video-title")
    result_vid_part2 = results['href'].split('/watch?v=')[1]
    result_final = DOWN_VID_PART1 + result_vid_part2
    print(result_final)
    return result_final


def __main__():

    data = pandas.read_csv('songs.csv')
    data = data['song names'].tolist()
    print("Found ", len(data), " songs!")
    DownloadVideosFromTitles(data[0:1])


__main__()
