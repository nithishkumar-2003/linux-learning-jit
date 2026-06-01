# main.py
import sys
from PySide6.QtWidgets import QApplication
from ui_mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MainWindow()
    win.setWindowTitle('GMSL Config Tool - Modular')
    win.resize(900, 520)
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
