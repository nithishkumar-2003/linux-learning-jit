GMSL Modular Monolithic - Final (PySide6)

How to run:
1. Create a virtualenv (recommended):
   python -m venv venv
   venv\Scripts\activate     (Windows)

2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   python main.py

Notes:
- This app uses PySide6 and should work on Python 3.13 when PySide6 is installed.
- The UI shows only Serializer or Deserializer at a time.
- MAX96717 has Transmission Rate options that update a simulated register 0x01.
- Modify modules (devices.py, registers.py, device_settings_widget.py) to extend behavior.
