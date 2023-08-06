from matplotlib.figure import Figure
import pickle

from GuiMPLpretest.controller import Controller


def from_fig(fig: Figure = None):
    contro = Controller(fig=fig)
    contro.run()


def export_fig(fig: Figure, file_name: str):
    try:
        pickle.dump(fig, open(file_name, "wb"))
    except:
        print("Erreur lors de l'enregistrement de la figure par pickle")


def from_file(file_name: str = None):
    contro = Controller(fig_file_name=file_name)
    contro.run()
