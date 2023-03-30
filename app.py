import tkinter as tk
from tkinter import filedialog
import tkinter.font as font
import os
from pdf2docx import Converter

root = tk.Tk()
root.title("PDf To Word Converter")

def add_file():
    file_path = filedialog.askopenfilename(initialdir="/" , title = "Choose File To convert")
    convert_file(file_path)


def convert_file(file_path):
    save_location = r"D:\Anshika 2\PDF To Word\CovertedDocument.docx"
    cv = Converter(file_path)
    cv.convert(save_location, start=0, end=None)
    cv.close()
    success_text = tk.Label(frame, text="Conversion successful!!", font = (16), bg = "#F4C2C2")
    success_text.pack()


canvas = tk.Canvas(root, height=500, width=700)
canvas.pack()


frame = tk.Frame(root, bg = "#F4C2C2")

frame.place(relwidth = .8, relheight = .8, relx = .1, rely = .1)


button = tk.Button(frame, text = "SELCT FILE" , padx = 500 , pady = 50, bg = "#E75480", fg = "#F4C2C2" , command = add_file )

button_font = font.Font(size = 35)

button["font"] = button_font

button.pack()

root.mainloop()