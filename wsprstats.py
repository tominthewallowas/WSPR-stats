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

from PySide2.QtWidgets import (QMainWindow, QApplication, QHeaderView, QRadioButton, QButtonGroup)
from PySide2.QtCore import (Qt, QDate, QDateTime)
from PySide2.QtSql import (QSqlQuery, QSqlQueryModel)
from UI_wsprstats import *

from configparser import ConfigParser
import sqlitedatabase
import sqlcasephrases
from selectionchoices import SelectionChoices


class WSPRStats(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.configuration = tombo.configfile.ConfigFile('wsprstats.conf').getItems('CONFIG')
        self.configuration = self.gatherConfiguration('wsprstats.conf')
        self.db = sqlitedatabase.SqliteDatabase(self.configuration['db_file'])
        self.ui.lwConfigInfo.addItem('Datebase file: ' + self.configuration['db_file'])
        self.ui.lwConfigInfo.addItem('Tracked Callsign: ' + self.configuration['trackedcallsign'])
        self.selectionchoices = SelectionChoices()
        self.initialize()
        self.setupMethods()
        self.show()

    def gatherConfiguration(self, filename):
        self.configparser = ConfigParser()
        self.configparser.read(filename)
        return dict(self.configparser.items('CONFIG'))

    # ----------------------------------------------------------------------
    def initialize(self):
        self.setDateTimeEdits()
        self.dateButtonGroup = QButtonGroup()
        self.categoryButtonGroup = QButtonGroup()
        self.loadDateButtonGroup()
        self.loadCategoryButtonGroup()
        self.setDateGroupBoxStatus(self.RADIOBUTTON_ALL_DATES)

    # ----------------------------------------------------------------------
    def setupMethods(self):
        self.ui.action_Quit.triggered.connect(self.close)
        self.ui.pbQuit.clicked.connect(self.close)
        self.ui.pbCollectData.clicked.connect(self.selectModel)
        self.dateButtonGroup.buttonClicked[int].connect(self.setDateGroupBoxStatus)
        self.categoryButtonGroup.buttonClicked[int].connect(self.setCategoryChoice)

    # ----------------------------------------------------------------------
    def loadCategoryButtonGroup(self):
        self.RADIOBUTTON_NO_CATEGORY = 0
        self.RADIOBUTTON_BY_REPORTER_TRANSMITTER_BAND = 1
        self.RADIOBUTTON_BY_BAND = 2

        for button in [button for button in self.ui.gbTotalsByCategory.findChildren(QRadioButton)]:
            if button.objectName() == 'rbNoCategory':
                self.categoryButtonGroup.addButton(button, self.RADIOBUTTON_NO_CATEGORY)
            elif button.objectName() == 'rbByReporterTransmitterBand':
                self.categoryButtonGroup.addButton(button, self.RADIOBUTTON_BY_REPORTER_TRANSMITTER_BAND)
            elif button.objectName() == 'rbByBand':
                self.categoryButtonGroup.addButton(button, self.RADIOBUTTON_BY_BAND)
            elif button.objectName() == 'rbByReportingStation':
                self.categoryButtonGroup.addButton(button, self.RADIOBUTTON_BY_REPORTING_STATION)
            elif button.objectName() == 'rbByTransmittingStation':
                self.categoryButtonGroup.addButton(button, self.RADIOBUTTON_BY_TRANSMITTING_STATION)
    # ----------------------------------------------------------------------

    def loadDateButtonGroup(self):
        self.RADIOBUTTON_ALL_DATES = 0
        self.RADIOBUTTON_PREVIOUS_DAY = 1
        self.RADIOBUTTON_LAST_7_DAYS = 2
        self.RADIOBUTTON_LAST_30_DAYS = 3
        self.RADIOBUTTON_DATERANGE = 4

        for button in [button for button in self.ui.gbSpotsByDates.findChildren(QRadioButton)]:
            if button.objectName() == 'rbDateRange':
                self.dateButtonGroup.addButton(button, self.RADIOBUTTON_DATERANGE)
            elif button.objectName() == 'rbAllDates':
                self.dateButtonGroup.addButton(button, self.RADIOBUTTON_ALL_DATES)
            elif button.objectName() == 'rbPreviousDay':
                self.dateButtonGroup.addButton(button, self.RADIOBUTTON_PREVIOUS_DAY)
            elif button.objectName() == 'rbLast7Days':
                self.dateButtonGroup.addButton(button, self.RADIOBUTTON_LAST_7_DAYS)
            elif button.objectName() == 'rbLast30Days':
                self.dateButtonGroup.addButton(button, self.RADIOBUTTON_LAST_30_DAYS)

    # ----------------------------------------------------------------------
    def setDateTimeEdits(self):
        self.ui.dteFrom.setDateTime(QDateTime.currentDateTime().toUTC())
        self.ui.dteTo.setDateTime(QDateTime.currentDateTime().toUTC())

    # ----------------------------------------------------------------------
    def setCategoryChoice(self, buttonId):
        self.selectionchoices.setCategoryChoice(buttonId)

    # ----------------------------------------------------------------------
    def setDateGroupBoxStatus(self, buttonId):
        self.selectionchoices.setDateChoice(buttonId)
        self.ui.gbDateRange.setEnabled(True if buttonId == self.RADIOBUTTON_DATERANGE else False)

    # ----------------------------------------------------------------------
    def selectModel(self):
        conn = self.db.getConnection()
        model = QSqlQueryModel()
        query = QSqlQuery(conn)
        self.buildSqlStatement(query)
        query.exec_()
        if query.lastError().driverText():
            print("Query error msg:", query.lastError().driverText())
        model.setQuery(query)
        self.ui.tblStats.setModel(model)
        self.ui.tblStats.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    # ----------------------------------------------------------------------
    def buildSqlStatement(self, query):
        callsign = self.configuration['trackedcallsign']

        if self.selectionchoices.getDateChoice() == self.RADIOBUTTON_ALL_DATES:
            if self.selectionchoices.getCategoryChoice() == self.RADIOBUTTON_NO_CATEGORY:
                sql = "select reporter as Reporter, reporter_grid as 'Rpt Grid', xmit_callsign as 'Transmitter', xmit_grid as 'Xmit Grid', " + sqlcasephrases.sql_power_case_phrase + " as Power, " + sqlcasephrases.sql_band_case_phrase + " as Band, distance as 'Distance(km)', datetime(timestamp, 'unixepoch') as 'Date/Time', signal_noise_ratio as SNR from wspr_stats where (reporter = :callsign or xmit_callsign = :callsign) order by reporter, xmit_callsign"

            if self.selectionchoices.getCategoryChoice() == self.RADIOBUTTON_BY_REPORTER_TRANSMITTER_BAND:
                sql = "select reporter as Reporter, xmit_callsign as 'Transmitter', " + sqlcasephrases.sql_band_case_phrase + " as Band, count(*) as 'Band Count' from wspr_stats where reporter = :callsign or xmit_callsign = :callsign group by reporter, xmit_callsign, band order by reporter, xmit_callsign, band"

            if self.selectionchoices.getCategoryChoice() == self.RADIOBUTTON_BY_BAND:
                sql = "select  " + sqlcasephrases.sql_band_case_phrase + " as Band, count(*) as 'Band Count' from wspr_stats where reporter = :callsign or xmit_callsign = :callsign group by band order by band"

            query.prepare(sql)
            query.bindValue(':callsign', callsign)

        if self.selectionchoices.getDateChoice() in (self.RADIOBUTTON_PREVIOUS_DAY, self.RADIOBUTTON_LAST_7_DAYS, self.RADIOBUTTON_LAST_30_DAYS, self.RADIOBUTTON_DATERANGE):
            toDateTime = QDateTime.currentDateTime().toSecsSinceEpoch()
            if self.selectionchoices.getDateChoice() == self.RADIOBUTTON_PREVIOUS_DAY:
                fromDateTime = QDateTime.currentDateTime().addDays(-1).toSecsSinceEpoch()
            elif self.selectionchoices.getDateChoice() == self.RADIOBUTTON_LAST_7_DAYS:
                fromDateTime = QDateTime.currentDateTime().addDays(-7).toSecsSinceEpoch()
            elif self.selectionchoices.getDateChoice() == self.RADIOBUTTON_LAST_30_DAYS:
                fromDateTime = QDateTime.currentDateTime().addDays(-30).toSecsSinceEpoch()
            elif self.selectionchoices.getDateChoice() == self.RADIOBUTTON_DATERANGE:
                fromDateTime = self.ui.dteFrom.dateTime().toSecsSinceEpoch()
                toDateTime = self.ui.dteTo.dateTime().toSecsSinceEpoch()

            if self.selectionchoices.getCategoryChoice() == self.RADIOBUTTON_NO_CATEGORY:
                sql = "select reporter as Reporter, reporter_grid as 'Rpt Grid', xmit_callsign as 'Transmitter', xmit_grid as 'Xmit Grid', " + sqlcasephrases.sql_power_case_phrase + " as Power, " + sqlcasephrases.sql_band_case_phrase + " as Band, distance as 'Distance(km)', datetime(timestamp, 'unixepoch') as 'Date/Time', signal_noise_ratio as SNR from wspr_stats where (reporter = :callsign or xmit_callsign = :callsign) and (timestamp between :from and :to) order by reporter, xmit_callsign"
            elif self.selectionchoices.getCategoryChoice() == self.RADIOBUTTON_BY_REPORTER_TRANSMITTER_BAND:
                sql = "select reporter as Reporter, xmit_callsign as 'Transmitter', band as Band, count(*) as 'Band Count' from wspr_stats where (reporter = :callsign or xmit_callsign = :callsign) and (timestamp between :from and :to) group by reporter, xmit_callsign, band order by reporter, xmit_callsign, band"
            elif self.selectionchoices.getCategoryChoice() == self.RADIOBUTTON_BY_BAND:
                sql = "select " + sqlcasephrases.sql_band_case_phrase + " Band, count(*) as 'Band Count' from wspr_stats where (reporter = :callsign or xmit_callsign = :callsign) and (timestamp between :from and :to) group by band order by band"

            query.prepare(sql)
            query.bindValue(':callsign', callsign)
            query.bindValue(':from', int(fromDateTime))
            query.bindValue(':to', int(toDateTime))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wss = WSPRStats()
    wss.show()
    sys.exit(app.exec_())
