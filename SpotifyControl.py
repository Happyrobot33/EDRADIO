from http.cookiejar import DefaultCookiePolicy
from logging import exception
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.util import CLIENT_CREDS_ENV_VARS
import json

scope = "streaming app-remote-control user-read-playback-state user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='3bdd08cd9fbf4e1b8437467c357494e8', client_secret='3c0f5bb75e314ae99d8ebcc20184f0db', redirect_uri='http://localhost:8080', open_browser=True))

#Control Functions
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

#User Functions
def getCurrentTrackName():
    global sp
    try:
        return sp.current_user_playing_track()["item"]["name"]
    except:
        return "NULL"

def getCurrentTrackID():
    global sp
    try:
        return sp.current_user_playing_track()["item"]["id"]
    except:
        return "NULL"

def getCurrentTrackArtist():
    global sp
    try:
        return sp.track(getCurrentTrackID())["artists"][0]['name']
    except:
        return "NULL"

def toString():
    return "Currently Playing: " + getCurrentTrackName() + " \nArtist: " + getCurrentTrackArtist()