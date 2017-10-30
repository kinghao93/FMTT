# -*- coding: utf-8 -*-
import sys,os
from PyQt4.QtGui import QMainWindow, QSizePolicy, QWidget, QVBoxLayout, QAction, \
    QKeySequence, QLabel, QItemSelectionModel, QMessageBox, QFileDialog, QFrame, \
    QDockWidget, QProgressBar, QProgressDialog
from PyQt4.QtCore import SIGNAL, QSettings, QSize, QPoint, QVariant, QFileInfo, QTimer, pyqtSignal, QObject
import PyQt4.uic as uic

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupGui()

    ###
    ### GUI/Application setup
    ###___________________________________________________________________________________________
    def setupGui(self):
        self.ui = uic.loadUi(os.path.join('./gui/', "ftt.ui"), self)

        # Show the UI.  It is important that this comes *after* the above
        # adding of custom widgets, especially the central widget.  Otherwise the
        # dock widgets would be far to large.
        self.ui.show()

        ## connect action signals
        self.connectActions()

    def connectActions(self):
        self.ui.btn_start.clicked.connect(self.slots_btn_start_train)
        pass

    # slots
    def slots_btn_start_train(self):
        os.system('ls')
        pass
