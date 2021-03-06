from concurrent.futures import thread
from genericpath import exists
from http.cookiejar import DefaultCookiePolicy
from logging import exception
import spotipy
from spotipy.oauth2 import SpotifyPKCE
from spotipy.util import CLIENT_CREDS_ENV_VARS
import json
import threading
import time
import sys

scope = "streaming app-remote-control user-read-playback-state user-read-currently-playing"
sp = spotipy.Spotify(
    auth_manager=SpotifyPKCE(
        scope=scope,
        client_id="3bdd08cd9fbf4e1b8437467c357494e8",
        redirect_uri="http://localhost:8080",
        open_browser=True,
    )
)

trackName = "SPOTIFY NOT ACTIVE/UNREACHABLE"
trackArtist = "UNFINDABLE"
spotifyVolume = 10
requestedVolume = 10
runFlag = True

# Control Functions
def pause():
    global sp
    try:
        sp.pause_playback()
    except:
        pass


def play():
    global sp
    try:
        sp.start_playback()
    except:
        pass


def setVolume(percent):
    global requestedVolume
    requestedVolume = percent


def getCurrentTrackJson():
    global sp
    return sp.current_user_playing_track()


# This runs the info update on a seperate thread to prevent the GUI from being jittery, due to the HTML call taking a significant time
def startThread():
    global th
    # Start the thread
    try:
        th.start()
    except:
        print("Thread already running!")


def killThread():
    print("Attempting to kill spotify thread")
    global runFlag
    global th
    # set exit flag to true
    runFlag = False
    th.join()
    print("Thread joined!")
    sys.exit()


def update():
    global runFlag

    # Wait for authorization by ensuring .CACHE file exists
    while not exists(".cache"):
        time.sleep(1)

    while runFlag:
        time.sleep(1)
        global trackName
        global trackArtist
        global spotifyVolume
        global requestedVolume
        try:
            json = getCurrentTrackJson()
            trackName = json["item"]["name"]
            trackArtist = json["item"]["artists"][0]["name"]
            sp.volume(requestedVolume)
            spotifyVolume = sp.volume()
        except:
            localTrackName = "SPOTIFY NOT ACTIVE/UNREACHABLE"
            localTrackArtist = "UNFINDABLE"
    print("Thread killed!")


# Create a Thread with a function without any arguments
th = threading.Thread(target=update)
th.daemon = True

# User Functions
def getCurrentTrackName():
    global trackName
    return trackName


def getCurrentTrackArtist():
    global trackArtist
    return trackArtist


def getVolume():
    global spotifyVolume
    return spotifyVolume


def toString():
    return "Currently Playing: " + getCurrentTrackName() + " \nArtist: " + getCurrentTrackArtist()
