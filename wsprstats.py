#!/usr/bin/env python3
'''
WSPR Stats is a python project that displays statistics from a named amateur
radio station that is part of the WSPR reporting network.  WSPR (Weak Signal
Reporting System) is a beacon mode found on most HF ham bands.  For more information
try this address:  http://wsprnet.org/drupal/
This project work with collectwsprdata.sh.
Author: Tom Bingham
Date: 2/9/2019
'''

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtCore import Qt, QDate, QDateTime, QTimer
from PyQt5.QtGui import QBrush, QColor, QPen
from astral import Location
from UI_wsprstats import *

import tombo.configfile

class WSPRStats(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configuration = tombo.configfile.ConfigFile('wsprstats.conf')
        self.getConfiguration()
        self.setupMethods()
        self.show()

        #----------------------------------------------------------------------
    def getConfiguration(self):
        pass

    #----------------------------------------------------------------------
    def setupMethods(self):
        pass

    #----------------------------------------------------------------------
    def configActions(self, action):
        """Some pushbutton actions route here."""
        #print(action)
        if action == 'clear':
            pass
        elif action == 'discard':
            pass
        elif action == 'save':
            pass

    #----------------------------------------------------------------------
    def saveConfiguration(self):
        """Save info from config fields."""
        pass
 
    #----------------------------------------------------------------------
    def clearConfigFields(self):
        """Clear text from all config tab fields."""
        pass

    #----------------------------------------------------------------------
    def discardConfigFields(self):
        """Clear all config fields and repopulate with original text."""
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    smw = WSPRStats()
    smw.show()
    sys.exit(app.exec_())
