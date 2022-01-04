import vlc
import time

#built in radio stations
RADIOSIDEWINDER = 'http://radiosidewinder.out.airtime.pro:8000/radiosidewinder_a'
LAVERADIO = 'https://kathy.torontocast.com:2610/stream'

url = 'http://radiosidewinder.out.airtime.pro:8000/radiosidewinder_a'
stationName = "Radio Sidewinder"

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
    if station == "RadioSidewinder":
        url = RADIOSIDEWINDER
        stationName = "Radio Sidewinder"
    elif station == "LaveRadio":
        url = LAVERADIO
        stationName = "Lave Radio"
    
    #Define VLC player
    player=instance.media_player_new()
    #Define VLC media
    media=instance.media_new(url)
    #Set player media
    player.set_media(media)

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