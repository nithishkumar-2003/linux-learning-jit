# device_settings_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QGroupBox, QFormLayout
from registers import read_register, set_tx_rate_bits

class DeviceSettingsWidget(QWidget):
    def __init__(self, device_name: str, on_register_update=None):
        super().__init__()
        self.device_name = device_name
        self.on_register_update = on_register_update
        layout = QVBoxLayout(self)

        title = QLabel(f"<b>{device_name}</b>")
        layout.addWidget(title)

        # Only MAX96717 has configurable TX_RATE for our demo
        if device_name == "MAX96717":
            group = QGroupBox("Device Address / Link")
            form = QFormLayout()
            self.tx_combo = QComboBox()
            self.tx_combo.addItems(["3Gbps", "6Gbps"])
            form.addRow("Transmission Rate:", self.tx_combo)
            group.setLayout(form)
            layout.addWidget(group)

            apply_btn = QPushButton("Apply TX Rate")
            apply_btn.clicked.connect(self.apply_tx_rate)
            layout.addWidget(apply_btn)
        else:
            layout.addWidget(QLabel("No configurable options for this device."))

        # Register display
        self.reg_label = QLabel(self._reg_text())
        self.reg_label.setObjectName("regLabel")
        layout.addWidget(self.reg_label)

        layout.addStretch()

    def apply_tx_rate(self):
        rate = self.tx_combo.currentText()
        new_val = set_tx_rate_bits(rate)
        # update label
        self.reg_label.setText(self._reg_text())
        if callable(self.on_register_update):
            self.on_register_update(0x01, new_val)

    def _reg_text(self):
        v = read_register(0x01)
        return f"0x01 = {bin(v)}"
