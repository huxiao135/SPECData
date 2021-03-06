# Author: Jasmine Oliveira
# Date: 5/12/2017

from PyQt4.QtGui import *

from dialog___check_requirements import CheckRequirements
from dialog___wizard_window import WizardWindow


class WelcomeWindow(WizardWindow):
    def __init__(self):
        super(WelcomeWindow, self).__init__(False)

        self.header_txt = "Welcome to the SPECdata \nSetup Wizard"
        self.body_txt = "\n\nThis wizard will guide you through the installation of SPECdata. \n\n" \
                        "It is recommended that you read the README.txt or instructions listed on the" \
                        " Github Wiki before starting Setup. The appropriate python enviornment must be setup beforehand." \
                        "\n\n\n\n\n Click Next to continue, or Cancel to exit Setup."

        self.__setup_center_layout()
        self.__setup_buttons()
        self.show()

    def __setup_buttons(self):
        self.rightbtn.setText("Cancel")
        self.leftbtn.setText("Next")
        self.rightbtn.clicked.connect(self.close)
        self.leftbtn.clicked.connect(self.right_btn_action)

    def __setup_center_layout(self):
        # Setup header
        header_lbl = QLabel(self.header_txt)
        header_lbl.setMargin(1)
        header_lbl.setStyleSheet(self.header_font)
        header_lbl.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        header_lbl.setWordWrap(True)

        # Setup Body
        body_lbl = QLabel(self.body_txt)
        body_lbl.setWordWrap(True)
        body_lbl.setStyleSheet(self.body_font)
        # Spacer
        spacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)

        ###########################################
        # Add all to main layout
        ###########################################
        self.center_layout.addWidget(header_lbl, 0, 0)
        self.center_layout.addWidget(body_lbl, 1, 0)
        self.center_layout.addItem(spacer, 2, 0)
        self.center_layout.setSpacing(0)

    def right_btn_action(self):
        self.close()
        window = CheckRequirements()
        window.show()
        window.exec_()
