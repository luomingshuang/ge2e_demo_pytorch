from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import pyqtSlot, Qt

from dynamicLabels import ColorChangingLabel, ImageChangingLabel, CustomButton
from framelessDialog import FramelessDialog

import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

class Ui_MainWindow_transcription(object):
    def setupUi(self, MainWindow_transcription):
        MainWindow_transcription.setObjectName("MainWindow_transcription")
        MainWindow_transcription.resize(1000, 600)
        #MainWindow_player.resize(1400, 600)
        MainWindow_transcription.setMinimumSize(QtCore.QSize(1000, 580))
        MainWindow_transcription.setMaximumSize(QtCore.QSize(1000, 580))
        
        MainWindow_transcription.setLayoutDirection(QtCore.Qt.LeftToRight)

        MainWindow_transcription.setWindowIcon(QIcon('pngs/windows0.jpeg')) #设置窗体标题图标
        ##设置窗口背景图片

        MainWindow_transcription.setStyleSheet("#MainWindow_transcription{border-image:url(./pngs/windows0.jpeg);}")

        self.centralwidget = QtWidgets.QWidget(MainWindow_transcription)
        self.centralwidget.setObjectName("centralwidget")

        # self.line = QtWidgets.QFrame(self.centralwidget)
        # self.line.setGeometry(QtCore.QRect(210, 0, 15, 600))
        # self.line.setLineWidth(2)
        # self.line.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        ###设置颜色
        pe = QPalette()
        pe.setColor(QPalette.WindowText,Qt.green)

        #####显示说话人和分数
        font = QtGui.QFont()
        font.setPointSize(10)

        self.speaker_label = QLabel(self)
        self.speaker_label.setText('您请说：8346175')
        self.speaker_label.setFont(font)

        self.speaker_label.resize(300, 30)
        self.speaker_label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label.move(20, 100)

        self.speaker_label.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label.setPalette(pe)
        #speaker_label.show()

        self.speaker_label1 = QLabel(self)
        self.speaker_label1.setText('您请说：白日依山尽，黄河入海流')
        self.speaker_label1.setFont(font)

        self.speaker_label1.resize(600, 30)
        self.speaker_label1.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label1.move(20, 150)

        self.speaker_label1.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label1.setPalette(pe)

        self.speaker_label2 = QLabel(self)
        self.speaker_label2.setText('您请说：风雨送春归，飞雪迎春到')
        self.speaker_label2.setFont(font)

        self.speaker_label2.resize(600, 30)
        self.speaker_label2.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label2.move(20, 200)

        self.speaker_label2.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label2.setPalette(pe)

        self.speaker_label3 = QLabel(self)
        self.speaker_label3.setText('您请说：京东数科')
        self.speaker_label3.setFont(font)

        self.speaker_label3.resize(300, 30)
        self.speaker_label3.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label3.move(20, 250)

        self.speaker_label3.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label3.setPalette(pe)

        self.speaker_label4 = QLabel(self)
        self.speaker_label4.setText('您请说：周瑜打黄盖-一个愿打一个愿挨')
        self.speaker_label4.setFont(font)

        self.speaker_label4.resize(600, 30)
        self.speaker_label4.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label4.move(20, 300)

        self.speaker_label4.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label4.setPalette(pe)

        self.speaker_label5 = QLabel(self)
        self.speaker_label5.setText('您请说：中华人民共和国')
        self.speaker_label5.setFont(font)

        self.speaker_label5.resize(600, 30)
        self.speaker_label5.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label5.move(20, 350)

        self.speaker_label5.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label5.setPalette(pe)

        self.speaker_label6 = QLabel(self)
        self.speaker_label6.setText('您请说：京东购物季')
        self.speaker_label6.setFont(font)

        self.speaker_label6.resize(600, 30)
        self.speaker_label6.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label6.move(20, 400)

        self.speaker_label6.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label6.setPalette(pe)

        self.speaker_label7 = QLabel(self)
        self.speaker_label7.setText('您请说：空山新雨后，天气晚来秋')
        self.speaker_label7.setFont(font)

        self.speaker_label7.resize(600, 30)
        self.speaker_label7.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label7.move(20, 450)

        self.speaker_label7.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label7.setPalette(pe)

        self.speaker_label8 = QLabel(self)
        self.speaker_label8.setText('您请说：西塞山前白鹭飞')
        self.speaker_label8.setFont(font)

        self.speaker_label8.resize(600, 30)
        self.speaker_label8.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label8.move(20, 500)

        self.speaker_label8.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label8.setPalette(pe)

        self.speaker_label9 = QLabel(self)
        self.speaker_label9.setText('您请说：中国特色社会主义')
        self.speaker_label9.setFont(font)

        self.speaker_label9.resize(600, 30)
        self.speaker_label9.setFont(QFont("Roman times", 15, QFont.Bold))
        self.speaker_label9.move(20, 550)

        self.speaker_label9.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window,Qt.red)
        
        pe.setColor(QPalette.Background, QColor(10,10,10,0))
        self.speaker_label9.setPalette(pe)

        self.record_button_label = ImageChangingLabel(resource_path("images/mic_1.png"), resource_path(
            "images/mic_2.png"),
                                                      self.start_recording)
        self.pause_button_label = ImageChangingLabel(resource_path("images/pause_1.png"), resource_path(
            "images/pause_2.png"),
                                                     self.pause_recording)
        self.stop_button_label = ImageChangingLabel(resource_path("images/stop_1.png"), resource_path(
            "images/stop_2.png"),
                                                    self.stop_recording)

        self.record_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.record_pushButton.setGeometry(QtCore.QRect(260, 160, 61, 41))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.record_pushButton.setFont(font)
        self.record_pushButton.setObjectName("record_pushButton")

        self.record_pushButton.setStyleSheet("QPushButton{border-image: url(pngs/start1.png)}")
        self.record_pushButton.setToolTip('START!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.record_pushButton.move(550, 240)
        self.record_pushButton.resize(120, 120)
        
        ###显示时间###
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(690, 100, 160, 81))
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")

        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pause_pushButton.setGeometry(QtCore.QRect(370, 160, 61, 41))
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.pause_pushButton.setFont(font)
        self.pause_pushButton.setObjectName("pause_pushButton")

        self.pause_pushButton.setStyleSheet("QPushButton{border-image: url(pngs/stop1.png)}")
        self.pause_pushButton.setToolTip('STOP!')

        #self.transcription_pushButton.setGeometry(QtCore.QRect(300, 90, 140, 81))
        self.pause_pushButton.move(880, 240)
        self.pause_pushButton.resize(120, 120)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(5, 40, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        MainWindow_transcription.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow_transcription)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_transcription)
    
    def start_recording(self):
        """This function is called when you press the record button. It will check for user
        errors, and provides error messages, as well as a file selection dialog for getting
        a new file's name. When the recording is started, it will notify via the win10Toast
        module."""

        if self.recording:
            warning_dialog = FramelessDialog(self, "A recording is already underway.", self.normal_bg,
                                             self.highlight_bg, self.normal_color, self.highlight_color, "Error",
                                             self.current_font)
            self.main_frame_blur.setEnabled(True)
            warning_dialog.exec_()
            self.main_frame_blur.setEnabled(False)
        elif not self.recording:
            self.filename = ""
            self.filepath = ""
            self.filepath = QtWidgets.QFileDialog.getSaveFileName(self, "Save Audio As",
                                                                  os.getcwd(), "Audio Files (*.wav)")[0]
            if self.filepath:
                self.filename = os.path.basename(self.filepath)
                self.record_button_label.invert_active_state()
                self.recording = True
                self.paused = False
                self.stopped = False
                self.set_current_recording_text(recording=True)
                self._start_timer_thread()
                self._start_recording_thread()
                self.toaster.show_toast(self.app_name, f"Recording Started:\n{self.filename} created.",
                                        resource_path("images/icon.ico"), 3, True)

    def pause_recording(self):
        
        if self.paused:
            self.pause_button_label.invert_active_state()
            self.recording = True
            self.paused = False
            self.record_button_label.invert_active_state()
            self.set_current_recording_text(recording=True)
        elif self.recording:
            self.recording = False
            self.paused = True
            self.pause_button_label.invert_active_state()
            self.record_button_label.invert_active_state()
            self.set_current_recording_text(paused=True)
        else:
            warning_dialog = FramelessDialog(self, "You must first start a\nrecording to be able to pause.",
                                             self.normal_bg, self.highlight_bg, self.normal_color, self.highlight_color,
                                             "Error", self.current_font)
            self.main_frame_blur.setEnabled(True)
            warning_dialog.exec_()
            self.main_frame_blur.setEnabled(False)

    def stop_recording(self):
        """This function is called when you stop recording. It will check that you have a
        recording that you have at least started already. Otherwise, it will save the recording
        via wave, an in-built python module for wav files. This function will also take care of
        resetting the variables for a new recording to take place."""

        self.stopped = True
        if not self.recording and not self.paused:
            warning_dialog = FramelessDialog(self, "Please start recording first.", self.normal_bg, self.highlight_bg,
                                             self.normal_color, self.highlight_color, "Error", self.current_font)
            self.main_frame_blur.setEnabled(True)
            warning_dialog.exec_()
            self.main_frame_blur.setEnabled(False)
        else:
            if self.recording:
                self.record_button_label.invert_active_state()
            elif self.paused:
                self.pause_button_label.invert_active_state()
            self.recording = False
            self.paused = False
            with wave.open(self.filepath, "wb") as wf:
                wf.setnchannels(self.input_channels)
                wf.setsampwidth(self.p.get_sample_size(SAMPLE_FORMAT))
                wf.setframerate(FPS)
                wf.writeframes(b''.join(self.frames))
                self.frames.clear()
            self.toaster.show_toast(self.app_name, f"Recording Stopped:\n{self.filename} saved.",
                                    resource_path("images/icon.ico"), 3, True)
            self.set_current_recording_text(stopped=True)
            self.total_time = 0.0
            self.filepath = ""
            self.filename = ""
            self.set_current_time_text(0)
        for thread in self.threads:
            if thread.is_alive():
                thread.join(.5)
        self.threads.clear()

    def retranslateUi(self, MainWindow_transcription):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_transcription.setWindowTitle(_translate("MainWindow_transcription", "ENROLL"))
        #self.record_pushButton.setText(_translate("MainWindow_transcription", "录制"))
        #self.pause_pushButton.setText(_translate("MainWindow_transcription", "停止"))
        self.comboBox.setItemText(0, _translate("MainWindow_transcription", "注册音频文件列表"))