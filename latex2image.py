#!/usr/bin/env python3

import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import os
import matplotlib
import matplotlib.mathtext as mt
import matplotlib.font_manager as fm
from PIL import Image, ImageTk


# 初始化
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "latex2image.ui"
TEMP_IMG = PROJECT_PATH / "formula.png"

os.chdir(PROJECT_PATH)

    
def convertor(latex: str):
    mt.math_to_image(f"${latex}$", TEMP_IMG, dpi=300, format="png")
    
    tk_img = ImageTk.PhotoImage(Image.open(TEMP_IMG))
    return tk_img


class Latex2ImageApp:
    def __init__(self, master=None):
        # Create a builder and setup resources path (if you have images)
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        # Load a ui file
        builder.add_from_file(PROJECT_UI)

        # Create the mainwindow
        self.mainwindow = builder.get_object('toplevel1', master)

        # Connect callbacks
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event):
        text = self.builder.get_object('text1').get('1.0', 'end-1c')
        latex_img = convertor(text)
        canvas = self.builder.get_object('canvas1')
        canvas.delete(tk.ALL)
        canvas.create_image(10, 10, image=latex_img, anchor="nw")
        

if __name__ == '__main__':
    app = Latex2ImageApp()
    app.run()
