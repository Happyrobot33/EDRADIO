#Library imports
import json

settings = {}

def getWorkingVolume():
    readSettings()
    return settings["workingVolume"]
def setWorkingVolume(percent):
    global settings
    readSettings()
    settings["workingVolume"] = percent
    saveSettings()


def getLoweredVolume():
    readSettings()
    return settings["loweredVolume"]
def setLoweredVolume(percent):
    global settings
    readSettings()
    settings["loweredVolume"] = percent
    saveSettings()
    

def getMediaSource():
    readSettings()
    return settings["mediaSource"]
def setMediaSource(mediaSource):
    global settings
    readSettings()
    settings["mediaSource"] = mediaSource
    saveSettings()

def getRadioStation():
    readSettings()
    return settings["specifiedStation"]
def setRadioStation(station):
    global settings
    readSettings()
    settings["specifiedStation"] = station
    saveSettings()


def getMode():
    readSettings()
    return settings["mode"]
def setMode(mode):
    global settings
    readSettings()
    settings["mode"] = mode
    saveSettings()

def getJournalFolder():
    readSettings()
    return settings["journalFolder"]

def readSettings():
    global settings
    file = open("settings.json")
    settings = json.load(file)
    file.close()

def saveSettings():
    if settings != "":
        with open("settings.json", "w") as outfile:
            json.dump(settings, outfile, indent=4)
            outfile.close()