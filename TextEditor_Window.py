# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

#import sys
#from PySide6.QtWidgets import QApplication, QMainWindow
#from PySide6.QtCore import QFile
#from mainwindow import Ui_MainWindow

#class MainWindow(QMainWindow):
#    def __init__(self):
#        super(MainWindow,self).__init__()
#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)

# import sys
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtWidgets import QApplication
# from PySide6.QtCore import QFile,QIODevice

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
# #    window = MainWindow()
# #    window.show()
#     ui_file_name = "mainwindow.ui"
#     ui_file = QFile(ui_file_name)

#     if not ui_file.open(QIODevice.ReadOnly):
#         print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
#         sys.exit(-1)

#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     ui_file.close()
#     if not window:
#         print(loader.errorString())
#         sys.exit(-1)
#     window.show()
#     sys.exit(app.exec())

# import sys
from PySide6.QtWidgets import  QMainWindow,QFileDialog,QMessageBox, QFontDialog, QColorDialog
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PySide6.QtCore import QFileInfo, Qt, QTime, QDate
from PySide6.QtGui import QFont
from Texteditor import Ui_TextEditor

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = QMainWindow()
#     window = Ui_TextEditor()
#     window.setupUi(main_window)
#     main_window.show()
#     sys.exit(app.exec())

class EditorWindow(QMainWindow, Ui_TextEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.printfile)
        self.actionPrint_Preview.triggered.connect(self.printpreview)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionExport_As_PDF.triggered.connect(self.filePDF)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionCut.triggered.connect(self.cut)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.textBold)
        self.actionItalic.triggered.connect(self.textItalic)
        self.actionUnderline.triggered.connect(self.textUnderline)
        self.actionLeft.triggered.connect(self.alignLeft)
        self.actionCenter.triggered.connect(self.alignCenter)
        self.actionRight.triggered.connect(self.alignRight)
        self.actionJustify.triggered.connect(self.alignJustify)
        self.actionDate.triggered.connect(self.showDate)
        self.actionTime.triggered.connect(self.showTime)
        self.show()

    def fileNew(self):
        self.textEdit.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
    
    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self,'Save File')
        if filename[0]:
            f = open(filename[0],'w')
            with f:
                text = self.textEdit.toPlainText()
                f.write()
                QMessageBox.about(self,"Save File","File Saved Successfully!")
    
    def printfile(self):
        # Creating a printer object
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)

        if dialog.exec() == QPrintDialog.Accepted:
            self.textEdit.print(printer)
    
    def printpreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec()
    
    def printPreview(self,printer):
        self.textEdit.print_(printer)
    
    def filePDF(self):
        fn,_ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (*.pdf) ;; All files (*.*)")
        if fn != "":
            if QFileInfo(fn).suffix() == "":
                fn += ".pdf"
        
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(fn)
        self.textEdit.document().print_(printer)
    
    def exitApp(self):
        self.close()
    
    def copy(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
    
    def cut(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
        self.textEdit.cut()

    def paste(self):
        self.textEdit.append(self.copiedText)

    def fontDialog(self):
        ok,font = QFontDialog.getFont()     # QFontDialog gives (True, <PySide6.QtGui.QFont(IBM Plex Sans,13,-1,5,700,1,0,0,0,0,0,0,0,0,0,1) at 0x7f829fd61f00>)
        if ok:
            self.textEdit.setFont(font)
    
    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)
    
    def textBold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)
    
    def textItalic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)
    
    def textUnderline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)
    
    def alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)
    
    def alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)
    
    def alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def showTime(self):
        time = QTime.currentTime()
        # print(time.toString())
        # self.textEdit.setText(time.toString(QTime.DefaultLocaleLongDate))
        self.textEdit.setText(time.toString())
    
    def showDate(self):
        date = QDate.currentDate()
        # print(date.toString())
        # self.textEdit.setText(date.toString(QDate.DefaultLocaleLongDate))
        self.textEdit.setText(date.toString())
