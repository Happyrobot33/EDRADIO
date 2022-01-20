# Library imports
import glob
import json
import os


class journal:
    # global variables
    journalPath = ""
    journalFolderPath = ""
    lastEventJson = ""

    # set the current journal path
    def setJournalPath(self, pathDirectlyToJournal):
        self.journalPath = pathDirectlyToJournal

    # Automatically find latest journal
    def findJournalPath(self, journalFolderPath):
        self.journalFolderPath = journalFolderPath
        # journalPath = journalFolderPath + 'Journal.220103161413.01.log'
        journalFiles = glob.glob(journalFolderPath + "\\*.log")
        self.journalPath = max(journalFiles, key=os.path.getmtime)

    # return the current journal path
    def getJournalPath(self):
        return self.journalPath

    # return the current JSON text
    def getlastEventJson(self):
        if self.lastEventJson == "":
            return "{'timestamp': '0000-00-00T00:00:00Z'}"
        return self.lastEventJson

    def getLastEvent(self):
        return self.lastEventJson["event"]

    # Updates the stored journal
    def update(self):

        with open(self.journalPath) as f:
            for line in f:
                self.lastEventJson = json.loads(line)

        # This ensures that the new journal file will be found if we restarted the game
        if self.getLastEvent() == "Shutdown":
            print("Searching for new journal file...")
            self.findJournalPath(self.journalFolderPath)
