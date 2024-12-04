# A very simple Flask Hello World app for you to get started with...
import os

from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/friends')
def FriendsEpisodes():
    return render_template("friendsEpisodes.html")


@app.route('/friendsData')
def friendsData():
    path = '/home/reiniskr1/mysite/static/FriendsEpisodes.json'
    if not os.path.exists(path):
        return
    with open(path, 'r') as f:
        resList = json.load(f)
    return json.dumps(resList)
