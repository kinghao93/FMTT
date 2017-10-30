# -*- coding: utf-8 -*-
# 扣件模型训练检测

import sys
from PyQt4 import QtGui
from gui.FTT import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ftt = MainWindow()
    sys.exit(app.exec_())