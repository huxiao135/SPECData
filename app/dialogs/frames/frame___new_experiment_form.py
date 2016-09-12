# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_experiment_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1054, 732)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgba(98, 98, 98, 247)\n"
""))
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 60, 451, 581))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.new_experiment_title_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.new_experiment_title_lbl.setFont(font)
        self.new_experiment_title_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Droid Sans\";"))
        self.new_experiment_title_lbl.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_experiment_title_lbl.setObjectName(_fromUtf8("new_experiment_title_lbl"))
        self.verticalLayout_2.addWidget(self.new_experiment_title_lbl)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.exp_author_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.exp_author_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.exp_author_lbl.setFrameShadow(QtGui.QFrame.Raised)
        self.exp_author_lbl.setLineWidth(22)
        self.exp_author_lbl.setObjectName(_fromUtf8("exp_author_lbl"))
        self.verticalLayout_3.addWidget(self.exp_author_lbl)
        self.author_txt = QtGui.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.author_txt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.author_txt.setStyleSheet(_fromUtf8("color: rgb(48, 48, 48);\n"
"background-color: rgb(255, 255, 255);"))
        self.author_txt.setObjectName(_fromUtf8("author_txt"))
        self.verticalLayout_3.addWidget(self.author_txt)
        self.exp_name_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.exp_name_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.exp_name_lbl.setObjectName(_fromUtf8("exp_name_lbl"))
        self.verticalLayout_3.addWidget(self.exp_name_lbl)
        self.name_txt = QtGui.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.name_txt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.name_txt.setStyleSheet(_fromUtf8("color: rgb(48, 48, 48);\n"
"background-color: rgb(255, 255, 255);"))
        self.name_txt.setObjectName(_fromUtf8("name_txt"))
        self.verticalLayout_3.addWidget(self.name_txt)
        self.exp_composition_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.exp_composition_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exp_composition_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.exp_composition_lbl.setObjectName(_fromUtf8("exp_composition_lbl"))
        self.verticalLayout_3.addWidget(self.exp_composition_lbl)
        self.composition_txt = QtGui.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.composition_txt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.composition_txt.setStyleSheet(_fromUtf8("color: rgb(48, 48, 48);\n"
"background-color: rgb(255, 255, 255);"))
        self.composition_txt.setObjectName(_fromUtf8("composition_txt"))
        self.verticalLayout_3.addWidget(self.composition_txt)
        self.exp_select_file_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.exp_select_file_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.exp_select_file_lbl.setObjectName(_fromUtf8("exp_select_file_lbl"))
        self.verticalLayout_3.addWidget(self.exp_select_file_lbl)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.select_file_txt = QtGui.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.select_file_txt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.select_file_txt.setStyleSheet(_fromUtf8("color: rgb(48, 48, 48);\n"
"background-color: rgb(255, 255, 255);"))
        self.select_file_txt.setObjectName(_fromUtf8("select_file_txt"))
        self.horizontalLayout.addWidget(self.select_file_txt)
        self.select_file_btn = QtGui.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_btn.sizePolicy().hasHeightForWidth())
        self.select_file_btn.setSizePolicy(sizePolicy)
        self.select_file_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.select_file_btn.setSizeIncrement(QtCore.QSize(0, 0))
        self.select_file_btn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(195, 195, 195);\n"
