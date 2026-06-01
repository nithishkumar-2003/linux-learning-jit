GMSL Modular Monolithic - Attractive GUI (PyQt5)
------------------------------------------------
This project is a modular-monolithic Python desktop application using PyQt5.
It separates device lists and register logic into modules and uses a modern-looking PyQt5 UI.

Files:
- main.py        : Entry point
- ui.py          : PyQt5 UI (MainWindow)
- devices.py     : Lists of serializers/deserializers
- registers.py   : Register simulation logic
- requirements.txt: PyQt5

Run:
1. Create & activate a virtualenv (recommended)
   python -m venv venv
   source venv/bin/activate   (Linux/macOS)
   venv\Scripts\activate    (Windows)

2. Install:
   pip install -r requirements.txt

3. Run:
   python main.py

Notes:
- This is a demo UI with simulated registers. If you want I2C support, I can add smbus2 integration.
- The UI uses a custom stylesheet; tweak ui.py to change colors or fonts.
