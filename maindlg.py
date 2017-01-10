
# -*- coding: utf-8 -*-
import sip
sip.setapi('QString', 2)
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog
from maindlg_ui import Ui_NewsAnal

from grab import Grab


class Crawler(QObject):

    def __init__(self, parent=None):
        super(Crawler, self).__init__(parent)
        self.grab = Grab()

    def crawl(self, url):
        self.grab.go(url)


class MainDialog(QDialog, Ui_NewsAnal):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.onClicked_btnSearch)
        self.btnSortLatest.clicked.connect(self.onClicked_btnSortLatest)
        self.btnSortPopular.clicked.connect(self.onClicked_btnSortLatest)
        self.leUrl.textChanged.connect(self.onTextChanged_leUrl)
        self.targetUrl = None

    def onTextChanged_leUrl(self, newText):
        self.targetUrl = newText

    def onClicked_btnSearch(self):

    def onClicked_btnSortLatest(self):
        print("onClicked_btnSortLatest")

    def onClicked_btnSortPopular(self):
        print("onClicked_btnSortPopular")
