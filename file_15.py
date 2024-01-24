from tkinter import *
from PIL import  Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Hamxah")
# root.iconbitmap("/home/hamza/Desktop/TKinter_Files/Image.ico")



def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Desktop/Pictures", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()





















# return self.tk.call('wm', 'iconbitmap', self._w, bitmap)
# _tkinter.TclError: bitmap "/home/hamza/Desktop/TKinter_Files/Image.ico" not defined