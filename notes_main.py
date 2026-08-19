from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random
import json



with open('0.txt', 'w', encoding='utf-8') as file:
    file.write('Добро пожаловать!' + '\n')
    file.write(f'Добро пожаловать! Здесь вы можете легко создавать новые заметки, редактировать их, удалять ненужные записи и удобно организовывать всю информацию с помощью гибкой системы тегов, создавая и удаляя их в пару кликов.' + '\n')
    file.write('\n')

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
        note = [note_name, '', []]
        notes.append(note)
        with open(str(len(notes))+'.txt', 'w', encoding='utf-8') as file:
            file.write(note[0]+'\n')
            file.write(note[1]+'\n')
            for tag in note[2]:
                file.write(tag)
            print(notes)
        listwidget.addItem(note[0])
def del_note():
    pass

def save_note():
    if listwidget.selectedItems():
        key = listwidget.selectedItems()[0].text()
        for note in notes:
            if key == note[0]:
                filename = str(len(notes))+'.txt'
                note[1]=bigtextedit.toPlainText()
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(note[0] + '\n')
                    file.write(note[1] + '\n')
                    for tag in note[2]:
                        file.write(tag)
                    file.write('\n')



def show_notes():
    key = listwidget.selectedItems()[0].text()
    for note in notes:
        if key == note[0]:
            bigtextedit.clear()
            lstwidget.clear()
            bigtextedit.setText(note[1])
            lstwidget.addItems(note[2])

def add_tag():
    pass
     
                
def del_tag():
    pass

def search_tag():
    pass
listwidget.itemClicked.connect(show_notes)
b3.clicked.connect(add_note)
b4.clicked.connect(del_note)
b1.clicked.connect(save_note)
b2.clicked.connect(add_tag)
b5.clicked.connect(del_tag)
b6.clicked.connect(search_tag)

notes = []
num_name = 0
while True:
    filename = str(num_name)+".txt"
    try:
        with open(filename, 'r') as file:
            note = []
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
            note[2] = note[2].split()
            notes.append(note)
            num_name += 1
            print('Все заметки:', notes)
    except IOError:
        print('Опаньки! Больше нету заметок!')
        break
for note in notes:
    listwidget.addItem(note[0])

app.exec()