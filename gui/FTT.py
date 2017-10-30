# -*- coding: utf-8 -*-
import sys,os
import subprocess
from PyQt4.QtGui import QMainWindow, QSizePolicy, QWidget, QVBoxLayout, QAction, \
    QKeySequence, QLabel, QItemSelectionModel, QMessageBox, QFileDialog, QFrame, \
    QDockWidget, QProgressBar, QProgressDialog
from PyQt4.QtCore import QString, QStringList, SIGNAL, QSettings, QSize, QPoint, QVariant, QFileInfo, QTimer, pyqtSignal, QObject
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

        self.ui.cbb_weights.addItems(QStringList(['vgg16.ckpt',]))
        # self.ui.cbb_weights.addItem(QString('vgg16.ckpt1'))
        # Show the UI.  It is important that this comes *after* the above
        # adding of custom widgets, especially the central widget.  Otherwise the
        # dock widgets would be far to large.
        self.ui.show()

        ## connect action signals
        self.connectActions()

    def connectActions(self):
        self.ui.btn_start.clicked.connect(self.slots_btn_start_train)
        self.ui.btn_reset.clicked.connect(self.slots_btn_reset_train)
        pass

    # slots

    def slots_btn_start_train(self):
        # print(self.ui.cbb_weights.currentText())
        p = subprocess.Popen('ps aux', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # self.ui.plainTextEdit.setPlainText(self.ui.cbb_weights.currentText())
        self.ui.textEdit.setText(self.ui.cbb_weights.currentText())

        # p.stdout.readlines()
        for line in p.stdout.readlines():
            self.ui.textEdit.append(QString(line))
        self.ui.progressBar.setValue(100)

    def slots_btn_reset_train(self):
        self.ui.textEdit.clear()
        self.ui.progressBar.setValue(0)