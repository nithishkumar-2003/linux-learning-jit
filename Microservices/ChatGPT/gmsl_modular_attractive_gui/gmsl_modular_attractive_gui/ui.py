from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QListWidget, QListWidgetItem, QPushButton,
    QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QFrame, QStackedWidget,
    QGroupBox, QFormLayout, QSizePolicy, QSpacerItem
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from devices import SERIALIZERS, DESERIALIZERS
from registers import read_register, set_tx_rate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GMSL Config Tool — Modular Monolithic')
        self.setMinimumSize(800, 500)
        self._setup_ui()
        self.apply_styles()

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        # Left panel: type and device list
        left_panel = QFrame()
        left_panel.setObjectName('leftPanel')
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(12,12,12,12)
        left_layout.setSpacing(10)

        type_label = QLabel('Select Type')
        type_label.setFont(QFont('Segoe UI', 10, QFont.Bold))
        left_layout.addWidget(type_label)

        # Buttons for Serializer / Deserializer
        btn_layout = QHBoxLayout()
        self.btn_serializer = QPushButton('Serializer')
        self.btn_deserializer = QPushButton('Deserializer')
        self.btn_serializer.setCheckable(True)
        self.btn_deserializer.setCheckable(True)
        self.btn_serializer.clicked.connect(self.show_serializers)
        self.btn_deserializer.clicked.connect(self.show_deserializers)
        btn_layout.addWidget(self.btn_serializer)
        btn_layout.addWidget(self.btn_deserializer)
        left_layout.addLayout(btn_layout)

        # Device list
        dev_label = QLabel('Devices')
        dev_label.setFont(QFont('Segoe UI', 9, QFont.Bold))
        left_layout.addWidget(dev_label)

        self.device_list = QListWidget()
        self.device_list.setSpacing(6)
        self.device_list.itemClicked.connect(self.on_device_selected)
        left_layout.addWidget(self.device_list, 1)

        # Right panel: options / inspector
        right_panel = QFrame()
        right_panel.setObjectName('rightPanel')
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(12,12,12,12)
        right_layout.setSpacing(12)

        inspector_label = QLabel('Properties')
        inspector_label.setFont(QFont('Segoe UI', 10, QFont.Bold))
        right_layout.addWidget(inspector_label)

        # Stacked widget to show different device option pages
        self.stack = QStackedWidget()
        right_layout.addWidget(self.stack, 1)

        # Default empty page
        empty = QWidget()
        empty_l = QVBoxLayout(empty)
        empty_l.addWidget(QLabel('Select a device to configure from the left.'))
        empty_l.addStretch()
        self.stack.addWidget(empty)

        # Add MAX96717 page
        self.page_max96717 = self._make_max96717_page()
        self.stack.addWidget(self.page_max96717)

        # Bottom area: register display & action
        bottom_frame = QFrame()
        bottom_layout = QHBoxLayout(bottom_frame)
        bottom_layout.setContentsMargins(0,0,0,0)

        self.reg_label = QLabel(self._reg_text())
        self.reg_label.setFont(QFont('Courier', 10))
        bottom_layout.addWidget(self.reg_label)

        bottom_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        refresh_btn = QPushButton('Refresh')
        refresh_btn.clicked.connect(self.refresh_register)
        bottom_layout.addWidget(refresh_btn)

        right_layout.addWidget(bottom_frame)

        # Layout split
        main_layout = QHBoxLayout(central)
        main_layout.addWidget(left_panel, 30)
        main_layout.addWidget(right_panel, 70)

        # start with serializers selected
        self.btn_serializer.setChecked(True)
        self.show_serializers()

    def _make_max96717_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(10)

        group = QGroupBox('MAX96717 - Device Address')
        form = QFormLayout()
        self.tx_rate_combo = QComboBox()
        self.tx_rate_combo.addItems(['3Gbps', '6Gbps'])
        form.addRow('Transmission Rate:', self.tx_rate_combo)
        group.setLayout(form)
        layout.addWidget(group)

        # Apply button
        apply_btn = QPushButton('Apply Changes')
        apply_btn.setFixedHeight(36)
        apply_btn.clicked.connect(self.apply_tx_rate)
        layout.addWidget(apply_btn, alignment=Qt.AlignLeft)

        layout.addStretch()
        return page

    def show_serializers(self):
        self.btn_serializer.setChecked(True)
        self.btn_deserializer.setChecked(False)
        self.populate_devices(SERIALIZERS)

    def show_deserializers(self):
        self.btn_serializer.setChecked(False)
        self.btn_deserializer.setChecked(True)
        self.populate_devices(DESERIALIZERS)

    def populate_devices(self, devs):
        self.device_list.clear()
        for d in devs:
            item = QListWidgetItem(d)
            item.setSizeHint(QSize(200, 40))
            self.device_list.addItem(item)
        # reset inspector
        self.stack.setCurrentIndex(0)
        self.reg_label.setText(self._reg_text())

    def on_device_selected(self, item):
        name = item.text()
        # For this demo only MAX96717 has options
        if name == 'MAX96717':
            # index 1 is our page for MAX96717
            self.stack.setCurrentWidget(self.page_max96717)
        else:
            # show a simple message page
            msg = QWidget()
            l = QVBoxLayout(msg)
            l.addWidget(QLabel(f'No configurable options for {name}.'))
            l.addStretch()
            # ensure single instance in stack
            if self.stack.indexOf(msg) == -1:
                self.stack.addWidget(msg)
            self.stack.setCurrentWidget(msg)

    def apply_tx_rate(self):
        rate = self.tx_rate_combo.currentText()
        val = set_tx_rate(rate)
        self.reg_label.setText(self._reg_text())
        # simple feedback
        if val is not None:
            # flash message on status (temporary)
            self.statusBar().showMessage(f'Set TX rate: {rate} (reg 0x01 = {bin(val)})', 4000)

    def refresh_register(self):
        self.reg_label.setText(self._reg_text())
        self.statusBar().showMessage('Register refreshed', 2000)

    def _reg_text(self):
        v = read_register(0x01)
        return f'0x01 = {bin(v)}'

    def apply_styles(self):
        # basic modern stylesheet
        self.setStyleSheet("""
        QMainWindow {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                        stop:0 #f7f9fb, stop:1 #eaf2f8);
        }
        #leftPanel {
            background: #ffffff;
            border-radius: 10px;
            padding: 6px;
        }
        #rightPanel {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #ffffff, stop:1 #f3f6fb);
            border-radius: 10px;
            padding: 10px;
        }
        QListWidget {
            background: transparent;
            border: none;
        }
        QListWidget::item {
            background: #f0f4ff;
            margin: 4px;
            padding: 10px;
            border-radius: 8px;
        }
        QListWidget::item:selected {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #6aa7ff, stop:1 #4d8eff);
            color: white;
        }
        QPushButton {
            background: #4860ff;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 8px;
        }
        QPushButton:checked {
            background: #2f49d1;
        }
        QGroupBox {
            background: rgba(255,255,255,0.6);
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 8px;
            padding: 8px;
        }
        QComboBox {
            padding: 6px;
            min-width: 120px;
        }
        QLabel {
            color: #2b2b2b;
        }
        """)
