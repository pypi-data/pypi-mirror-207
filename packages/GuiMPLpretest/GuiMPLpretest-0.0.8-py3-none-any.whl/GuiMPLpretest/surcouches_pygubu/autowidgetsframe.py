import tkinter as tk
import tkinter.ttk as ttk

from GuiMPLpretest.row_pygubu.autowidgets_base_frame import AutowidgetsBaseFrameWidget
from GuiMPLpretest.custom_widgets.color_chooser import ColorChooser
from GuiMPLpretest.custom_widgets.double_spinbox import DoubleSpinbox


class AutoWidgetsFrame(AutowidgetsBaseFrameWidget):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.next_widget_row = 0
        self.widgets_dico = {}

    def get_widget_value_from_property_name(self, property_name):
        try:
            widget_data = self.widgets_dico[property_name]
        except:
            print(self.widgets_dico.keys())
            return

        match widget_data["widget_type"]:
            case "entry":
                return widget_data["widget"].get()
            case "checkbutton":
                return widget_data["widget"].instate(["selected"])
            case "combobox":
                return widget_data["widget"].get()
            case "spinbox":
                return float(widget_data["widget"].get())
            case "colorchooser":
                return widget_data["widget"].get()
            case "doublespinbox":
                return widget_data["widget"].get()
            case _:
                return

    # Create a new widget

    def add_widget(
        self,
        widget_type,
        widget_property_name,
        widget_name,
        initial_value,
        combo_options=None,
    ):
        label = self.get_next_label(widget_name)

        match widget_type:
            case "entry":
                widget, var = self.get_an_entry(initial_value)
                widget.insert(0, initial_value)
            case "checkbutton":
                widget, var = self.get_a_checkbutton()
                if initial_value:
                    widget.invoke()
                else:
                    widget.invoke()
                    widget.invoke()
            case "combobox":
                widget, var = self.get_a_combobox()
                widget.configure(values=combo_options)
                widget.set(initial_value)
            case "spinbox":
                widget, var = self.get_a_spinbox()
                widget.set(initial_value)
            case "colorchooser":
                widget, var = self.get_a_colorchooser()
                widget.set_value(initial_value)
            case "doublespinbox":
                widget, var = self.get_a_doublespinbox()
                widget.set_value(initial_value)
            case _:
                return

        widget.grid(column=1, row=self.next_widget_row, sticky="ew")

        self.widgets_dico[widget_property_name] = {
            "widget": widget,
            "label": label,
            "widget_type": widget_type,
            "widget_name": widget_name,
            "widget_var": var,
        }
        self.next_widget_row += 1

    def get_next_label(self, label_text):
        label = ttk.Label(self)
        label.configure(text=label_text)
        label.grid(column=0, row=self.next_widget_row, sticky="ew")
        return label

    def get_a_checkbutton(self):
        checkbutton = ttk.Checkbutton(self)
        checkbutton_var = tk.BooleanVar()
        checkbutton.configure(
            textvariable=checkbutton_var, onvalue=True, offvalue=False
        )
        return checkbutton, checkbutton_var

    def get_an_entry(self, initial_value):
        entry = ttk.Entry(self)
        entry_var = tk.StringVar(value=initial_value)
        entry.configure(textvariable=entry_var)
        return entry, entry_var

    def get_a_combobox(self):
        combobox = ttk.Combobox(self)
        combobox_var = tk.StringVar()
        combobox.configure(textvariable=combobox_var)
        return combobox, combobox_var

    def get_a_spinbox(self):
        spinbox = ttk.Spinbox(self)
        spinbox_var = tk.DoubleVar()
        spinbox.configure(
            textvariable=spinbox_var,
            increment=1.0,
            from_=float("-inf"),
            to=float("inf"),
        )
        return spinbox, spinbox_var

    def get_a_colorchooser(self):
        colorchooser = ColorChooser(self)
        var = colorchooser.get_var()
        return colorchooser, var

    def get_a_doublespinbox(self):
        doublespinbox = DoubleSpinbox(self)
        var = doublespinbox.get_var()
        return doublespinbox, var
