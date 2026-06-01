# GMSL Config Tool (Tkinter)

This is a small desktop GUI example written in Python using Tkinter.
It demonstrates a simple monolithic/modular structure to select
Serializer/Deserializer devices and change a simulated register based on
transmission rate.

## Files
- `main.py` : Entry point for the application.
- `ui.py` : UI logic and widgets.
- `devices.py` : Lists of serializer/deserializer devices.
- `registers.py` : Simulated register map and logic.

## Run
1. Make sure you have Python 3 installed.
2. Run `python main.py` from the project directory.
3. The GUI will open. Click "Serializer" → "MAX96717" → "Device Address" → choose "3Gbps" or "6Gbps".
4. The simulated register 0x01 will update and be printed to the console.

## Notes
- This is a simulation. If you want real I2C writes, I can extend `registers.py`
  to use `smbus2` and perform hardware writes — tell me the target platform and I2C bus/address.
