# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\git\streamer-sender\ui\videoSetting.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 400)
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setContentsMargins(0, 3, 0, 3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem = QtWidgets.QSpacerItem(20, 135, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem, 4, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setContentsMargins(3, -1, 3, 3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_17.addWidget(self.label_14)
        self.comboBox_scale = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        self.comboBox_scale.setFont(font)
        self.comboBox_scale.setObjectName("comboBox_scale")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_scale)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_18.addWidget(self.label_15)
        self.comboBox_resolution = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        self.comboBox_resolution.setFont(font)
        self.comboBox_resolution.setObjectName("comboBox_resolution")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.comboBox_resolution.addItem("")
        self.horizontalLayout_18.addWidget(self.comboBox_resolution)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem1)
        self.gridLayout_7.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setContentsMargins(3, -1, 3, 3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_7.addLayout(self.horizontalLayout_25)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_8.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBox_2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.checkBox_video_bitrate = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_video_bitrate.setObjectName("checkBox_video_bitrate")
        self.horizontalLayout_24.addWidget(self.checkBox_video_bitrate)
        self.spinBox_video_bitrate = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_video_bitrate.setEnabled(False)
        self.spinBox_video_bitrate.setMinimum(100)
        self.spinBox_video_bitrate.setMaximum(100000)
        self.spinBox_video_bitrate.setObjectName("spinBox_video_bitrate")
        self.horizontalLayout_24.addWidget(self.spinBox_video_bitrate)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_24.addWidget(self.label_11)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_24)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setContentsMargins(3, -1, 3, 3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem4)
        self.gridLayout_9.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setContentsMargins(3, 9, 3, 3)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.comboBox_audioCoding = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        self.comboBox_audioCoding.setFont(font)
        self.comboBox_audioCoding.setObjectName("comboBox_audioCoding")
        self.comboBox_audioCoding.addItem("")
        self.comboBox_audioCoding.addItem("")
        self.comboBox_audioCoding.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_audioCoding)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(3, -1, 3, 3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.label_current_volume = QtWidgets.QLabel(self.groupBox)
        self.label_current_volume.setObjectName("label_current_volume")
        self.horizontalLayout_13.addWidget(self.label_current_volume)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.spinBox_volume_percent = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_volume_percent.setMaximum(1000)
        self.spinBox_volume_percent.setProperty("value", 100)
        self.spinBox_volume_percent.setObjectName("spinBox_volume_percent")
        self.horizontalLayout_11.addWidget(self.spinBox_volume_percent)
        self.comboBox_dB_direction = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_dB_direction.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        self.comboBox_dB_direction.setFont(font)
        self.comboBox_dB_direction.setObjectName("comboBox_dB_direction")
        self.comboBox_dB_direction.addItem("")
        self.comboBox_dB_direction.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_dB_direction)
        self.doubleSpinBox_dB = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_dB.setDecimals(1)
        self.doubleSpinBox_dB.setProperty("value", 0.0)
        self.doubleSpinBox_dB.setObjectName("doubleSpinBox_dB")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_dB)
        self.comboBox_volume_unit = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_volume_unit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox_volume_unit.setObjectName("comboBox_volume_unit")
        self.comboBox_volume_unit.addItem("")
        self.comboBox_volume_unit.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_volume_unit)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.gridLayout_5.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 182, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        self.comboBox_sub_addmode = QtWidgets.QComboBox(self.tab_4)
        font = QtGui.QFont()
        self.comboBox_sub_addmode.setFont(font)
        self.comboBox_sub_addmode.setObjectName("comboBox_sub_addmode")
        self.comboBox_sub_addmode.addItem("")
        self.comboBox_sub_addmode.addItem("")
        self.horizontalLayout_16.addWidget(self.comboBox_sub_addmode)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem9)
        self.gridLayout_4.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.pushButton_sub_add = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_sub_add.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_sub_add.setFont(font)
        self.pushButton_sub_add.setObjectName("pushButton_sub_add")
        self.horizontalLayout_12.addWidget(self.pushButton_sub_add)
        self.label_sub = QtWidgets.QLabel(self.tab_4)
        self.label_sub.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_sub.setText("")
        self.label_sub.setWordWrap(True)
        self.label_sub.setObjectName("label_sub")
        self.horizontalLayout_12.addWidget(self.label_sub)
        self.pushButton_sub_del = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_sub_del.setEnabled(False)
        self.pushButton_sub_del.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_sub_del.setObjectName("pushButton_sub_del")
        self.horizontalLayout_12.addWidget(self.pushButton_sub_del)
        self.horizontalLayout.addLayout(self.horizontalLayout_12)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 245, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.checkBox_pkt_size = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        self.checkBox_pkt_size.setFont(font)
        self.checkBox_pkt_size.setText("")
        self.checkBox_pkt_size.setObjectName("checkBox_pkt_size")
        self.horizontalLayout_28.addWidget(self.checkBox_pkt_size)
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_28.addWidget(self.label_17)
        self.spinBox_pkt_size = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_pkt_size.setEnabled(False)
        self.spinBox_pkt_size.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox_pkt_size.setMinimum(1)
        self.spinBox_pkt_size.setMaximum(2000)
        self.spinBox_pkt_size.setSingleStep(1)
        self.spinBox_pkt_size.setProperty("value", 1316)
        self.spinBox_pkt_size.setObjectName("spinBox_pkt_size")
        self.horizontalLayout_28.addWidget(self.spinBox_pkt_size)
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_28.addWidget(self.label_22)
        self.horizontalLayout_32.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_29.addWidget(self.label_19)
        self.spinBox_local_port = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_local_port.setMaximum(65535)
        self.spinBox_local_port.setSingleStep(1)
        self.spinBox_local_port.setProperty("value", 0)
        self.spinBox_local_port.setObjectName("spinBox_local_port")
        self.horizontalLayout_29.addWidget(self.spinBox_local_port)
        self.horizontalLayout_32.addLayout(self.horizontalLayout_29)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem12)
        self.gridLayout_11.addLayout(self.horizontalLayout_32, 0, 0, 1, 1)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_31.addWidget(self.label_21)
        self.spinBox_buffer_size = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_buffer_size.setMaximum(1000000)
        self.spinBox_buffer_size.setSingleStep(1)
        self.spinBox_buffer_size.setProperty("value", 64)
        self.spinBox_buffer_size.setObjectName("spinBox_buffer_size")
        self.horizontalLayout_31.addWidget(self.spinBox_buffer_size)
        self.label_23 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_31.addWidget(self.label_23)
        self.horizontalLayout_33.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_30.addWidget(self.label_20)
        self.spinBox_ttl = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_ttl.setMaximum(256)
        self.spinBox_ttl.setSingleStep(1)
        self.spinBox_ttl.setProperty("value", 16)
        self.spinBox_ttl.setObjectName("spinBox_ttl")
        self.horizontalLayout_30.addWidget(self.spinBox_ttl)
        self.horizontalLayout_33.addLayout(self.horizontalLayout_30)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem13)
        self.gridLayout_11.addLayout(self.horizontalLayout_33, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_6, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 210, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem14, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(3, -1, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_params_global = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        self.label_params_global.setFont(font)
        self.label_params_global.setText("")
        self.label_params_global.setObjectName("label_params_global")
        self.horizontalLayout_22.addWidget(self.label_params_global)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.plainTextEdit_params_global = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_params_global.setObjectName("plainTextEdit_params_global")
        self.verticalLayout_5.addWidget(self.plainTextEdit_params_global)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_params_out = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        self.label_params_out.setFont(font)
        self.label_params_out.setText("")
        self.label_params_out.setObjectName("label_params_out")
        self.horizontalLayout_21.addWidget(self.label_params_out)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.plainTextEdit_params_out = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_params_out.setObjectName("plainTextEdit_params_out")
        self.verticalLayout_4.addWidget(self.plainTextEdit_params_out)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_params_in = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        self.label_params_in.setFont(font)
        self.label_params_in.setText("")
        self.label_params_in.setObjectName("label_params_in")
        self.horizontalLayout_20.addWidget(self.label_params_in)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.plainTextEdit_params_in = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_params_in.setObjectName("plainTextEdit_params_in")
        self.verticalLayout_3.addWidget(self.plainTextEdit_params_in)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_26.addWidget(self.label_10)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_params_global_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        self.label_params_global_2.setFont(font)
        self.label_params_global_2.setText("")
        self.label_params_global_2.setObjectName("label_params_global_2")
        self.horizontalLayout_27.addWidget(self.label_params_global_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem18)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_27.addWidget(self.label_18)
        self.verticalLayout_6.addLayout(self.horizontalLayout_27)
        self.plainTextEdit_params_url = QtWidgets.QPlainTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        self.plainTextEdit_params_url.setFont(font)
        self.plainTextEdit_params_url.setPlainText("")
        self.plainTextEdit_params_url.setObjectName("plainTextEdit_params_url")
        self.verticalLayout_6.addWidget(self.plainTextEdit_params_url)
        self.horizontalLayout_26.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_26, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem21)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem23)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setEnabled(False)
        self.pushButton_ok.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem24)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "音视频设置"))
        self.groupBox_3.setTitle(_translate("Dialog", "图像"))
        self.label_14.setText(_translate("Dialog", "图像比例"))
        self.comboBox_scale.setItemText(0, _translate("Dialog", "原始"))
        self.comboBox_scale.setItemText(1, _translate("Dialog", "4:3"))
        self.comboBox_scale.setItemText(2, _translate("Dialog", "16:9"))
        self.label_15.setText(_translate("Dialog", "图像分辨率"))
        self.comboBox_resolution.setItemText(0, _translate("Dialog", "原始"))
        self.comboBox_resolution.setItemText(1, _translate("Dialog", "4K"))
        self.comboBox_resolution.setItemText(2, _translate("Dialog", "2K"))
        self.comboBox_resolution.setItemText(3, _translate("Dialog", "1080P"))
        self.comboBox_resolution.setItemText(4, _translate("Dialog", "720P"))
        self.comboBox_resolution.setItemText(5, _translate("Dialog", "480P"))
        self.groupBox_4.setTitle(_translate("Dialog", "视频"))
        self.label_7.setText(_translate("Dialog", "编码格式"))
        self.comboBox.setItemText(0, _translate("Dialog", "原始"))
        self.comboBox.setItemText(1, _translate("Dialog", "H264"))
        self.comboBox.setItemText(2, _translate("Dialog", "H265"))
        self.comboBox.setItemText(3, _translate("Dialog", "MPEG4"))
        self.comboBox.setItemText(4, _translate("Dialog", "MPEG2VIDEO"))
        self.comboBox.setItemText(5, _translate("Dialog", "PCM"))
        self.comboBox.setItemText(6, _translate("Dialog", "FLV1"))
        self.label_8.setText(_translate("Dialog", "帧数"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "原始"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "30"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "60"))
        self.checkBox_video_bitrate.setText(_translate("Dialog", "码率"))
        self.label_11.setText(_translate("Dialog", "kbps"))
        self.groupBox_5.setTitle(_translate("Dialog", "封装"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "视频设置"))
        self.label_9.setText(_translate("Dialog", "音频编码"))
        self.comboBox_audioCoding.setItemText(0, _translate("Dialog", "原始"))
        self.comboBox_audioCoding.setItemText(1, _translate("Dialog", "AAC"))
        self.comboBox_audioCoding.setItemText(2, _translate("Dialog", "AC3"))
        self.groupBox.setTitle(_translate("Dialog", "音量设置"))
        self.label_6.setText(_translate("Dialog", "音频音量"))
        self.label_current_volume.setText(_translate("Dialog", "0.0"))
        self.label_12.setText(_translate("Dialog", "dB"))
        self.label_5.setText(_translate("Dialog", "音量设置"))
        self.comboBox_dB_direction.setItemText(0, _translate("Dialog", "增大"))
        self.comboBox_dB_direction.setItemText(1, _translate("Dialog", "减小"))
        self.comboBox_volume_unit.setItemText(0, _translate("Dialog", "%"))
        self.comboBox_volume_unit.setItemText(1, _translate("Dialog", "dB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "音频设置"))
        self.label_13.setText(_translate("Dialog", "添加方式"))
        self.comboBox_sub_addmode.setItemText(0, _translate("Dialog", "嵌入容器"))
        self.comboBox_sub_addmode.setItemText(1, _translate("Dialog", "嵌入视频流"))
        self.label.setText(_translate("Dialog", "字幕文件"))
        self.pushButton_sub_add.setText(_translate("Dialog", "添加"))
        self.pushButton_sub_del.setText(_translate("Dialog", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "字幕设置"))
        self.groupBox_6.setTitle(_translate("Dialog", "URL参数"))
        self.label_17.setText(_translate("Dialog", "数据包"))
        self.label_22.setText(_translate("Dialog", "字节"))
        self.label_19.setText(_translate("Dialog", "本地端口"))
        self.label_21.setText(_translate("Dialog", "缓冲区大小"))
        self.label_23.setText(_translate("Dialog", "KB"))
        self.label_20.setText(_translate("Dialog", "TTL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "其他设置"))
        self.groupBox_2.setTitle(_translate("Dialog", "参数设置"))
        self.label_4.setText(_translate("Dialog", "全局参数"))
        self.label_2.setText(_translate("Dialog", "输出参数"))
        self.label_3.setText(_translate("Dialog", "输入参数"))
        self.label_10.setText(_translate("Dialog", "URL参数"))
        self.label_18.setText(_translate("Dialog", "例：key=value,空格分隔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "命令参数设置"))
        self.pushButton_ok.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
