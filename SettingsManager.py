#Library imports
import json

settings = {}

def getWorkingVolume():
    readSettings()
    return settings["workingVolume"]

def getLoweredVolume():
    readSettings()
    return settings["loweredVolume"]

def getMediaSource():
    readSettings()
    return settings["mediaSource"]

def getRadioStation():
    readSettings()
    return settings["specifiedStation"]

def readSettings():
    global settings

    file = open("settings.json")
    settings = json.load(file)