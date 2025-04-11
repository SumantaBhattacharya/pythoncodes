from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image paths
image_paths = [
    r"C:\Users\Sumanta Bhattacharya\Documents\chainsaw-man-6zhr96v1eo9fidla.jpg",
    r"C:\Users\Sumanta Bhattacharya\OneDrive\Pictures\13512a461869faea65ef1cd7bdef05de.jpg",
    r"C:\Users\Sumanta Bhattacharya\OneDrive\Pictures\Screenshots\WhatsApp Image 2023-12-08 at 16.16.43_b3a4b210.jpg",
    r"C:\Users\Sumanta Bhattacharya\Downloads\OMEN Sunago.jpg",
    r"C:\Users\Sumanta Bhattacharya\Downloads\logo.png.png"
]

# Resize the Images to 1080*1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]

# PIL MODULE - IMAGE - PHOTOIMAGE METHOD
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Label object which is tkinter label class that is used to display images or text in the GUI
label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

# ITERTOOLS MODULE - CYCLE() FUNCTION WHICH WILL HELP TO ITERATE IN THE LOOP OF THE IMAGES IN PHOTO_IMAGES
slideshow_cycle = cycle(photo_images)

def start_slideshow():
    for i in range(len(image_paths)):
        update_image()

# Create a play button
play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
