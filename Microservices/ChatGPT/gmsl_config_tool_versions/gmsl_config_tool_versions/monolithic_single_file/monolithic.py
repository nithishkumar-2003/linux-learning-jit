"""Monolithic single-file GMSL Config Tool (Tkinter)
Everything (UI + device lists + register logic) is in this one file.
Run: python monolithic.py
"""
import tkinter as tk
from tkinter import ttk

# --- Devices (embedded) ---
SERIALIZERS = ["MAX96717", "MAX96793", "MAX9295D"]
DESERIALIZERS = ["MAX96724", "MAX96794", "MAX9294"]

# --- Register simulation (embedded) ---
register_map = {0x01: 0b00000000}

def read_register_map():
    return register_map

def set_tx_rate(rate):
    if 0x01 not in register_map:
        register_map[0x01] = 0
    if rate == "3Gbps":
        register_map[0x01] = (register_map[0x01] | (1 << 1)) & ~(1 << 2)
    elif rate == "6Gbps":
        register_map[0x01] = (register_map[0x01] & ~(1 << 1)) | (1 << 2)
    else:
        return
    print(f"[REGISTER] 0x01 updated: {bin(register_map[0x01])}")

# --- UI functions (embedded) ---
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_tx_rate_options(frame_options):
    clear_frame(frame_options)
    tk.Label(frame_options, text="Transmission Rate", font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=(5,0))
    rate_dropdown = ttk.Combobox(frame_options, values=["3Gbps", "6Gbps"], state='readonly')
    rate_dropdown.pack(pady=8, padx=10, anchor='w')
    rate_dropdown.bind("<<ComboboxSelected>>", lambda e: (set_tx_rate(rate_dropdown.get()), update_register_label(frame_options)))
    # Register value label
    value_label = tk.Label(frame_options, text=f"Current 0x01 = {bin(read_register_map()[0x01])}")
    value_label.pack(anchor='w', padx=10, pady=(8,0))
    # Store label for updates
    frame_options._reg_label = value_label

def update_register_label(frame_options):
    if hasattr(frame_options, '_reg_label'):
        frame_options._reg_label.config(text=f"Current 0x01 = {bin(read_register_map()[0x01])}")

def show_device_options(device, frame_options):
    clear_frame(frame_options)
    if device == "MAX96717":
        tk.Button(frame_options, text="Device Address", width=20,
                  command=lambda: show_tx_rate_options(frame_options)).pack(pady=5, padx=10, anchor='w')
    else:
        tk.Label(frame_options, text=f"No configurable options for {device}.").pack(padx=10, pady=10, anchor='w')

def show_devices(type_choice, frame_devices, frame_options):
    clear_frame(frame_devices)
    clear_frame(frame_options)
    devices = SERIALIZERS if type_choice == "Serializer" else DESERIALIZERS
    tk.Label(frame_devices, text=f"{type_choice} Devices:", font=('Arial', 10, 'bold')).pack(anchor='w', padx=10)
    for dev in devices:
        tk.Button(frame_devices, text=dev, width=25,
                  command=lambda d=dev: show_device_options(d, frame_options)).pack(pady=3, padx=10, anchor='w')

# --- Main ---
def main():
    root = tk.Tk()
    root.title("GMSL Config Tool - Monolithic")
    root.geometry("480x320")

    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    frame_devices = tk.Frame(root)
    frame_devices.pack(pady=10, fill='x')

    frame_options = tk.Frame(root)
    frame_options.pack(pady=10, fill='both', expand=True)

    tk.Button(frame_top, text="Serializer", width=15,
              command=lambda: show_devices("Serializer", frame_devices, frame_options)).grid(row=0, column=0, padx=5)
    tk.Button(frame_top, text="Deserializer", width=15,
              command=lambda: show_devices("Deserializer", frame_devices, frame_options)).grid(row=0, column=1, padx=5)

    root.mainloop()

if __name__ == '__main__':
    main()
