from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QWidget
)
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt

from main_window_ui import Ui_mainwindow
from view_table_itk_ui import Ui_FormTableITK
from fiche_joueur_window_ui import Ui_FormFicheJoueur

import pandas as pd

import os
import sys
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_csv = os.path.abspath(os.path.join(bundle_dir, "resources/pratiques04052023.csv"))

COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # value = self._data[index.row()][index.column()]
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        # if role == Qt.ItemDataRole.DecorationRole:
        #     # value = self._data[index.row()][index.column()]
        #     value = self._data.iloc[index.row(), index.column()]
        #     if (isinstance(value, int) or isinstance(value, float)):
        #         value = int(value)  # Convert to integer for indexing.
        #         # Limit to range -5 ... +5, then convert to 0..10
        #         value = max(-5, value)  # values < -5 become -5
        #         value = min(5, value)  # values > +5 become +5
        #         value = value + 5  # -5 becomes 0, +5 becomes + 10
        #         return QtGui.QColor(COLORS[value])

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

    # def rowCount(self, index):
    #     return len(self._data)

    # def columnCount(self, index):
    #     return len(self._data[0])


class Fiche_joueur_Window(QWidget, Ui_FormFicheJoueur):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
class ItkWindow(QWidget, Ui_FormTableITK):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #  https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/
        data = pd.read_csv(path_to_csv)
        # data = [
        #     ["irrigation", "irrigation", "irrigation", "irr", 1, 1, -7, 2],
        #     ["irrigation", "irrigation", "irrigation", "irr", 2, 1, -2, 3],
        #     ["irrigation", "irrigation", "irrigation", "irr", 3, 1, 3, 2],
        #     ["irrigation", "irrigation", "irrigation", "irr", 4, 1, -1, 6],
        #     ["...", "...", "...", "irr", 3, 1, -1, 2],
        # ]
        self.model = TableModel(data)
        self.tableView.setModel(self.model)


class Window(QMainWindow, Ui_mainwindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_propos.triggered.connect(self.about)
        self.pushButton_2.clicked.connect(self.view_itk)
        self.commandLinkButton_creerJoueurs.clicked.connect(self.view_fiche_joueur)

    def view_fiche_joueur(self):
        self.win_fiche_joueur = Fiche_joueur_Window()
        self.win_fiche_joueur.comboBoxTypeFarm.addItem("Agriculteur exportateur")
        self.win_fiche_joueur.comboBoxTypeFarm.addItem("Agriculteur local")
        self.win_fiche_joueur.comboBoxTypeFarm.addItem("Négociant Bana bana")
        self.win_fiche_joueur.comboBoxTypeFarm.addItem("Négociant exportateur")
        self.win_fiche_joueur.lineEdit_idJoueur.setText(win.spinBox_nombreDeJoueurs.text())
        self.win_fiche_joueur.show()

    def view_itk(self, checked):
        # print("should open window itk")
        self.win_view_itk = ItkWindow()
        self.win_view_itk.show()

    def about(self):
        QMessageBox.about(
            self,
            "À propos du jeu 'Course contre la mouche'",
            "<p>Jeu de rôle pour une gestion territoriale de la mouche des fruits dans la filière mangue. </p>"
            "<p>projet DISLAND ; CIRAD-IRD</p>",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    # pyinstaller --name Bdorsalis --onefile --windowed --icon=./resources/fly.ico --add-data "resources:resources" app.py
