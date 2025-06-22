from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from apartments import HouseManager

app = QtWidgets.QApplication([])
win = uic.loadUi("apartments.ui")

manager = HouseManager()
manager.read_data_from_file("apartments.txt")

def btnLoadTable():
    win.tableWidget.setRowCount(manager.count)
    for row, x in enumerate(manager.apartments):
        apt = manager.apartments[x]
        for col, value in enumerate(apt.getApartment_forTable()):
            win.tableWidget.setItem(row, col, QTableWidgetItem(value))

def btnAppendApartment():
    data = [
        win.lineEdit_street.text(),
        win.lineEdit_house.text(),
        win.lineEdit_apt.text(),
        win.lineEdit_rooms.text(),
        win.lineEdit_floor.text()
    ]
    manager.appendApartment(data)
    manager.save_to_file("apartments.txt")
    btnLoadTable()

def btnEditApartment():
    row = int(win.lineEdit_row.text()) - 1 if win.lineEdit_row.text() else 0
    col = int(win.lineEdit_col.text()) - 1 if win.lineEdit_col.text() else 0
    
    if row < win.tableWidget.rowCount() and col < win.tableWidget.columnCount():
        data = []
        for i in range(5):  
            if i == col:
                data.append(win.lineEdit_newValue.text())
            else:
                data.append(win.tableWidget.item(row, i).text())
        
        key = manager.find_keyApartment(data)
        if key != -1:
            win.tableWidget.setItem(row, col, QTableWidgetItem(win.lineEdit_newValue.text()))
            manager.editApartment(key, data)
            manager.save_to_file("apartments.txt")

def btnDelApartment():
    data = [
        win.lineEdit_street.text(),
        win.lineEdit_house.text(),
        win.lineEdit_apt.text(),
        win.lineEdit_rooms.text(),
        win.lineEdit_floor.text()
    ]
    manager.delApartment(data)
    manager.save_to_file("apartments.txt")
    btnLoadTable()

win.pushButton_load.clicked.connect(btnLoadTable)
win.pushButton_add.clicked.connect(btnAppendApartment)
win.pushButton_edit.clicked.connect(btnEditApartment)
win.pushButton_del.clicked.connect(btnDelApartment)

win.show()
sys.exit(app.exec())
