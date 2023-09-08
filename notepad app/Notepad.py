from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

from PyQt5 import uic, QtGui
import sys
import os


# import Notepad


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("notepad.ui", self)
        self.menu = self.findChild(QMenuBar, "menubar")

        # text edit
        self.plain_text = self.findChild(QTextEdit, "textEdit")
        self.plain_text.document().modificationChanged.connect(self.setWindowModified)
        self.plain_text.textChanged.connect(self.position_of_cursor)

        # status bar
        self.status_bar = self.findChild(QStatusBar, "statusbar")
        self.filename = None

        # menu bar functions
        # File Menu
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(lambda: self.file_open())
        self.actionSave.triggered.connect(lambda: self.file_save())
        self.actionSave_as.triggered.connect(lambda: self.file_save_as())

        # exit
        self.actionExit.triggered.connect(self.file_exit)

        # Edit Menu
        self.actionUndo.triggered.connect(self.a_undo)
        self.actionRedo.triggered.connect(self.a_redo)
        #
        self.actionCut.triggered.connect(self.a_cut)
        self.actionCopy.triggered.connect(self.a_copy)
        self.actionPaste.triggered.connect(self.a_paste)
        self.actionSelect_all.triggered.connect(self.a_select_all)
        self.actionDelete.triggered.connect(self.a_delete)

        # View Menu functions

        self.actionStatus_bar.triggered.connect(self.v_statusBar)
        

        # status bar information
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.position_of_cursor)
        self.timer.start(1000)
        self.myMessage = QLabel()

        # Word Wrap
        self.actionWord_Wrap.triggered.connect(self.word_wrap)

        # Zoom function

        self.actionZoom_in.triggered.connect(self.zoomin)
        self.actionZoom_out.triggered.connect(self.zoomout)
        self.actionRestore_default_zoom.triggered.connect(self.restore_to_default)
        
        # base font
        self.fnt = 20

        self.show()

    ############################################## File Menu Functions ############################

    def file_new(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Notepad")
        self.msg.setText("Do you want to save the changes?")
        self.msg.setIcon(QMessageBox.Information)

        self.msg.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.pop_up)

        self.msg.exec_()

   # Save the recent file before closing warning dialog box
    def pop_up(self, i):

        if i.text() == "Save":
            try:
                self.file_save()
            except Exception as e:
                print(e)

        elif i.text() == "Discard":
            self.plain_text.clear()
            self.msg.close()
        elif i.text() == "Cancel":
            self.msg.close()

    # For opening a file

    # this variable is used to save and new file in file_save st if

    def file_open(self):

        fname = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt)")

        print(fname[0])
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.plain_text.setPlainText(data)
            f.close()
        fname = fname[0]

    # For writing to files

    def file_save(self):
        if not self.isWindowModified():
            return
        if not self.filename:
            self.file_save_as()
        else:
            with open(self.filename, 'w') as f:
                f.write(self.plain_text.toPlainText())

    def file_save_as(self):

        if not self.isWindowModified():
            return
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Files", "", " Text Files (*.txt) ;;All files (*)", options=options)

        if filename:
            with open(filename, 'w') as f:
                f.write(self.plain_text.toPlainText()) 
                self.filename = filename
                self.setWindowTitle(
                    str(os.path.basename(filename)) + " - Notepad[*]")

    # Exit the app function

    def file_exit(self):
        self.close()

    # Printin as a text document

    ############################################## Edit Menu functions ############################

    def a_undo(self):
        self.plain_text.undo()

    def a_redo(self):
        self.plain_text.redo()

    def a_cut(self):
        self.plain_text.cut()

    def a_copy(self):
        self.plain_text.copy()

    def a_paste(self):
        self.plain_text.paste()

    def a_select_all(self):
        self.plain_text.selectAll()

    def a_delete(self):
        self.plain_text.cut()

################################################## View Menu Functions ############################

    def v_statusBar(self):

        if self.actionStatus_bar.isChecked() is True:
            self.status_bar.setVisible(True)

            self.ct = 1
            if self.ct == 1:
                self.statusbar.addWidget(self.myMessage)
                self.ct = 2

            else:
                self.myMessage.show()

        elif self.actionStatus_bar.isChecked() is False:
            self.status_bar.setVisible(False)

    def position_of_cursor(self):

        self.a = self.plain_text.textCursor().position()
        self.c = self.plain_text.textCursor().columnNumber()
        self.l = self.plain_text.textCursor().blockNumber()+1

        print(self.a)
        print(f"c{self.c}")
        print(f"l {self.l}")
        self.myMessage.setText(
            f"   cursor position: {str(self.a)} | col: {self.c} | ln: {self.l} ")

    def word_wrap(self):
        if self.actionWord_Wrap.isChecked() == True:
            self.plain_text.setLineWrapMode(QTextEdit.FixedColumnWidth)
            self.plain_text.setLineWrapColumnOrWidth(70)
            print("Line Wrap on")
        if self.actionWord_Wrap.isChecked() == False:
            self.plain_text.setLineWrapMode(QTextEdit.NoWrap)
            print("Line Wrap off")

    def zoomin(self):
        self.fnt = self.fnt+1
        print(f"font{self.fnt}")
        if self.fnt <= 8:
            self.plain_text.setStyleSheet(
                "QTextEdit { border: none; font: 20px Consolas } ")
            self.fnt = 9
        else:
            self.plain_text.setStyleSheet(
                f"QTextEdit {{ border: none; font: {self.fnt}px Consolas }} ")

    def zoomout(self):
        self.fnt = self.fnt-1
        print(f"font1: {self.fnt}")

        if self.fnt <= 8:
            self.plain_text.setStyleSheet(
                "QTextEdit { border: none; font: 11px Consolas } ")
            self.fnt = 9
        else:
            self.plain_text.setStyleSheet(
                f"QTextEdit {{ border: none; font: {self.fnt}px Consolas }} ")

    def restore_to_default(self):
            self.plain_text.setStyleSheet(
                "QTextEdit { border: none; font: 20px Consolas } ")
        
app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()