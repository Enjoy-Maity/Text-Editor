import sys
from PySide6.QtWidgets import QApplication
from TextEditor_Window import EditorWindow

app = QApplication(sys.argv)
text_editor = EditorWindow()
sys.exit(app.exec())