#! /usr/bin/python3

################################################################################
## Form generated from reading UI file 'test_1st.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import cv2
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 400, 400))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 40, 400, 400))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 440, 120, 80))
        self.pushButton.setText("保存视频")
        # self.pushButton.clicked.connect
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 43))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def displayVideo(self):
        self.cap1 = cv2.VideoCapture(0)
        self.cap2 = cv2.VideoCapture(1)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter ("output.avi", fourcc, 1.0, (400,400))
        i:int = 0
        while True:
            _,frame1 = self.cap1.read()
            _,frame2 = self.cap2.read()
            frame1 = cv2.resize(frame1,(400,400))
            frame2 = cv2.resize(frame2,(400,400))
            frame1_RGB = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            out.write(frame1)
            frame2_RGB = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
            pixmap1 = QImage (frame1_RGB, 400, 400, QImage.Format_RGB888)
            pixmap2 = QImage (frame2_RGB, 400, 400, QImage.Format_RGB888)
            pixmap1 = QPixmap.fromImage(pixmap1)
            pixmap2 = QPixmap.fromImage(pixmap2)
            print(i)
            i += 1
            # if i >= 100:
            #     self.label.setPixmap(pixmap)
            self.label.setPixmap(pixmap1)
            self.label_2.setPixmap(pixmap2)
            cv2.imshow("test1",frame1)
            cv2.imshow("test2",frame2)
            cv2.waitKey(1)
            print("hello!")
            time.sleep(1)
            if i >= 5:
                break
        out.release()
        print("保存成功！")
    # def saveVideo():
        

    # def displayPic(self):
    #     self.cap = cv2.VideoCapture(1)
    #     _,frame = self.cap.read()
    #     if _ == False:
    #         self.cap = cv2.VideoCapture(1)
    #     if _ == True:
    #         frame = cv2.resize(frame,(400,400))
    #         frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         pixmap = QImage(frame_RGB, 400, 400, QImage.Format_RGB888)
    #         pixmap = QPixmap.fromImage(pixmap)
    #         cv2.imshow("test",frame)
    #         self.label_2.setPixmap(pixmap)

        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication([])
    win = QMainWindow()
    ui = Ui_MainWindow() # 始化一个window实例
    ui.setupUi(win)
    win.show()
    ui.displayVideo()
    app.exec()
