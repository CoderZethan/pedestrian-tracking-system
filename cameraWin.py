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
import platform,time
import monitorThread

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
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        result = cv2.VideoWriter ("output.avi", fourcc, 1, (400,400))
        i:int = 0
        while True:
            usb1 = monitorThread.monitor(0)  # 创建外接摄像头对象1
            usb1.run()
            frame_RGB = cv2.cvtColor(usb1.output_image_frame, cv2.COLOR_BGR2RGB)
            frame_write = cv2.resize(usb1.output_image_frame,(400,400))
            result.write(frame_write)
            pixmap = QImage (frame_RGB, 400, 400, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
            i += 1
            self.label.setPixmap(pixmap)
            cv2.imshow("test1",usb1.output_image_frame)
            cv2.waitKey(1)
            print("当前帧数",i)
            print("程序运行时间",time.perf_counter())
            if time.perf_counter() >= 20:
                break
        result.release



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
