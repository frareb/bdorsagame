# Form implementation generated from reading ui file 'ui/fiche_joueur.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormFicheJoueur(object):
    def setupUi(self, FormFicheJoueur):
        FormFicheJoueur.setObjectName("FormFicheJoueur")
        FormFicheJoueur.resize(400, 450)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=FormFicheJoueur)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 381, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxTypeFarm = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.comboBoxTypeFarm.setAccessibleName("")
        self.comboBoxTypeFarm.setCurrentText("")
        self.comboBoxTypeFarm.setObjectName("comboBoxTypeFarm")
        self.gridLayout.addWidget(self.comboBoxTypeFarm, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=FormFicheJoueur)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 381, 181))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_2.addWidget(self.spinBox_6, 2, 5, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_2.addWidget(self.spinBox_8, 3, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_2.addWidget(self.spinBox_5, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_2.addWidget(self.spinBox_3, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_2.addWidget(self.spinBox_4, 1, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 4, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 4, 1, 1)
        self.spinBox_7 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout_2.addWidget(self.spinBox_7, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.spinBox_9 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_2.addWidget(self.spinBox_9, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 4, 4, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_2.addWidget(self.spinBox_10, 4, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 4, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=FormFicheJoueur)
        self.buttonBox.setGeometry(QtCore.QRect(220, 410, 166, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Apply|QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(parent=FormFicheJoueur)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit_idJoueur = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_idJoueur.setObjectName("lineEdit_idJoueur")
        self.gridLayout_3.addWidget(self.lineEdit_idJoueur, 0, 1, 1, 1)

        self.retranslateUi(FormFicheJoueur)
        self.comboBoxTypeFarm.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(FormFicheJoueur)

    def retranslateUi(self, FormFicheJoueur):
        _translate = QtCore.QCoreApplication.translate
        FormFicheJoueur.setWindowTitle(_translate("FormFicheJoueur", "Fiche joueur"))
        self.label_2.setText(_translate("FormFicheJoueur", "Nom"))
        self.label.setText(_translate("FormFicheJoueur", "Prénom"))
        self.label_3.setText(_translate("FormFicheJoueur", "Type"))
        self.label_4.setText(_translate("FormFicheJoueur", "Surface"))
        self.groupBox.setTitle(_translate("FormFicheJoueur", "Variétés"))
        self.label_9.setText(_translate("FormFicheJoueur", "Var05"))
        self.label_10.setText(_translate("FormFicheJoueur", "Var06"))
        self.label_6.setText(_translate("FormFicheJoueur", "Var02"))
        self.label_5.setText(_translate("FormFicheJoueur", "Var01"))
        self.label_11.setText(_translate("FormFicheJoueur", "Var07"))
        self.label_12.setText(_translate("FormFicheJoueur", "Var08"))
        self.label_8.setText(_translate("FormFicheJoueur", "Var04"))
        self.label_7.setText(_translate("FormFicheJoueur", "Var03"))
        self.label_14.setText(_translate("FormFicheJoueur", "Var09"))
        self.label_15.setText(_translate("FormFicheJoueur", "Var10"))
        self.label_13.setText(_translate("FormFicheJoueur", "Numero d\'identifiant du joueur"))
