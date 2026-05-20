# deserializer_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from devices import DESERIALIZERS

class DeserializerWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("<b>Deserializers</b>"))
        for name in DESERIALIZERS:
            b = QPushButton(name)
            b.setMinimumHeight(36)
            b.clicked.connect(lambda _, n=name: self._on_select(n))
            layout.addWidget(b)
        self.setLayout(layout)

    def _on_select(self, name):
        # For now we simply show selection in console; you can add settings like Serializer
        print(f"Selected deserializer: {name}")
