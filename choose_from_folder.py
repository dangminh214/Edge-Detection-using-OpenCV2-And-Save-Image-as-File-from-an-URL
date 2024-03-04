import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

image = None

def choose_image():
    global image  # using image as global
    # open dialog to choose image
    file_path = filedialog.askopenfilename()

    if file_path: 

        # check if user has already selected       
        image = cv2.imread(file_path) 
        if image is not None:
            height, width, _ = image.shape
            if (height < 800 and width < 800):
                new_width = int(width * 1.5)
                new_height = int(height * 1.5)
            elif (height > 1000 and width > 1000):
                new_width = int(width * 0.5)
                new_height = int(height * 0.5)
            else: 
                new_width = width
                new_height = height

            image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
            print('width: ', new_width, 'heigth: ', new_height)
            print('path: ', file_path)
            face_detect(image)

        else:
            print("No image was selected.")
            show_popup('Fail', 'No image was selected.')
            root.quit()
            return None
     
    def show_popup(title, content):
        # show the pop up
        messagebox.showinfo(title, content)

    root = tk.Tk()
    root.withdraw() # folder pop down
    root.geometry("800x600")

    # pop up the warning, choose legit images
    show_popup("Warning", "Name of image contains only legit character, please don't use some special names")

