from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random
import json

app = QApplication([])
main_win = QWidget()
main_win.resize(900, 600)
main_win.setWindowTitle('Умные заметки')
bigtextedit = QTextEdit()
lineedit = QLineEdit()
listwidget = QListWidget()
lstwidget = QListWidget()
b1 = QPushButton('Сохранить заметку')
b2 = QPushButton('Добавить к заметке')
b3 = QPushButton('Создать заметку')
b4 = QPushButton('Удалить заметку')
b5 = QPushButton('Открепить от заметки')
b6 = QPushButton('Искать заметки по тегу')
l1 = QHBoxLayout()
l2 = QHBoxLayout()
l3 = QVBoxLayout()
l4 = QHBoxLayout()
l1.addWidget(b3)
l1.addWidget(b4)
l2.addWidget(b2)
l2.addWidget(b5)
l3.addWidget(listwidget)
l3.addLayout(l1)
l3.addWidget(b1)
l3.addWidget(lstwidget)
l3.addWidget(lineedit)
l3.addLayout(l2)
l3.addWidget(b6)
l4.addWidget(bigtextedit)
l4.addLayout(l3)
main_win.setLayout(l4)
main_win.show()

def add_note():
    note_name, ok = QInputDialog.getText(
        main_win, 'Добавить заметку', 'Название заметки: '
    )
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" : []}
        listwidget.addItem(note_name)
        lstwidget.addItems(notes[note_name]["теги"])

def del_note():
    if listwidget.selectedItems():
        key = listwidget.selectedItems()[0].text()
        del notes[key]
        listwidget.clear()
        bigtextedit.clear()
        lstwidget.clear()
        listwidget.addItems(notes)
        with open('nts.json', 'w') as file:
            json.dump(notes, file, ensure_ascii=False)

def save_note():
    if listwidget.selectedItems():
        key = listwidget.selectedItems()[0].text()
        gotText = bigtextedit.toPlainText()
        notes[key]['текст']=gotText
        with open('nts.json', 'w') as file:
            json.dump(notes, file, ensure_ascii=False)
            print(notes)

def show_notes():
    key = listwidget.selectedItems()[0].text()
    bigtextedit.setText(notes[key]['текст'])
    lstwidget.clear()
    lstwidget.addItems(notes[key]['теги'])

def add_tag():
    if listwidget.selectedItems():
        key = listwidget.selectedItems()[0].text()
        gotNameTag = lineedit.text()
        if not gotNameTag in notes[key]['теги']:
            notes[key]['теги'].append(gotNameTag)
            lstwidget.addItem(gotNameTag)
            lineedit.clear()
            with open('nts.json', 'w') as file:
                json.dump(notes, file, ensure_ascii=False)
                print(notes)
                
def del_tag():
    if lstwidget.selectedItems():
        key = listwidget.selectedItems()[0].text()
        gotDelTag = lstwidget.selectedItems()[0].text()
        notes[key]['теги'].remove(gotDelTag)
        with open('nts.json', 'w') as file:
                json.dump(notes, file, ensure_ascii=False)
                print(notes)
                lstwidget.clear()
                lstwidget.addItems(notes[key]['теги'])

def search_tag():
    if b6.text() == 'Искать заметки по тегу':
        gotSearchTag = lineedit.text()
        notes_filtered = {}
        for note in notes:
            if gotSearchTag in notes[note]['теги']:
                notes_filtered[note]=gotSearchTag
        listwidget.clear()
        listwidget.addItems(notes_filtered)
        b6.setText('Сбросить поиск')
        print(notes_filtered)
    elif b6.text() == 'Сбросить поиск':
        lineedit.clear()
        listwidget.clear()
        listwidget.addItems(notes)
        b6.setText('Искать заметки по тегу')
listwidget.itemClicked.connect(show_notes)
b3.clicked.connect(add_note)
b4.clicked.connect(del_note)
b1.clicked.connect(save_note)
b2.clicked.connect(add_tag)
b5.clicked.connect(del_tag)
b6.clicked.connect(search_tag)
with open('nts.json', 'r') as file:
    notes = json.load(file)

listwidget.addItems(notes)

app.exec()