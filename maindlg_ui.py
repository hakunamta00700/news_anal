# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindlg.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewsAnal(object):
    def setupUi(self, NewsAnal):
        NewsAnal.setObjectName("NewsAnal")
        NewsAnal.resize(388, 556)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NewsAnal)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leUrl = QtWidgets.QLineEdit(NewsAnal)
        self.leUrl.setObjectName("leUrl")
        self.horizontalLayout.addWidget(self.leUrl)
        self.btnSearch = QtWidgets.QPushButton(NewsAnal)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnSortPopular = QtWidgets.QPushButton(NewsAnal)
        self.btnSortPopular.setObjectName("btnSortPopular")
        self.horizontalLayout_3.addWidget(self.btnSortPopular)
        self.btnSortLatest = QtWidgets.QPushButton(NewsAnal)
        self.btnSortLatest.setObjectName("btnSortLatest")
        self.horizontalLayout_3.addWidget(self.btnSortLatest)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lwResult = QtWidgets.QListWidget(NewsAnal)
        self.lwResult.setObjectName("lwResult")
        self.verticalLayout.addWidget(self.lwResult)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(NewsAnal)
        QtCore.QMetaObject.connectSlotsByName(NewsAnal)

    def retranslateUi(self, NewsAnal):
        _translate = QtCore.QCoreApplication.translate
        NewsAnal.setWindowTitle(_translate("NewsAnal", "댓글 분석기"))
        self.btnSearch.setText(_translate("NewsAnal", "검색"))
        self.btnSortPopular.setText(_translate("NewsAnal", "인기순"))
        self.btnSortLatest.setText(_translate("NewsAnal", "최신순"))

