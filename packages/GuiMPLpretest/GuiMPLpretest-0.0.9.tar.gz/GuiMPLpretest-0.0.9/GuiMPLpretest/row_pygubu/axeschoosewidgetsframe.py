#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class AxesChooseWidgetsFrameWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(AxesChooseWidgetsFrameWidget, self).__init__(master, **kw)
        self.choose_axes = ttk.Label(self)
        self.choose_axes.configure(text="Choose axe")
        self.choose_axes.grid(column=0, row=0, sticky="ew")
        self.choose_axes_combo = ttk.Combobox(self)
        self.choose_axes_var = tk.StringVar()
        self.choose_axes_combo.configure(textvariable=self.choose_axes_var)
        self.choose_axes_combo.grid(column=1, row=0, sticky="ew")
        self.main_axe_frame = ttk.Frame(self)
        self.main_axe_frame.configure(height=200, width=250)
        self.main_axe_frame.grid(column=0, columnspan=2, row=1, sticky="n")
        self.configure(height=200, width=200)
        self.grid(column=0, row=0, sticky="new")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    widget = AxesChooseWidgetsFrameWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
