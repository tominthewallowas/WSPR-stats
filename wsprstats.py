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

from PyQt5.QtWidgets import (QMainWindow, QApplication, QGraphicsScene)
from PyQt5.QtCore import (Qt, QDate, QDateTime, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QPen)
from PyQt5.QtSql import (QSqlQuery, QSqlQueryModel)
from UI_wsprstats import *

import tombo.configfile
import sqlstatements
import sqlitedatabase

class WSPRStats(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configuration = tombo.configfile.ConfigFile('wsprstats.conf').getItems('CONFIG')
        self.db = sqlitedatabase.SqliteDatabase(self.configuration['db_file'])
        self.setupMethods()
        self.reporter_grids = []
        self.xmit_grids = []
        self.methodDirector('Xmit_Callsigns')
        self.methodDirector('Reporter_Callsigns')
        
        self.show()

    #----------------------------------------------------------------------
    def selectModel(self, sql, callsign):
        conn = self.db.getConnection()
        model = QSqlQueryModel()
        query = QSqlQuery(conn)
        query.prepare(sql)
        query.bindValue(':callsign', callsign)
        #print(sql)
        query.exec()
        #print("Query error msg:", query.lastError().driverText())
        model.setQuery(query)
        self.ui.tblStats.setModel(model)

    #----------------------------------------------------------------------
    def loadXmitCallsigns(self, sql):
        result = self.db.select(sql)
        while result.next():
            self.ui.cmbXmits.addItem(result.value('xmit_callsign'))
            self.xmit_grids.append(result.value('xmit_grid'))

    #----------------------------------------------------------------------
    def loadReporterCallsigns(self, sql):
        result = self.db.select(sql)
        while result.next():
            self.ui.cmbReporters.addItem(result.value('reporter'))
            self.reporter_grids.append(result.value('reporter_grid'))

    #----------------------------------------------------------------------
    def setupMethods(self):
        self.ui.action_Quit.triggered.connect(lambda: self.methodDirector("Quit"))
        #self.ui.pbLoadTable.clicked.connect(lambda: self.methodDirector("Table1"))
        #self.ui.pbLoadTable2.clicked.connect(lambda: self.methodDirector("Table2"))
        #self.ui.pbLoadList.clicked.connect(lambda: self.methodDirector("List"))
        self.ui.cmbXmits.activated[str].connect(self.xmitComboSelect)
        self.ui.cmbReporters.activated[str].connect(self.reporterComboSelect)

    #----------------------------------------------------------------------
    def methodDirector(self, action):
        if action == 'Quit':
            self.close()
        elif action == 'Table1':
            self.selectModel('select count(*) as row_count from wspr_stats')
        elif action == 'Table2':
            self.selectModel(sqlstatements.combined)
        elif action == 'Xmit_Callsigns':
            self.loadXmitCallsigns(sqlstatements.xmit_callsigns)
        elif action == 'Reporter_Callsigns':
            self.loadReporterCallsigns(sqlstatements.reporter_callsigns)

    #----------------------------------------------------------------------
    def xmitComboSelect(self, text):
        self.setReporterFacts(text, self.reporter_grids[self.ui.cmbReporters.currentIndex()])
        self.selectModel(sqlstatements.xmit_findings, text)

    #----------------------------------------------------------------------
    def reporterComboSelect(self, text):
        self.setReporterFacts(text, self.reporter_grids[self.ui.cmbReporters.currentIndex()])
        self.selectModel(sqlstatements.reporter_findings, text)

    #----------------------------------------------------------------------
    def setReporterFacts(self, callsign, grid):
        self.ui.lblCallsignFacts.setText(callsign + ' - ' + grid)

    #----------------------------------------------------------------------
    def setXmitFacts(self, callsign, grid):
        self.ui.lblCallsignFacts.setText(callsign + ' - ' + grid)

    #----------------------------------------------------------------------
    def testQuery(self, statement):
        print('Statement:', statement)
        result = self.db.select(statement)
        print(type(result))
        while result.next():
            print(result.value('reporter'), result.value('reporter_callsign_count'), result.value('xmit_callsign_count'))

    #----------------------------------------------------------------------
    def configActions(self, action):
        """Some pushbutton actions route here."""
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
