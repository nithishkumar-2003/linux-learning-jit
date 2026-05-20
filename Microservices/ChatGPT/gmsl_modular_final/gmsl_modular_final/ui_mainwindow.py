# ui_mainwindow.py
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QComboBox, QFrame
from PySide6.QtCore import Qt
from serializer_widget import SerializerWidget
from deserializer_widget import DeserializerWidget
from themes import dark, light

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        # central container
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(12,12,12,12)
        main_layout.setSpacing(12)

        # Left panel (controls)
        left = QFrame()
        left.setObjectName("leftPanel")
        left.setFixedWidth(240)
        left_layout = QVBoxLayout(left)
        left_layout.setSpacing(10)

        lbl = QLabel("Mode")
        left_layout.addWidget(lbl)

        self.btn_serializer = QPushButton("Serializer")
        self.btn_deserializer = QPushButton("Deserializer")
        self.btn_serializer.setCheckable(True)
        self.btn_deserializer.setCheckable(True)

        self.btn_serializer.clicked.connect(self.show_serializer)
        self.btn_deserializer.clicked.connect(self.show_deserializer)

        left_layout.addWidget(self.btn_serializer)
        left_layout.addWidget(self.btn_deserializer)

        left_layout.addSpacing(8)
        left_layout.addWidget(QLabel("Theme"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Dark", "Light"])
        self.theme_combo.currentTextChanged.connect(self.apply_theme)
        left_layout.addWidget(self.theme_combo)
        left_layout.addStretch()

        # Right panel (content)
        right = QFrame()
        right.setObjectName("rightPanel")
        right_layout = QVBoxLayout(right)
        right_layout.setSpacing(8)

        self.header = QLabel("Select a mode and device")
        right_layout.addWidget(self.header)

        # placeholder content area
        self.content_container = QFrame()
        self.content_layout = QVBoxLayout(self.content_container)
        right_layout.addWidget(self.content_container)

        main_layout.addWidget(left)
        main_layout.addWidget(right, 1)

        # initial widgets
        self.serializer_widget = SerializerWidget(on_register_update=self.on_register_update)
        self.deserializer_widget = DeserializerWidget()

        # default state: serializer visible (match earlier preference)
        self.btn_serializer.setChecked(True)
        self.show_serializer()

        # default theme
        self.theme_combo.setCurrentText("Dark")
        self.apply_theme("Dark")

    def apply_theme(self, name):
        if name == "Dark":
            self.setStyleSheet(dark)
        else:
            self.setStyleSheet(light)

    def _clear_content(self):
        for i in reversed(range(self.content_layout.count())):
            w = self.content_layout.itemAt(i).widget()
            if w:
                w.setParent(None)  # remove

    def show_serializer(self):
        self.btn_serializer.setChecked(True)
        self.btn_deserializer.setChecked(False)
        self._clear_content()
        self.header.setText("Serializers")
        self.content_layout.addWidget(self.serializer_widget)

    def show_deserializer(self):
        self.btn_serializer.setChecked(False)
        self.btn_deserializer.setChecked(True)
        self._clear_content()
        self.header.setText("Deserializers")
        self.content_layout.addWidget(self.deserializer_widget)

    def on_register_update(self, addr, val):
        # optional callback when a register updates
        # you could show a transient status in statusBar
        self.statusBar().showMessage(f"Updated 0x{addr:02X} -> {bin(val)}", 3000)
