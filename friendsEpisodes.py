import os

import requests, json
from bs4 import BeautifulSoup
from flask import request


class EpisodeInfo:
    def __init__(self):
        self.name = None
        self.link = None

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link

    def set_name(self, name):
        self.name = name

    def set_link(self, link):
        self.link = link


url = "https://en.wikipedia.org/wiki/List_of_Friends_episodes"
baseUrl = "https://en.wikipedia.org"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

episode_list = soup.findAll("td", class_=["summary"])

episodeInfoList = []

for episode in episode_list:
    tag = episode.find("a")
    episodeInfo = EpisodeInfo()
    test = None
    if tag is not None:
        text = tag.getText()
        if text[0] == '[' or text[0] == '†':
            continue
        episodeInfo.set_name(text)
        episodeInfo.set_link(baseUrl + tag['href'])
        test = json.dumps({'name': text, 'link': baseUrl + tag['href']})
    else:
        episodeInfo.set_name(episode.getText())
        episodeInfo.set_link(None)
        text = episode.getText()[1:len(episode.getText()) - 1]
        test = json.dumps({'name': text, 'link': ''})

    episodeInfoList.append(test)
    # episodeInfoList.append(episodeInfo)

path = '/home/reiniskr1/mysite/static/FriendsEpisodes.json'
with open(path, 'w') as f:
    json.dump(episodeInfoList, f)
