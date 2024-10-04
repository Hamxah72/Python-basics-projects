from tkinter import *
from PIL import ImageTk, Image

# Initialize the root window
root = Tk()
root.title("Hamxah")
root.geometry("800x600")

# Open image
my_pic = Image.open("/home/hamza/Pictures/IG_SShorts/JO.png")

# Resize image
resized = my_pic.resize((300, 225), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

# Create and pack the label with the image
my_label = Label(root, image=new_pic)
my_label.pack(pady=20)

# Run the main loop
root.mainloop()
