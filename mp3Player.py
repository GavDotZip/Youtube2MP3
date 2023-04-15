import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Set the GUI
mp3 = tkr.Tk()
mp3.title("Enjoy the Music!")
mp3.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(mp3, font="Helvetica 12 bold", bg='black', fg='white', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


playButton = tkr.Button(mp3, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="green",
                        fg="white")
pauseButton = tkr.Button(mp3, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause,
                         bg="yellow", fg="white")
stopButton = tkr.Button(mp3, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red",
                        fg="white")
unpauseButton = tkr.Button(mp3, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause,
                           bg="blue", fg="white")

var = tkr.StringVar()
song_title = tkr.Label(mp3, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
playButton.pack(fill="x")
pauseButton.pack(fill="x")
stopButton.pack(fill="x")
unpauseButton.pack(fill="x")

play_list.pack(fill="both", expand="yes")
mp3.mainloop()
