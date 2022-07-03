

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QTime
from PasswordWindow import Ui_PasswordWindow
from datetime import datetime
import requests
from threading import Thread


try:
    import local_db
    store_id = local_db.get_store_number()
except Exception as e:
    print("Error::: {}".format(str(e)))

class Ui_MainWindow(object):
    def __init__(self):
        self.alert_gen_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def get_store_id(self):
        try:
            import local_db
            store_id = local_db.get_store_number()
            print(f"get_store_id fun: {store_id}")
            return store_id
        except Exception as e:
            store_id = "0789"
            print("Error::: {}".format(str(e)))
            return store_id
    
    def api_call(self, alert_attend_time, store_id):
        url = "https://saivalentine.com/alert_attend"
        headers = {'accept': '/', 'content-type': 'application/json', 'user-agent': 'XY'}
        proxies = {
                    'http':"http://webproxy01:80", 
                    'https':"http://webproxy01:80" 
                }
        data = dict(alert_gen_time=self.alert_gen_time, alert_attend_time=alert_attend_time, store_id=store_id)
        print(data)
        try:
            r = requests.post(url=url, json=data, verify=False)
        except:
            r = requests.post(url=url, json=data, headers=headers, proxies=proxies, verify=False)
            # r = requests.post(url=url, data=data, proxies=proxies, verify=False)
        print(r)

    def ok_button(self, MainWindow):
        store_id = self.get_store_id()
        alert_attend_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            x = Thread(target = self.api_call, args=(alert_attend_time, store_id))
            x.start()
        except:
            print("Error: unable to start thread")
        MainWindow.close()

    def openwindow(self, MainWindow):
        MainWindow.close()
        self.Window =  QtWidgets.QMainWindow()
        self.ui = Ui_PasswordWindow()
        self.ui.setupUi(self.Window)
        self.Window.show()
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 306)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        MainWindow.setWindowFlags(QtCore.Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.ok_button(MainWindow))#clicked = lambda: self.openwindow(MainWindow))
        # self.pushButton.setGeometry(QtCore.QRect(850, 500, 151, 41))
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
QTimer.singleShot (10000, lambda: ui.openwindow(MainWindow))
sys.exit(app.exec_())