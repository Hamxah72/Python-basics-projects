from tkinter import *
import pygame

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("/home/hamza/Downloads/MUsiqah/Ayo-Teo-Rolex-via-Naijafinix.com_.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()


my_button = Button(root, text="Play Song", font=("Helvetica"), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack(pady=20)


root.mainloop()