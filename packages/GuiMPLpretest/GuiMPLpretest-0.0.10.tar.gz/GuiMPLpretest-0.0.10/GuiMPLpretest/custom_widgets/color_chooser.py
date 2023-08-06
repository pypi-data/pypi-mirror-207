import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser


class ColorChooser:
    def __init__(self, button_master):
        self.button = ttk.Button(button_master, command=self.color_choice, text="X")
        self.color_var = tk.StringVar()

    def color_choice(self):
        color = colorchooser.askcolor()
        if color == None:
            return
        self.color_var.set(color[-1])

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def get(self):
        return self.color_var.get()

    def set_value(self, value: str = "#1f77b4"):
        self.color_var.set(value)

    def get_var(self):
        return self.color_var
