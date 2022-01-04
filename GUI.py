#Library Imports
from tkinter import *
from tkinter.constants import CENTER
import pyglet

#Local Code Imports
import EDSR_v2
import SettingsManager as settings

pyglet.font.add_directory('Fonts')

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("EDSR")
        master.geometry("500x150")
        master.configure(bg="black")
        #self.EDSR = EDSR_v2.EDSR('C:\\Users\\Matthew\\Saved Games\\Frontier Developments\\Elite Dangerous\\Journal.211226192835.01.log')
        self.EDSR = EDSR_v2.EDSR(settings.getMode())
        self.EDSR.setAudioProvider(settings.getMediaSource())
        self.EDSR.resume()
        self.EDSR.setRadioStation(settings.getRadioStation())
        self.canvas = Canvas(master)

        #Constants
        SONGINFOX = 60
        SONGINFOY = 2
        #Color Constants
        EDOrange = "#FBA706"
        EDOrangeHot = "#FFFA64"
        EDOrangeMid = "#FFC236"
        Black = "black"

        #Song Info Labels
        self.SongName = StringVar("")
        self.SongNameLabel = Label(master, textvariable=self.SongName, font=("EuroStyle", 45), anchor="center", bg=Black, fg=EDOrange)
        self.SongNameLabel.place(x= SONGINFOX, y = SONGINFOY + 20)
        self.SongArtist = StringVar("")
        self.SongArtistLabel = Label(master, textvariable=self.SongArtist, font=("EuroStyle", 15), anchor="center", bg=Black, fg=EDOrange)
        self.SongArtistLabel.place(x= SONGINFOX, y = SONGINFOY)

        #Status Symbols
        self.lastEvent = StringVar("")
        self.lastEventLabel = Label(master, textvariable=self.lastEvent, font=("EuroStyle", 15), anchor="center", bg=Black, fg=EDOrange)
        self.lastEventLabel.place(x= SONGINFOX + 200, y = SONGINFOY)
        self.currentMode = StringVar("")
        self.currentModeLabel = Label(master, textvariable=self.currentMode, font=("EuroStyle", 15), anchor="center", bg=Black, fg=EDOrange)
        self.currentModeLabel.place(x= SONGINFOX, y = SONGINFOY + 81)
        self.currentWorkingVolume = StringVar("")
        self.currentWorkingVolumeLabel = Label(master, textvariable=self.currentWorkingVolume, font=("EuroStyle", 15), anchor="center", bg=Black, fg=EDOrange)
        self.currentWorkingVolumeLabel.place(x= SONGINFOX, y = SONGINFOY + 81 + 20)
        self.currentLoweredVolume = StringVar("")
        self.currentLoweredVolumeLabel = Label(master, textvariable=self.currentLoweredVolume, font=("EuroStyle", 15), anchor="center", bg=Black, fg=EDOrange)
        self.currentLoweredVolumeLabel.place(x= SONGINFOX, y = SONGINFOY + 81 + 40)

        #Control Buttons
        self.close_button = Button(master, text="Quit", command=master.quit, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.close_button.place(x= 0, y = 0)
        self.pause_button = Button(master, text="Pause", command=self.EDSR.pause, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.pause_button.place(x= 0, y = 25)
        self.play_button = Button(master, text="Play", command=self.EDSR.resume, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.play_button.place(x= 0, y = 50)
        self.mode_toggle_button = Button(master, text="Mode", command=self.EDSR.toggleMode, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.mode_toggle_button.place(x= 0, y = 75)
        self.switch_provider_spotify_button = Button(master, text="Spotify", command=self.switchToSpotify, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.switch_provider_spotify_button.place(x= 0, y = 100)
        self.switch_provider_radio_button = Button(master, text="Radio", command=self.switchToRadio, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.switch_provider_radio_button.place(x= 0, y = 125)

        self.canvas.create_line(SONGINFOX-1, 0, SONGINFOX-1, 1000, fill=EDOrange)
        self.canvas.create_line(SONGINFOX-1, SONGINFOY+80, 1000, SONGINFOY+80, fill=EDOrange)
        self.canvas.configure(bg=Black, bd=0, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=1)

        #Final cleanup and run update functions
        self.update()
    
    def switchToSpotify(self):
        self.EDSR.setAudioProvider("Spotify")
    
    def switchToRadio(self):
        self.EDSR.setAudioProvider("Radio")

    def update(self):
        #Update our data
        self.EDSR.runUpdate()

        self.SongName.set(self.EDSR.getSongName())
        self.SongArtist.set(self.EDSR.getSongArtist())
        self.lastEvent.set("Event : " + self.EDSR.getLastEvent())
        self.currentMode.set("Current Event Mode : " + self.EDSR.getMode())
        self.currentWorkingVolume.set("Set Standby Volume : " + str(settings.getWorkingVolume()))
        self.currentLoweredVolume.set("Set Event Volume : " + str(settings.getLoweredVolume()))

        #Needed to que this function again
        self.master.after(100, self.update)

root = Tk()
gui = GUI(root)
root.mainloop()