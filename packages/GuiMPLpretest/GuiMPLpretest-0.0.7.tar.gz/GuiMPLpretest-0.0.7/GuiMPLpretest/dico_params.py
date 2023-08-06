dico_param_figure = {
    "figheight": {"widget_type": "spinbox"},
    "figwidth": {"widget_type": "spinbox"},
    "dpi": {"widget_type": "spinbox"},
}

dico_param_axe = {
    "visible": {"widget_type": "checkbutton"},
    "title": {"widget_type": "entry"},
    "xlabel": {"widget_type": "entry"},
    "ylabel": {"widget_type": "entry"},
    "xlim": {"widget_type": "doublespinbox"},
    "ylim": {"widget_type": "doublespinbox"},
    "axisbelow": {
        "widget_type": "combobox",
        "combo_options": ["True", "False", "line"],
    },
    "autoscale_on": {"widget_type": "checkbutton"},
    "autoscalex_on": {"widget_type": "checkbutton"},
    "autoscaley_on": {"widget_type": "checkbutton"},
    "adjustable": {"widget_type": "combobox", "combo_options": ["box", "datalim"]},
    "anchor": {
        "widget_type": "combobox",
        "combo_options": ["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
    },
}

dico_param_line = {
    "visible": {"widget_type": "checkbutton"},
    "label": {"widget_type": "entry"},
    "color": {"widget_type": "colorchooser"},
    "linestyle": {
        "widget_type": "combobox",
        "combo_options": ["-", "--", "-.", ":", ""],
    },
    "linewidth": {"widget_type": "spinbox"},
    "marker": {
        "widget_type": "combobox",
        "combo_options": [".", "o", "v", "^", "<", ">", "*", "x", "X", "None"],
    },
    "markerfacecolor": {"widget_type": "colorchooser"},
    "markeredgecolor": {"widget_type": "colorchooser"},
    "markersize": {"widget_type": "spinbox"},
    "markeredgewidth": {"widget_type": "spinbox"},
    "fillstyle": {
        "widget_type": "combobox",
        "combo_options": ["full", "left", "right", "bottom", "top", "none"],
    },
    "dash_capstyle": {
        "widget_type": "combobox",
        "combo_options": ["butt", "round", "projectile"],
    },
    "gapcolor": {"widget_type": "colorchooser"},
    "drawstyle": {
        "widget_type": "combobox",
        "combo_options": ["default", "steps", "steps-pre", "steps-mid", "steps-post"],
    },
}
