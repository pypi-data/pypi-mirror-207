from view import View
from model import Model
from tkinter import filedialog
import os
import pickle
from matplotlib.figure import Figure

from dico_params import dico_param_figure, dico_param_axe, dico_param_line


class Controller:
    def __init__(self, fig: Figure = None, fig_file_name: str = None):
        self.model = Model()
        self.view = View(self)
        self.data_set_list = []
        self.view.second_layer_init(self.model.fig)
        if fig != None:
            try:
                self.open_fig(fig)
            except:
                print("Erreur lors de l'ouverture de la figure")
        elif fig_file_name != None:
            try:
                self.open_pickle(fig_file_name)
            except:
                print("Erreur lors de l'ouverture de la figure")

    # Update functions

    def update_button_event(self):
        print("Update Event")

        self.sync_autowidgets_lines()
        self.sync_autowidgets_axes()
        self.sync_autowidgets_figure()

        self.sync_special_widgets_lines()
        self.sync_special_widgets_axes()
        self.sync_special_widgets_figure()

        self.view.refresh_canvas(self.model.fig)

    def sync_autowidgets_figure(self):
        fig_prop = {}

        for param in dico_param_figure:
            fig_prop[
                param
            ] = self.view.figure_widgets.get_widget_value_from_property_name(param)

        self.model.update_figure(fig_prop)

    def sync_autowidgets_axes(self):
        for row in range(len(self.model.axes)):
            for col in range(len(self.model.axes[row])):
                axe_prop = {}
                for param in dico_param_axe:
                    axe_prop[param] = self.view.axe_widgets_list[row][
                        col
                    ].auto_widgets_widget.get_widget_value_from_property_name(param)
                self.model.update_axe(row, col, axe_prop)

    def sync_autowidgets_lines(self):
        for row in range(len(self.model.lines)):
            for col in range(len(self.model.lines[row])):
                for line_index in range(len(self.model.lines[row][col])):
                    line_prop = {}
                    for param in dico_param_line:
                        line_prop[param] = self.view.line_widgets_list[row][col][
                            line_index
                        ].get_widget_value_from_property_name(param)
                    self.model.update_line(row, col, line_index, line_prop)

    def sync_special_widgets_lines(self):
        for row in range(len(self.view.special_widgets_dico["lines"])):
            for col in range(len(self.view.special_widgets_dico["lines"][row])):
                for line_index in range(
                    len(self.view.special_widgets_dico["lines"][row][col])
                ):
                    for key in self.view.special_widgets_dico["lines"][row][col][
                        line_index
                    ].keys():
                        widget_value = self.view.axe_widgets_list[row][col][
                            line_index
                        ].get_widget_value_from_property_name(
                            self.view.special_widgets_dico["lines"][row][col][
                                line_index
                            ][key]["property_name"]
                        )
                        self.view.special_widgets_dico["lines"][row][col][line_index][
                            key
                        ]["func"](widget_value)

    def sync_special_widgets_axes(self):
        for row in range(len(self.view.special_widgets_dico["axes"])):
            for col in range(len(self.view.special_widgets_dico["axes"][row])):
                for key in self.view.special_widgets_dico["axes"][row][col].keys():
                    widget_value = self.view.axe_widgets_list[row][
                        col
                    ].auto_widgets_widget.get_widget_value_from_property_name(
                        self.view.special_widgets_dico["axes"][row][col][key][
                            "property_name"
                        ]
                    )
                    self.view.special_widgets_dico["axes"][row][col][key]["func"](
                        widget_value
                    )

    def sync_special_widgets_figure(self):
        for key in self.view.special_widgets_dico["figure"].keys():
            widget_value = self.view.figure_widgets.get_widget_value_from_property_name(
                self.view.special_widgets_dico["figure"][key]["property_name"]
            )
            self.view.special_widgets_dico["figure"][key]["func"](widget_value)

    # Menu functions

    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            filetypes=[
                ("PDF", ".pdf"),
                ("PNG", ".png"),
                ("JPG", ".jpg"),
                ("PICKLE", ".pickle"),
            ],
            defaultextension=".pickle",
        )
        filename, file_extension = os.path.splitext(file_path)
        if file_extension == ".pickle":
            pickle.dump(self.model.fig, open(file_path, "wb"))
        else:
            self.model.fig.savefig(file_path)

    def open(self):
        fic_path = filedialog.askopenfilename()

        filename, file_extension = os.path.splitext(fic_path)

        if file_extension == ".pickle":
            self.open_pickle(fic_path)
        else:
            print("Extension inconnue")

    def open_pickle(self, fic_path):
        fig_handle = pickle.load(open(fic_path, "rb"))
        self.open_fig(fig_handle)

    def open_fig(self, fig: Figure):
        self.model.set_new_fig(fig)
        self.view.full_reset()
        self.update_button_event()

    def quit(self):
        self.view.main_frame.quit()
        self.view.main_frame.destroy()

    def run(self):
        print("Starting UI")
        self.view.run()