"font: 10pt \"Droid Sans\";"))
        self.select_file_btn.setObjectName(_fromUtf8("select_file_btn"))
        self.horizontalLayout.addWidget(self.select_file_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.exp_filetype_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.exp_filetype_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.exp_filetype_lbl.setObjectName(_fromUtf8("exp_filetype_lbl"))
        self.horizontalLayout_6.addWidget(self.exp_filetype_lbl)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.filetype_checkbox = QtGui.QVBoxLayout()
        self.filetype_checkbox.setObjectName(_fromUtf8("filetype_checkbox"))
        self.peak_type_rbtn = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.peak_type_rbtn.setEnabled(True)
        self.peak_type_rbtn.setObjectName(_fromUtf8("peak_type_rbtn"))
        self.filetype_checkbox.addWidget(self.peak_type_rbtn)
        self.full_type_rbtn = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.full_type_rbtn.setEnabled(True)
        self.full_type_rbtn.setObjectName(_fromUtf8("full_type_rbtn"))
        self.filetype_checkbox.addWidget(self.full_type_rbtn)
        self.horizontalLayout_2.addLayout(self.filetype_checkbox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.analysis_options_title_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.analysis_options_title_lbl.setFont(font)
        self.analysis_options_title_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Droid Sans\";"))
        self.analysis_options_title_lbl.setObjectName(_fromUtf8("analysis_options_title_lbl"))
        self.verticalLayout_2.addWidget(self.analysis_options_title_lbl)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        spacerItem3 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.choose_layout = QtGui.QVBoxLayout()
        self.choose_layout.setObjectName(_fromUtf8("choose_layout"))
        self.analyse_with_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.analyse_with_lbl.setWhatsThis(_fromUtf8(""))
        self.analyse_with_lbl.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.analyse_with_lbl.setObjectName(_fromUtf8("analyse_with_lbl"))
        self.choose_layout.addWidget(self.analyse_with_lbl)
        self.local_chk = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.local_chk.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 10pt \"Droid Sans\";"))
        self.local_chk.setObjectName(_fromUtf8("local_chk"))
        self.choose_layout.addWidget(self.local_chk)
        self.hitran_chk = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.hitran_chk.setEnabled(False)
        self.hitran_chk.setObjectName(_fromUtf8("hitran_chk"))
        self.choose_layout.addWidget(self.hitran_chk)
        self.splatlog_chk = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.splatlog_chk.setEnabled(False)
        self.splatlog_chk.setObjectName(_fromUtf8("splatlog_chk"))
        self.choose_layout.addWidget(self.splatlog_chk)
        self.verticalLayout_2.addLayout(self.choose_layout)
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.analyze_btn = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.analyze_btn.setAutoFillBackground(False)
        self.analyze_btn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);"))
        self.analyze_btn.setCheckable(False)
        self.analyze_btn.setAutoDefault(True)
        self.analyze_btn.setDefault(False)
        self.analyze_btn.setFlat(False)
        self.analyze_btn.setObjectName(_fromUtf8("analyze_btn"))
        self.gridLayout.addWidget(self.analyze_btn, 0, 2, 1, 1)
        self.back_btn = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DEC Terminal"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.back_btn.setFont(font)
        self.back_btn.setAutoFillBackground(False)
        self.back_btn.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);"))
        self.back_btn.setCheckable(False)
        self.back_btn.setAutoDefault(True)
        self.back_btn.setDefault(False)
        self.back_btn.setFlat(False)
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.gridLayout.addWidget(self.back_btn, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(266, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayoutWidget_2.raise_()
        self.new_experiment_title_lbl.raise_()
        self.exp_author_lbl.raise_()
        self.new_experiment_title_lbl.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.new_experiment_title_lbl.setText(_translate("Dialog", "Experiment Information", None))
        self.exp_author_lbl.setText(_translate("Dialog", "Author", None))
        self.exp_name_lbl.setText(_translate("Dialog", "Name", None))
        self.exp_composition_lbl.setText(_translate("Dialog", "Composition", None))
        self.exp_select_file_lbl.setText(_translate("Dialog", "Select  File", None))
        self.select_file_btn.setText(_translate("Dialog", "...", None))
        self.exp_filetype_lbl.setText(_translate("Dialog", "File Type:", None))
        self.peak_type_rbtn.setText(_translate("Dialog", "Peak File", None))
        self.full_type_rbtn.setText(_translate("Dialog", "Full Spectrum", None))
        self.analysis_options_title_lbl.setText(_translate("Dialog", "Analysis Options", None))
        self.analyse_with_lbl.setText(_translate("Dialog", "Analyze with:", None))
        self.local_chk.setText(_translate("Dialog", "Local Database", None))
        self.hitran_chk.setText(_translate("Dialog", "HITRAN (unavailable)", None))
        self.splatlog_chk.setText(_translate("Dialog", "SplatLog (unavailable)", None))
        self.analyze_btn.setText(_translate("Dialog", "Analyze", None))
        self.back_btn.setText(_translate("Dialog", "Back to Main", None))
