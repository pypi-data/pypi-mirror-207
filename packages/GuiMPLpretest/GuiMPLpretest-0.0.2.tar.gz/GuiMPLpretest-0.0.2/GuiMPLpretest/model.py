from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self.new_subplot()

    def new_subplot(self):
        self.fig = plt.figure(figsize=(2, 2))
        self.axes = self.fig.subplots(2, 2)
        self.lines_init()

    # Re-Initialisation de Model à l'ouverture d'une figure

    def set_new_fig(self, fig: Figure):
        self.fig = fig
        self.axes_init()
        self.lines_init()

    def axes_init(self):
        if len(self.fig.axes) == 0:
            self.axes = []
            return
        if type(self.fig.axes[0]) != type([]):
            self.axes = [self.fig.axes]
        else:
            self.axes = self.fig.axes

    def lines_init(self):
        if len(self.axes) == 0:
            self.lines = []
            return
        self.lines = []
        for row in range(len(self.axes)):
            self.lines.append([])
            for col in range(len(self.axes[row])):
                self.lines[row].append(self.axes[row][col].get_lines())

    # Update autowidgets functions

    def update_figure(self, properties):
        try:
            self.fig.update(properties)
        except:
            print("Paramètres de la figure invalides")

    def update_axe(self, row, col, properties):
        try:
            self.axes[row][col].update(properties)
        except:
            print("Paramètres de l'axe (" + str(row) + "," + str(col) + ") invalides")

    def update_line(self, row, col, line_index, properties):
        try:
            self.lines[row][col][line_index].update(properties)
        except:
            print(
                "Paramètres de la ligne",
                line_index,
                "de l'axe (" + str(row) + "," + str(col) + ") invalides",
            )

    # Special widgets functions

    def get_figure_suptitle(self):
        if self.fig._suptitle != None:
            return self.fig._suptitle.get_text()
        return ""

    def set_suptitle(self, title):
        self.fig.suptitle(title)

    def get_grid_visible(self, row, col):
        return self.axes[row][col].properties()["xgridlines"][0].properties()["visible"]

    def set_grid_visible(self, row, col, value):
        self.axes[row][col].grid(visible=value)

    def get_legend_visible(self, row, col):
        if self.axes[row][col].get_legend() == None:
            return False
        else:
            return self.axes[row][col].get_legend().get_visible()

    def set_legend_visible(self, row, col, value):
        if self.axes[row][col].get_legend() == None:
            if value:
                self.axes[row][col].legend()
        else:
            self.axes[row][col].get_legend().set_visible(value)

    def set_legend_anchor(self, row, col, value):
        initial_visible = self.get_legend_visible(row, col)
        self.axes[row][col].legend(loc=value)
        self.set_legend_visible(row, col, initial_visible)
