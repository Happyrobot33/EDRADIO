#library imports
import time
from datetime import *

#local python imports
import JournalRead
import SpotifyControl as Spotify
import VLCRadioControl as Radio
import SettingsManager as settings

#RecieveText currently not implemented as it needs special handling
timeDictionary = {
  "StartJump": 6,
  "DockingGranted": 6,
  "DockingCancelled": 6,
  "Docked": 13,
  "Undocked": 10,
  "DockingDenied": 13,
  "JetConeBoost": 3,
  "FighterDestroyed": 3
}

class EDSR:
    previouslyStoredLastEvent = ""

    def __init__(self, journalPath, mode):
        self.journal = JournalRead.journal()
        self.journal.setJournalPath(journalPath)
        self.journal.update()
        self.shouldEndTime = datetime.now()
        self.mode = mode
    
    def __init__(self, mode):
        self.journal = JournalRead.journal()
        self.journal.findJournalPath('C:\\Users\\Matthew\\Saved Games\\Frontier Developments\\Elite Dangerous\\')
        self.journal.update()
        self.shouldEndTime = datetime.now()
        self.mode = mode

    def runUpdate(self):
        self.journal.update()

        lastEvent = self.journal.getLastEvent()

        if lastEvent in timeDictionary:
            if lastEvent != self.previouslyStoredLastEvent:
                if self.mode == "pause":
                    self.pauseSong()
                else:
                    self.setVolume(settings.getLoweredVolume())
                self.shouldEndTime = datetime.now() + timedelta(0,timeDictionary[lastEvent])
                self.previouslyStoredLastEvent = lastEvent
        
        if (datetime.now() > self.shouldEndTime):
            if self.mode == "pause":
                self.pauseSong()
            else:
                self.setVolume(settings.getWorkingVolume())
                
    #This allows the selection of different audio providers, Spotify premium, Radio
    def setAudioProvider(self, PassedProvider):
        self.Provider = PassedProvider

    def setRadioStation(self, station):
        Radio.selectStation(station)

    def getSongName(self):
        if self.Provider == "Radio":
            return Radio.getRadioStation()
        elif self.Provider == "Spotify":
            return Spotify.getCurrentTrackName()

    def getSongArtist(self):
        if self.Provider == "Radio":
            return "Radio Station"
        elif self.Provider == "Spotify":
            return Spotify.getCurrentTrackArtist()
    
    def getLastEvent(self):
        return self.journal.getLastEvent()
    
    def getVolume(self):
        if self.Provider == "Radio":
            Radio.getVolume()
        elif self.Provider == "Spotify":
            return Spotify.getVolume()

    def pause(self):
        if self.Provider == "Radio":
            Radio.pause()
        elif self.Provider == "Spotify":
            Spotify.pause()
    
    def resume(self):
        if self.Provider == "Radio":
            Radio.play()
        elif self.Provider == "Spotify":
            Spotify.play()
    
    def setVolume(self, percent):
        if self.Provider == "Radio":
            Radio.setVolume(percent)
        elif self.Provider == "Spotify":
            Spotify.setVolume(percent)

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode
    
    def toggleMode(self):
        if self.mode == "pause":
            self.mode = "volume"
        else:
            self.mode = "pause"