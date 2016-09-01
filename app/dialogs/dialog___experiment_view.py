# Author: Jasmine Oliveira
# Date: 08/24/2016

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib.backends.backend_qt4agg

#import matplotlib
#matplotlib.use("Agg")

from .frames.frame___experiment import Ui_Dialog
from .widget___molecule_selection import MoleculeSelectionWidget
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget
from .splash_screens import LoadingProgressScreen

from ..experiment_analysis import Graph
from functions import experiment
import pyqtgraph as pg

import time
import os


class ExperimentView(QDialog):

    def __init__(self, experiment_name, mid):
        super(ExperimentView, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Experiment View")

        # Widgets
        self.plot_widget = None
        self.matplot_widget = MatplotlibWidget()
        self.selection_widget = MoleculeSelectionWidget()
        self.redisplay_btn = QPushButton()
        # Data
        self.experiment = None
        self.loading_screen = None

        self.startup(experiment_name, mid)

    def startup(self, experiment_name, mid):
        self.loading_screen = LoadingProgressScreen()
        self.loading_screen.start()     # Start Loading Screen

        ## Do Things ##

        # Create Experiment
        self.loading_screen.set_caption('Creating experiment...')
        self.experiment = self.create_experiment(experiment_name, mid)  # Create experiment obj
        time.sleep(1)
        self.loading_screen.next_value(20)

        # Analyze Experiment
        self.loading_screen.set_caption('Analyzing...')
        self.do_analysis()                      # Run Analysis
        self.loading_screen.next_value(40)
        time.sleep(2)

        # Setup Layout
        self.loading_screen.set_caption('Setting up...')
        self.setup_layout()                     # Setup Layout
        self.loading_screen.next_value(60)

        # Add Assignments to Selection Widget
        self.add_selection_assignments()        # Add assignments
        time.sleep(2)
        self.loading_screen.next_value(80)

        # Graph Main Graph
        self.graph()                            # Graph
        self.loading_screen.next_value(90)
        time.sleep(2)

        self.loading_screen.end()

    def create_experiment(self, experiment_name, mid):
        return experiment.Experiment(experiment_name, mid)

    def do_analysis(self):
        self.experiment.get_assigned_molecules()

    def setup_layout(self):

        # Set a grid layout to manage widgets
        layout = QGridLayout()
        self.setLayout(layout)

        # Widgets
        self.matplot_widget = MatplotlibWidget()
        self.selection_widget = MoleculeSelectionWidget()
        self.redisplay_btn = QPushButton()

        self.redisplay_btn.setText("Redisplay")
        self.redisplay_btn.clicked.connect(self.redisplay_graph)

        #self.plot_widget = pg.PlotWidget(title="Experiment Peaks")
        #spacer1_widget = QSpacerItem()

        ## Add Widgets to layout
        layout.addWidget(self.selection_widget, 0,0)
        layout.addWidget(self.matplot_widget, 0, 1)
        layout.addWidget(self.redisplay_btn, 1,0)

        #layout.addWidget(spacer1_widget, 0, 1)
        #layout.addWidget(self.plot_widget, 0,1)

    def add_selection_assignments(self):
        # Set
        #self.selection_widget.add_all(self.experiment.get_assigned_names(), self.experiment.get_assigned_mids())
        self.selection_widget.add_all(self.experiment.molecule_matches.values())

    def graph(self):
        experiment_graph = Graph(self.matplot_widget, self.experiment)
        experiment_graph.add_subplot_experiment(211)
        matches, colors = self.selection_widget.get_selections()
        experiment_graph.add_subplot_selected_assignments(212, matches, colors)
        experiment_graph.draw()

    def connect_buttons(self):
        redisplay_btn = self.ui.redisplay_btn
        redisplay_btn.clicked.connect(self.redisplay_graph)

    def redisplay_graph(self):
        matches, colors = self.selection_widget.get_selections()
        self.matplot_widget = MatplotlibWidget()
        experiment_graph = Graph(self.matplot_widget, self.experiment)
        #experiment_graph.clear()
        experiment_graph.add_subplot_experiment(211)
        experiment_graph.add_subplot_selected_assignments(212, matches, colors)

        return True # do nothing