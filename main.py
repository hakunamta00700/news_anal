# -*- coding: utf-8 -*-

import grab
import bs4


'''
1. url 입력 - 뉴스 주소 입력

2. 뉴스 댓글을 쫙 긁어옴.
3. 댓글 리스트 중 한개의 댓글을 클릭하면
4. 댓글 돔에 유저아이디 있는 부분에 특이 점이 있는 지 확인
5.
'''

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import sys
from maindlg import MainDialog
# reload(sys)
# try:
#     sys.setdefaultencoding("utf-8")
# except:
#     pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setApplicationName("ApplicationName")
    # app.setOrganizationName("OrganizationName")

    dlg = MainDialog()
    dlg.show()
    sys.exit(app.exec_())
