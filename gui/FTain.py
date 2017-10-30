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
        self.ui = uic.loadUi(os.path.join('/home/wanghao/', "ftt.ui"), self)

        # Property Editor
        # self.property_editor = PropertyEditor(config.LABELS)
        # self.ui.dockProperties.setWidget(self.property_editor)

        # Scene

        # SceneView

        # give functions as lambdas, or else they will be called with a bool as parameter
        # self.controls.back_button.clicked.connect(lambda lt: self.labeltool.gotoPrevious())
        # self.controls.forward_button.clicked.connect(lambda lt: self.labeltool.gotoNext())
        #
        # self.ui.dockAnnotations.setWidget(self.treeview)
        #
        # self.scene.selectionChanged.connect(self.scene.onSelectionChanged)
        # self.treeview.selectedItemsChanged.connect(self.scene.onSelectionChangedInTreeView)


        # View menu
        # self.ui.menu_Views.addAction(self.ui.dockProperties.toggleViewAction())
        # self.ui.menu_Views.addAction(self.ui.dockAnnotations.toggleViewAction())

        # Annotation menu

        # Show the UI.  It is important that this comes *after* the above
        # adding of custom widgets, especially the central widget.  Otherwise the
        # dock widgets would be far to large.
        self.ui.show()

        ## connect action signals
        self.connectActions()


        ## File menu
        # self.ui.actionNew.triggered.connect(self.fileNew)
        # self.ui.actionOpen.triggered.connect(self.fileOpen)
        # self.ui.actionSave.triggered.connect(self.fileSave)
        # self.ui.actionSave_As.triggered.connect(self.fileSaveAs)
        # self.ui.actionExit.triggered.connect(self.close)

    def connectActions(self):
        self.ui.btn_start.clicked.connect(self.slots_btn_start_train)
        pass

    def slots_btn_start_train(self):
        os.system('ls')
        pass
