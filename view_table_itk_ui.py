# Form implementation generated from reading ui file 'ui/view_table_itk.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormTableITK(object):
    def setupUi(self, FormTableITK):
        FormTableITK.setObjectName("FormTableITK")
        FormTableITK.resize(866, 692)
        self.tableView = QtWidgets.QTableView(parent=FormTableITK)
        self.tableView.setGeometry(QtCore.QRect(0, 10, 861, 631))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(parent=FormTableITK)
        self.pushButton.setGeometry(QtCore.QRect(650, 650, 88, 25))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=FormTableITK)
        self.pushButton_2.setGeometry(QtCore.QRect(747, 650, 111, 25))
        icon = QtGui.QIcon.fromTheme("document-revert")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(FormTableITK)
        QtCore.QMetaObject.connectSlotsByName(FormTableITK)

    def retranslateUi(self, FormTableITK):
        _translate = QtCore.QCoreApplication.translate
        FormTableITK.setWindowTitle(_translate("FormTableITK", "Form"))
        self.pushButton.setText(_translate("FormTableITK", "OK"))
        self.pushButton_2.setText(_translate("FormTableITK", "ANNULER"))