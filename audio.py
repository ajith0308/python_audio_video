from playsound import playsound
import tkinter.filedialog
import pygame
from tkinter import *
from tkinter import messagebox

def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
def pause():
    pygame.mixer.music.pause()
def on_closing():
    pygame.mixer.music.stop()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
def resume():
    pygame.mixer.music.unpause()
    
    


def img_sel():
        f = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='E:/',
        title='Choose file',
        filetypes=[('mp3', '.mp3'),
                   ('web', '.webm')]
        )
        return f

root = tkinter.Tk()
root.minsize(400,400)
root.maxsize(1200,650)
mp3File = img_sel()
pygame.init()
pygame.mixer.music.load(mp3File)
play=tkinter.Button(root,text='play',command=play).pack(side=BOTTOM)
#sound.play()
pause=tkinter.Button(root,text='pause',command=pause).pack(side=BOTTOM)

op=tkinter.Button(root,text='open',command=img_sel).pack(side=BOTTOM)

resume=tkinter.Button(root,text='resume',command=resume).pack(side=BOTTOM)

stop=tkinter.Button(root,text='stop',command=stop).pack(side=BOTTOM)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
