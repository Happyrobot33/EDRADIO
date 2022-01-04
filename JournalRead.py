#Library imports
import glob
import json
import os

class journal:
    #global variables
    journalPath = ""
    lastEventJson = ""

    #set the current journal path
    def setJournalPath(self, pathDirectlyToJournal):
        global journalPath
        journalPath = pathDirectlyToJournal

    #Automatically find latest journal
    def findJournalPath(self, journalFolderPath):
        global journalPath
        #journalPath = journalFolderPath + 'Journal.220103161413.01.log'
        journalFiles = glob.glob(journalFolderPath + "\\*.log")
        journalPath = max(journalFiles, key=os.path.getmtime)

    #return the current journal path
    def getJournalPath(self):
        global journalPath
        return journalPath

    #return the current JSON text
    def getlastEventJson(self):
        global lastEventJson

        if lastEventJson == "":
            return "{'timestamp': '0000-00-00T00:00:00Z'}"
        return lastEventJson
    
    def getLastEvent(self):
        return lastEventJson["event"]

    #Updates the stored journal
    def update(self):
        global lastEventJson
        global journalPath
        
        with open(journalPath) as f:
            for line in f:
                lastEventJson = json.loads(line)
        pass