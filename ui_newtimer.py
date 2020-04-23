# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newtimer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import json
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import xml.etree.ElementTree as ET
from ui_addlap import Ui_addLap
import time
from datetime import datetime


class Ui_Newtimer(QWidget):


    def __init__(self):
        QWidget.__init__(self)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 131, 31))
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(22, 87, 91, 16))
        self.cboPeriod = QComboBox(self)
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")
        self.cboPeriod.addItem("")

        self.cboPeriod.setObjectName(u"cboPeriod")
        self.cboPeriod.setGeometry(QRect(17, 100, 221, 32))

        self.listTimers = QListWidget(self)

        self.listTimers.setObjectName(u"listTimers")
        self.listTimers.setGeometry(QRect(22, 136, 451, 221))
        #self.listTimers.currentItemChanged.connect(self.selectTimer)
        self.listTimers.itemClicked.connect(self.selectTimer)
        self.listTimers.itemDoubleClicked.connect(self.startTimer)

        #lw = self.listTimers
        #for x in range(lw.count()-1):
        #    lw.item(x).setText("XXX")
        #    lw.item(x).text()

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(23, 372, 131, 16))

        self.btnStart = QPushButton(self)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.hide()
        self.btnStart.clicked.connect(self.startTimer)

        self.btnStart.setGeometry(QRect(19, 400, 110, 32))
        self.btnAddLap = QPushButton(self)
        self.btnAddLap.setObjectName(u"btnAddLap")
        self.btnAddLap.hide()
        self.btnAddLap.clicked.connect(self.addLap)
        self.btnAddLap.setGeometry(QRect(257, 400, 110, 32))

        self.btnDeleteTimer = QPushButton(self)
        self.btnDeleteTimer.setObjectName(u"btnDeleteTimer")
        self.btnDeleteTimer.setGeometry(QRect(369, 400, 110, 32))
        self.btnDeleteTimer.setEnabled(0)
        self.btnDeleteTimer.clicked.connect(self.deleteTimer)

        self.cboTasks = QComboBox(self)
        self.cboTasks.setObjectName(u"cboTasks")
        self.cboTasks.setGeometry(QRect(157, 365, 321, 32))

        self.dtFromFilter = QDateTimeEdit(self)
        self.dtFromFilter.setObjectName(u"dtFromFilter")
        self.dtFromFilter.setGeometry(QRect(320, 75, 151, 22))
        self.dtFromFilter.hide()

        self.dtToPicker = QDateTimeEdit(self)
        self.dtToPicker.setObjectName(u"dtToPicker")
        self.dtToPicker.setGeometry(QRect(320, 100, 151, 22))
        self.dtToPicker.hide()

        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(275, 80, 41, 16))
        self.label_4.hide()

        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(276, 100, 41, 16))
        self.label_5.hide()

        self.retranslateUi(self)

      #  tree = ET.parse("Timers v.1.xml")
      #  root = tree.getroot()

       # for child in root:
            #self.listTimers.addItem(child.get('name') + " (00:00:00)")
       #     self.listTimers.addItem(child.get('name'))
        self.btnDeleteTimer.setEnabled(False)

        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()
        for timer in root.iter('Timer'):
            lap = timer.find("lap")
            if lap != None:
                start_date = lap.get("start")
                last_id=timer.find('lap[last()]').get('end')
                if last_id == None:
                    self.listTimers.addItem("* " + timer.get("name") + " (" + start_date + ") Started")
                else:
                    self.listTimers.addItem(timer.get("name") + " (00:00:00)")
            else:
                self.listTimers.addItem(timer.get("name") + " (00:00:00)")
            #print lap



            #tname = timer.get("name")
            #if xname[0] == tname:
            #    ts = time.time()
            #    data = ET.Element("lap", {"start": tt5})
            #    timer.append(data)
                #root.insert(1, data)
            #    tree.write("Timers v.1.xml")

        QMetaObject.connectSlotsByName(self)


    # setupUi

    def retranslateUi(self, Newtimer):
        Newtimer.setWindowTitle(QCoreApplication.translate("Newtimer", u"Form", None))
        self.label.setText(QCoreApplication.translate("Newtimer", u"Stopwatch", None))
        self.label_2.setText(QCoreApplication.translate("Newtimer", u"Show Timers:", None))
        self.cboPeriod.setItemText(0, QCoreApplication.translate("Newtimer", u"Total", None))
        self.cboPeriod.setItemText(1, QCoreApplication.translate("Newtimer", u"Last Lap", None))
        self.cboPeriod.setItemText(2, QCoreApplication.translate("Newtimer", u"Today", None))
        self.cboPeriod.setItemText(3, QCoreApplication.translate("Newtimer", u"This Week", None))
        self.cboPeriod.setItemText(4, QCoreApplication.translate("Newtimer", u"Workweek Average", None))
        self.cboPeriod.setItemText(5, QCoreApplication.translate("Newtimer", u"This Month", None))
        self.cboPeriod.setItemText(6, QCoreApplication.translate("Newtimer", u"Monthly Average", None))
        self.cboPeriod.setItemText(7, QCoreApplication.translate("Newtimer", u"Yesterday", None))
        self.cboPeriod.setItemText(8, QCoreApplication.translate("Newtimer", u"Last Week", None))
        self.cboPeriod.setItemText(9, QCoreApplication.translate("Newtimer", u"Last Month", None))
        self.cboPeriod.setItemText(10, QCoreApplication.translate("Newtimer", u"Daily", None))
        self.cboPeriod.setItemText(11, QCoreApplication.translate("Newtimer", u"Custom", None))

        self.label_3.setText(QCoreApplication.translate("Newtimer", u"Currently working on:", None))
        self.btnStart.setText(QCoreApplication.translate("Newtimer", u"Start", None))
        self.btnAddLap.setText(QCoreApplication.translate("Newtimer", u"Add Lap", None))
        self.btnDeleteTimer.setText(QCoreApplication.translate("Newtimer", u"Delete Timer", None))
        self.label_4.setText(QCoreApplication.translate("Newtimer", u"From:", None))
        self.label_5.setText(QCoreApplication.translate("Newtimer", u"To:", None))
    # retranslateUi



    def selectTimer(self):
        if not self.listTimers.selectedItems(): return
        self.btnDeleteTimer.setEnabled(True)
        self.btnStart.show()
        self.btnAddLap.show()

        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        selectName = self.listTimers.currentItem().text()
        self.cboTasks.clear()

        if selectName.split(" ")[0] != "*":
            xname = selectName.split(" ")[0]
            self.btnStart.setText(QCoreApplication.translate("Newtimer", u"Start", None))
        else:
            xname = selectName.split(" ")[1]
            self.btnStart.setText(QCoreApplication.translate("Newtimer", u"Stop", None))
        for timer in root.iter('Timer'):
            tname = timer.get("name")
            print xname
            if xname == tname:
                for lap in timer.iter('lap'):

                    if lap.get('task') != None:
                        self.cboTasks.addItem(lap.get('task'))



    def startTimer(self):
        xml_file_name = "Timers v.1.xml"
        tree = ET.parse(xml_file_name)
        root = tree.getroot()

        selectName = self.listTimers.currentItem().text()
        if selectName.split(" ")[0] != "*":

            xname = selectName.split(" (")
            currentDT = datetime.now()
            tt5 = currentDT.strftime("%Y-%m-%d %H:%M:%S")

            self.listTimers.currentItem().setText("* " + selectName)
            self.btnStart.setText(QCoreApplication.translate("Newtimer", u"Stop", None))
            for timer in root.iter('Timer'):
                tname = timer.get("name")
                if xname[0] == tname:
                    ts = time.time()
                    data = ET.Element("lap", {"start": tt5})
                    timer.append(data)
                    tree.write("Timers v.1.xml")
        else:
            currentDT = datetime.now()
            tt5 = currentDT.strftime("%Y-%m-%d %H:%M:%S")
            self.btnStart.setText(QCoreApplication.translate("Newtimer", u"Start", None))
            for timer in root.iter('Timer'):
                tname = timer.get("name")
                if selectName.split(" ")[1] == tname:
                    test_id=timer.find('lap[last()]').get('start')
                    timer.find('lap[last()]').set("end", tt5)
                    #data = ET.Element("lap", {"start": tt5})
                    #timer.append(data)
                    tree.write("Timers v.1.xml")
                    self.listTimers.currentItem().setText(selectName.split(" ")[1] + " (" + currentDT.strftime("%H:%M:%S") + ")")


    def addLap(self):
        Ui_addLap(self.listTimers.currentItem().text())
        #w = Addlap.Addlap(self)
        #if w.exec_() == QDialog.Accepted:
        #   name = w.projectName.text()
        #    self.workList.addItem(name)



    def deleteTimer(self):
        if not self.listTimers.selectedItems(): return
        tree = ET.parse("Timers v.1.xml")
        root = tree.getroot()

        if self.listTimers.currentItem().text().split(" ")[0] != "*":
            selectName = self.listTimers.currentItem().text().split(" ")[0]
        else:
            selectName = self.listTimers.currentItem().text().split(" ")[1]

        for child in root.findall('Timer'):
            strName = child.get('name')
            if strName == selectName:
                buttonReply = QMessageBox.question(self, 'Confirm', "Are you sure wish to delete this timer?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    for item in self.listTimers.selectedItems():
                        self.listTimers.takeItem(self.listTimers.row(item))
                    #print self.listTimers.currentItem().text()
                    root.remove(child)
                    #print self.listTimers.currentItem().text()
                    tree.write('Timers v.1.xml')
                    self.btnDeleteTimer.setEnabled(False)
                    self.btnStart.hide()
                    self.btnAddLap.hide()



            #self.listTimers.addItem(child.get('name'))



