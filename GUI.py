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
        master.geometry("1000x80")
        master.configure(bg="black")
        #self.EDSR = EDSR_v2.EDSR('C:\\Users\\Matthew\\Saved Games\\Frontier Developments\\Elite Dangerous\\Journal.211226192835.01.log')
        self.EDSR = EDSR_v2.EDSR("volume")
        self.EDSR.setAudioProvider("Radio")
        self.EDSR.resume()
        self.EDSR.setRadioStation(settings.getRadioStation())
        self.canvas = Canvas(master)

        #Constants
        SONGINFOX = 55
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

        self.lastEvent = StringVar("")
        self.lastEventLabel = Label(master, textvariable=self.lastEvent, font=("EuroStyle", 15), anchor="center", bg=Black, fg=EDOrange)
        self.lastEventLabel.place(x= SONGINFOX + 200, y = SONGINFOY)

        #Control Buttons
        self.close_button = Button(master, text="Quit", command=master.quit, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.close_button.place(x= 0, y = 0)
        self.pause_button = Button(master, text="Pause", command=self.EDSR.pause, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.pause_button.place(x= 0, y = 25)
        self.play_button = Button(master, text="Play", command=self.EDSR.resume, font=("EuroStyle", 15), anchor="center", bg="black", fg=EDOrange, border=0, pady=0, activebackground=EDOrange, activeforeground=EDOrangeHot)
        self.play_button.place(x= 0, y = 50)

        self.canvas.create_line(SONGINFOX-1, 0, SONGINFOX-1, 100, fill=EDOrange)
        self.canvas.configure(bg=Black, bd=0, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=1)

        #Final cleanup and run update functions
        self.update()
    
    def update(self):
        #Update our data
        self.EDSR.runUpdate()

        self.SongName.set(self.EDSR.getSongName())
        self.SongArtist.set(self.EDSR.getSongArtist())
        self.lastEvent.set("Event : " + self.EDSR.getLastEvent())

        #Needed to que this function again
        self.master.after(100, self.update)

root = Tk()
gui = GUI(root)
root.mainloop()