# themes.py

dark = """
QWidget {
    background-color: #f3f6fb;
    color: #222;
    font-family: "Segoe UI", Arial;
}
#leftPanel {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #eef4ff);
    border-radius: 10px;
    padding: 12px;
}
#rightPanel {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ffffff, stop:1 #f7fbff);
    border-radius: 10px;
    padding: 12px;
}
QPushButton {
    background: #4860ff;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 8px;
}
QPushButton:hover { background: #2f49d1; }
QComboBox { padding: 6px; min-width: 120px; }
QLabel#regLabel { font-family: "Courier New"; }
"""

light = """
QWidget {
    background-color: #ffffff;
    color: #111;
    font-family: "Segoe UI", Arial;
}
#leftPanel {
    background: #ffffff;
    border-radius: 8px;
    padding: 12px;
}
#rightPanel {
    background: #fcfdff;
    border-radius: 8px;
    padding: 12px;
}
QPushButton {
    background: #0b78d1;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 8px;
}
QPushButton:hover { background: #075fa8; }
QComboBox { padding: 6px; min-width: 120px; }
QLabel#regLabel { font-family: "Courier New"; }
"""
