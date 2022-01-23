from concurrent.futures import thread
from http.cookiejar import DefaultCookiePolicy
from logging import exception
import spotipy
from spotipy.oauth2 import SpotifyPKCE
from spotipy.util import CLIENT_CREDS_ENV_VARS
import json
import threading
import time

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
    global sp
    try:
        sp.volume(percent)
    except:
        pass


def getVolume():
    global sp
    try:
        sp.volume()
    except:
        return 0


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
    exit()


def updateStoredTrackInfo():
    global runFlag
    while runFlag:
        time.sleep(1)
        global trackName
        global trackArtist
        localTrackName = ""
        localTrackArtist = ""
        json = getCurrentTrackJson()
        try:
            localTrackName = json["item"]["name"]
            localTrackArtist = json["item"]["artists"][0]["name"]
        except:
            localTrackName = "SPOTIFY NOT ACTIVE/UNREACHABLE"
            localTrackArtist = "UNFINDABLE"

        # These are seperated in order to limit blocking access to these global variables
        print("Pushing new variables")
        trackName = localTrackName
        trackArtist = localTrackArtist
    print("Thread killed!")


# Create a Thread with a function without any arguments
th = threading.Thread(target=updateStoredTrackInfo)

# User Functions
def getCurrentTrackName():
    global trackName
    return trackName


def getCurrentTrackArtist():
    global trackArtist
    return trackArtist


def toString():
    return "Currently Playing: " + getCurrentTrackName() + " \nArtist: " + getCurrentTrackArtist()
