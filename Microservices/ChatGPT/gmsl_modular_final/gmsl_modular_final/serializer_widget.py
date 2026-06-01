# serializer_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from device_settings_widget import DeviceSettingsWidget
from devices import SERIALIZERS

class SerializerWidget(QWidget):
    def __init__(self, on_register_update=None):
        super().__init__()
        self.on_register_update = on_register_update
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("<b>Serializers</b>"))

        # Buttons for each serializer
        for name in SERIALIZERS:
            b = QPushButton(name)
            b.setMinimumHeight(36)
            b.clicked.connect(lambda _, n=name: self.show_settings(layout, n))
            layout.addWidget(b)

        self.setLayout(layout)

    def show_settings(self, parent_layout, name):
        # remove old settings widget (if any) then add
        for i in reversed(range(parent_layout.count())):
            w = parent_layout.itemAt(i).widget()
            if w:
                w.deleteLater()

        # re-add title and buttons
        parent_layout.addWidget(__import__('PySide6.QtWidgets', fromlist=['']).QtWidgets.QLabel("<b>Serializers</b>"))
        for name2 in SERIALIZERS:
            b = __import__('PySide6.QtWidgets', fromlist=['']).QtWidgets.QPushButton(name2)
            b.setMinimumHeight(36)
            b.clicked.connect(lambda _, n=name2: self._show_dev_widget(parent_layout, n))
            parent_layout.addWidget(b)

    def _show_dev_widget(self, parent_layout, name):
        # add DeviceSettingsWidget below buttons
        ds = DeviceSettingsWidget(name, on_register_update=self.on_register_update)
        parent_layout.addWidget(ds)
