from setuptools import setup, find_packages

VERSION = "0.0.6"
DESCRIPTION = "Application pour modifier l'esthétique d'un graphique matplotlib"
LONG_DESCRIPTION = "Projet Figure S2 MPCI ayant pour but le développement d'une interface graphique permettant d'intéragir ergonomiquement avec des figures matplotlib"

# Setting up
setup(
    name="GuiMPLpretest",
    version=VERSION,
    author="Groupe Figure MPCI",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages()
    + find_packages(where="./row_pygubu")
    + find_packages(where="./surcouches_pygubu")
    + find_packages(where="./custom_widgets"),
    install_requires=["matplotlib"],
    keywords=["matplotlib", "graphique", "interface graphique", "python", "figures"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
