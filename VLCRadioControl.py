import vlc
import time
import SettingsManager as settings

#built in radio stations
radioStations = {}

currentDictIndex = 0

url = 'INVALID'
stationName = "SELECT STATION"

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()
#Define VLC media
media=instance.media_new(url)
#Set player media
player.set_media(media)

def selectStation(station):
    global url
    global stationName
    global player
    global media
    global radioStations

    url = radioStations[station]
    stationName = station

    killStream()

    #Define VLC player
    player=instance.media_player_new()
    #Define VLC media
    media=instance.media_new(url)
    #Set player media
    player.set_media(media)
    play()

def play():
    player.play()

def pause():
    player.pause()

def getRadioStation():
    return stationName

def getVolume():
    return player.audio_get_volume()

def setVolume(percent):
    player.audio_set_volume(percent)

def killStream():
    player.stop()

def readStations():
    global radioStations

    radioStations = settings.getAvailableRadioStations()

def cycleNextStation():
    global currentDictIndex
    global radioStations
    
    currentDictIndex += 1

    if currentDictIndex == len(radioStations):
         currentDictIndex = 0
    
    keyName = list(radioStations)

    #Find the key name associated with the index
    selectStation(keyName[currentDictIndex])