#!/usr/bin/python3
import matplotlib
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sys import platform as sys_pf

from row_pygubu.row_pygubu import RowPygubuUiApp
from row_pygubu.axeschoosewidgetsframe import AxesChooseWidgetsFrameWidget

from surcouches_pygubu.autowidgetsframe import AutoWidgetsFrame
from surcouches_pygubu.mainaxewidgetsframewidget import MainAxeWidgetsFrameWidget

from dico_params import dico_param_figure, dico_param_axe, dico_param_line


class View(RowPygubuUiApp):
    # Initialisation

    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.rinit()
        self.menu_initiator()

    def rinit(self):
        self.widgets_dico = {}

        self.MainNoteBook.rowconfigure(0, weight=1)
        self.MainNoteBook.columnconfigure(0, weight=1)

        for child in self.MainNoteBook.tabs():
            self.MainNoteBook.forget(child)

        self.figure_widgets = AutoWidgetsFrame(self.MainNoteBook)
        self.MainNoteBook.add(self.figure_widgets, text="Figure")

        self.axes_choose_widget = AxesChooseWidgetsFrameWidget(self.MainNoteBook)
        self.MainNoteBook.add(self.axes_choose_widget, text="Axes")

    def second_layer_init(self, fig):
        self.update_button.configure(command=self.controller.update_button_event)
        self.refresh_canvas(fig)
        self.menu_Fichier.add_command(label="Ouvrir", command=self.controller.open)
        self.menu_Fichier.add_command(
            label="Enregister sous", command=self.controller.save_as
        )
        self.menu_Fichier.add_command(label="Quitter", command=self.controller.quit)
        self.add_axes_and_lines_options()
        self.add_auto_widgets(
            fig, self.controller.model.axes, self.controller.model.lines
        )
        self.add_special_widgets()

    def menu_initiator(self):
        self.menu_Bar = tk.Menu(self.main_frame)

        # Menu principaux
        self.menu_Fichier = tk.Menu(self.menu_Bar)

        # affichage
        self.menu_Bar.add_cascade(label="Fichier", menu=self.menu_Fichier)

        self.main_frame.config(menu=self.menu_Bar)

    # Reset View

    def full_reset(self):
        self.rinit()
        self.add_axes_and_lines_options()
        self.add_auto_widgets(
            self.controller.model.fig,
            self.controller.model.axes,
            self.controller.model.lines,
        )
        self.add_special_widgets()
        self.refresh_canvas(self.controller.model.fig)

    def add_axes_and_lines_options(self):
        options_list = []
        self.axe_widgets_list = []
        self.line_widgets_list = []
        for row in range(len(self.controller.model.axes)):
            self.axe_widgets_list.append([])
            self.line_widgets_list.append([])
            for col in range(len(self.controller.model.axes[row])):
                options_list.append(str((row, col)))
                self.axe_widgets_list[row].append(
                    MainAxeWidgetsFrameWidget(self.axes_choose_widget.main_axe_frame)
                )

                self.axe_widgets_list[row][col].auto_widgets_widget = AutoWidgetsFrame(
                    self.axe_widgets_list[row][col].axe_settings_frame
                )
                self.axe_widgets_list[row][col].grid(column=0, row=0)
                self.axe_widgets_list[row][col].grid_remove()

                self.line_widgets_list[row].append([])
                current_line_options = []
                for line_index in range(len(self.controller.model.lines[row][col])):
                    self.line_widgets_list[row][col].append(
                        AutoWidgetsFrame(
                            self.axe_widgets_list[row][col].line_settings_frame
                        )
                    )
                    self.line_widgets_list[row][col][line_index].grid(column=0, row=0)
                    self.line_widgets_list[row][col][line_index].grid_remove()
                    current_line_options.append(str(line_index))
                self.axe_widgets_list[row][col].choose_line_combo.configure(
                    values=current_line_options
                )
                self.axe_widgets_list[row][col].choose_line_combo.bind(
                    "<<ComboboxSelected>>",
                    (lambda rowa, cola: lambda *args: self.choose_line(rowa, cola))(
                        row, col
                    ),
                )

        self.axes_choose_widget.choose_axes_combo.configure(values=options_list)
        self.axes_choose_widget.choose_axes_combo.bind(
            "<<ComboboxSelected>>",
            self.choose_axe,
        )

    def add_auto_widgets(self, fig, axes, lines):
        self.add_figure_autowidgets(fig)
        self.add_axes_autowidgets(axes)
        self.add_lines_autowidgets(lines)

    def add_figure_autowidgets(self, fig):
        fig_properties = fig.properties()
        for param in dico_param_figure.keys():
            try:
                fig_properties[param]
            except:
                print(param, " NOT FOUND IN FIGURE PROPERTIES")
                continue

            if dico_param_figure[param]["widget_type"] != "combobox":
                self.figure_widgets.add_widget(
                    dico_param_figure[param]["widget_type"],
                    param,
                    param,
                    fig_properties[param],
                )
            else:
                self.figure_widgets.add_widget(
                    dico_param_figure[param]["widget_type"],
                    param,
                    param,
                    fig_properties[param],
                    combo_options=dico_param_figure[param]["combo_options"],
                )

    def add_axes_autowidgets(self, axes):
        for row in range(len(axes)):
            for col in range(len(axes[row])):
                axe_properties = axes[row][col].properties()
                for param in dico_param_axe.keys():
                    try:
                        axe_properties[param]
                    except:
                        print(param, " NOT FOUND IN AXES PROPERTIES")
                        continue

                    if dico_param_axe[param]["widget_type"] != "combobox":
                        self.axe_widgets_list[row][col].auto_widgets_widget.add_widget(
                            dico_param_axe[param]["widget_type"],
                            param,
                            param,
                            axe_properties[param],
                        )
                    else:
                        self.axe_widgets_list[row][col].auto_widgets_widget.add_widget(
                            dico_param_axe[param]["widget_type"],
                            param,
                            param,
                            axe_properties[param],
                            combo_options=dico_param_axe[param]["combo_options"],
                        )

    def add_lines_autowidgets(self, lines):
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                for line_index in range(len(lines[row][col])):
                    line_properties = lines[row][col][line_index].properties()
                    for param in dico_param_line.keys():
                        try:
                            line_properties[param]
                        except:
                            print(param, " NOT FOUND IN LINES PROPERTIES")
                            continue

                        if dico_param_line[param]["widget_type"] != "combobox":
                            self.line_widgets_list[row][col][line_index].add_widget(
                                dico_param_line[param]["widget_type"],
                                param,
                                param,
                                line_properties[param],
                            )
                        else:
                            self.line_widgets_list[row][col][line_index].add_widget(
                                dico_param_line[param]["widget_type"],
                                param,
                                param,
                                line_properties[param],
                                combo_options=dico_param_line[param]["combo_options"],
                            )

    def add_special_widgets(self):
        self.special_widgets_dico = {"figure": {}, "axes": [], "lines": []}
        for row in range(len(self.controller.model.axes)):
            self.special_widgets_dico["axes"].append([])
            self.special_widgets_dico["lines"].append([])
            for col in range(len(self.controller.model.axes[row])):
                self.special_widgets_dico["axes"][row].append({})
                self.special_widgets_dico["lines"][row].append([])
                for line_index in range(len(self.controller.model.lines[row][col])):
                    self.special_widgets_dico["lines"][row][col].append({})

        self.add_figure_suptitle_widget()
        self.add_grid_visible_widget()
        self.add_legend_visible_widget()
        self.add_legend_anchor_widget()

    def add_figure_suptitle_widget(self):
        initial_suptitle = self.controller.model.get_figure_suptitle()
        self.figure_widgets.add_widget(
            "entry", "suptitle", "suptitle", initial_suptitle
        )
        self.special_widgets_dico["figure"]["suptitle"] = {
            "widget": self.figure_widgets.widgets_dico["suptitle"],
            "func": lambda widget_value: self.controller.model.set_suptitle(
                widget_value
            ),
            "property_name": "suptitle",
        }

    def add_grid_visible_widget(self):
        for row in range(len(self.axe_widgets_list)):
            for col in range(len(self.axe_widgets_list[row])):
                initial_grid = self.controller.model.get_grid_visible(row, col)
                self.axe_widgets_list[row][col].auto_widgets_widget.add_widget(
                    "checkbutton", "grid_visible", "grid_visible", initial_grid
                )
                self.special_widgets_dico["axes"][row][col]["grid_visible"] = {
                    "widget": self.axe_widgets_list[row][
                        col
                    ].auto_widgets_widget.widgets_dico["grid_visible"],
                    "func": (
                        lambda rowi, coli: (
                            lambda widget_value: self.controller.model.set_grid_visible(
                                rowi, coli, widget_value
                            )
                        )
                    )(row, col),
                    "property_name": "grid_visible",
                }

    def add_legend_anchor_widget(self):
        for row in range(len(self.axe_widgets_list)):
            for col in range(len(self.axe_widgets_list[row])):
                self.axe_widgets_list[row][col].auto_widgets_widget.add_widget(
                    "combobox",
                    "legend_anchor",
                    "legend_anchor",
                    "best",
                    combo_options=[
                        "best",
                        "upper right",
                        "upper left",
                        "lower left",
                        "lower right",
                        "right",
                        "center left",
                        "center right",
                        "lower center",
                        "upper center",
                        "center",
                    ],
                )
                self.special_widgets_dico["axes"][row][col]["legend_anchor"] = {
                    "widget": self.axe_widgets_list[row][
                        col
                    ].auto_widgets_widget.widgets_dico["legend_anchor"],
                    "func": (
                        lambda rowi, coli: (
                            lambda widget_value: self.controller.model.set_legend_anchor(
                                rowi, coli, widget_value
                            )
                        )
                    )(row, col),
                    "property_name": "legend_anchor",
                }

    def add_legend_visible_widget(self):
        for row in range(len(self.axe_widgets_list)):
            for col in range(len(self.axe_widgets_list[row])):
                initial_legend = self.controller.model.get_legend_visible(row, col)
                self.axe_widgets_list[row][col].auto_widgets_widget.add_widget(
                    "checkbutton", "legend_visible", "legend_visible", initial_legend
                )
                self.special_widgets_dico["axes"][row][col]["legend_visible"] = {
                    "widget": self.axe_widgets_list[row][
                        col
                    ].auto_widgets_widget.widgets_dico["legend_visible"],
                    "func": (
                        lambda rowi, coli: (
                            lambda widget_value: self.controller.model.set_legend_visible(
                                rowi, coli, widget_value
                            )
                        )
                    )(row, col),
                    "property_name": "legend_visible",
                }

    # Updates

    def refresh_canvas(self, fig):
        try:
            self.fig_canvas.get_tk_widget().destroy()
        except:
            pass
        self.fig_canvas = FigureCanvasTkAgg(fig, master=self.main_frame)
        try:
            self.fig_canvas.draw()
        except ValueError:
            print("Erreur dans les paramètres entrés")
            return
        except:
            print("Unknown error")
            return
        self.fig_canvas.get_tk_widget().grid(column=0, row=0, sticky="nsew")
        self.fig_canvas.get_tk_widget().rowconfigure(0, weight=1)
        self.fig_canvas.get_tk_widget().columnconfigure(0, weight=1)
        self.fig_canvas.get_tk_widget().grid(
            column=0, pady=5, row=0, rowspan=3, sticky="nsew"
        )
        self.fig_canvas.get_tk_widget().rowconfigure(0, weight=1)
        self.fig_canvas.get_tk_widget().columnconfigure(0, weight=1)
        print("Canvas refreshed")

    def choose_axe(self, *args):
        axe_tupple = tuple(
            map(
                int,
                self.axes_choose_widget.choose_axes_combo.get()
                .replace("(", "")
                .replace(")", "")
                .split(", "),
            )
        )
        for row in range(len(self.axe_widgets_list)):
            for col in range(len(self.axe_widgets_list[row])):
                self.axe_widgets_list[row][col].grid_remove()
        self.axe_widgets_list[axe_tupple[0]][axe_tupple[1]].grid(
            column=0, row=0, columnspan=2
        )

    def choose_line(self, axe_row, axe_col):
        if self.axe_widgets_list[axe_row][axe_col].choose_line_combo.get() == "":
            return
        line_choice = int(
            self.axe_widgets_list[axe_row][axe_col].choose_line_combo.get()
        )

        for line_index in range(len(self.line_widgets_list[axe_row][axe_col])):
            self.line_widgets_list[axe_row][axe_col][line_index].grid_remove()
        self.line_widgets_list[axe_row][axe_col][line_choice].grid(column=0, row=0)

    def run(self):
        self.main_frame.mainloop()


if sys_pf == "darwin":
    matplotlib.use("TkAgg")

if __name__ == "__main__":
    app = View("fake_contro")
    app.run()
