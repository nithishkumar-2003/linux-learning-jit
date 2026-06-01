import tkinter as tk
from tkinter import ttk
from devices import SERIALIZERS, DESERIALIZERS
from registers import set_tx_rate, read_register_map

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_tx_rate_options(frame_options):
    clear_frame(frame_options)

    tk.Label(frame_options, text="Transmission Rate", font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=(5,0))
    rate_dropdown = ttk.Combobox(frame_options, values=["3Gbps", "6Gbps"], state='readonly')
    rate_dropdown.pack(pady=8, padx=10, anchor='w')
    rate_dropdown.bind("<<ComboboxSelected>>", lambda e: set_tx_rate(rate_dropdown.get()))

    # Show current simulated register value
    value_label = tk.Label(frame_options, text=f"Current 0x01 = {bin(read_register_map()[0x01])}")
    value_label.pack(anchor='w', padx=10, pady=(8,0))

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
