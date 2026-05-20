import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time

DEVICES_URL = "http://127.0.0.1:5001"
REG_URL = "http://127.0.0.1:5002"

def safe_get(url, retries=5, delay=0.5):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=1.0)
            r.raise_for_status()
            return r
        except Exception as e:
            time.sleep(delay)
    return None

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_tx_rate_options(frame_options):
    clear_frame(frame_options)
    tk.Label(frame_options, text="Transmission Rate", font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=(5,0))
    rate_dropdown = ttk.Combobox(frame_options, values=["3Gbps", "6Gbps"], state='readonly')
    rate_dropdown.pack(pady=8, padx=10, anchor='w')

    def apply_rate():
        rate = rate_dropdown.get()
        if not rate:
            messagebox.showwarning("Select", "Choose a rate first")
            return
        try:
            r = requests.post(f"{REG_URL}/registers/0x01/set_tx_rate", json={"rate": rate}, timeout=2.0)
            r.raise_for_status()
            data = r.json()
            messagebox.showinfo("Done", f"Updated register 0x01 -> {data.get('bin')}")
            update_register_label(frame_options)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to set rate: {e}")

    tk.Button(frame_options, text="Apply", command=apply_rate).pack(padx=10, pady=6, anchor='w')

    # Register value label
    value_label = tk.Label(frame_options, text="Current 0x01 = (unknown)")
    value_label.pack(anchor='w', padx=10, pady=(8,0))
    frame_options._reg_label = value_label
    update_register_label(frame_options)

def update_register_label(frame_options):
    try:
        r = requests.get(f"{REG_URL}/registers/0x01", timeout=1.0)
        if r and r.ok:
            v = r.json().get('value')
            frame_options._reg_label.config(text=f"Current 0x01 = {bin(v)}")
    except:
        frame_options._reg_label.config(text="Current 0x01 = (service down)")

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
    # query devices service
    endpoint = "/devices/serializers" if type_choice == "Serializer" else "/devices/deserializers"
    r = safe_get(DEVICES_URL + endpoint)
    if not r:
        tk.Label(frame_devices, text="Devices service not available", fg='red').pack(padx=10, pady=10)
        return
    devices = r.json()
    tk.Label(frame_devices, text=f"{type_choice} Devices:", font=('Arial', 10, 'bold')).pack(anchor='w', padx=10)
    for dev in devices:
        tk.Button(frame_devices, text=dev, width=25,
                  command=lambda d=dev: show_device_options(d, frame_options)).pack(pady=3, padx=10, anchor='w')

def main():
    root = tk.Tk()
    root.title("GMSL Config Tool - Microservice-like Local")
    root.geometry("520x360")

    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    frame_devices = tk.Frame(root)
    frame_devices.pack(pady=10, fill='x')

    frame_options = tk.Frame(root)
    frame_options.pack(pady=10, fill='both', expand=True)

    tk.Button(frame_top, text="Serializer", width=18,
              command=lambda: show_devices("Serializer", frame_devices, frame_options)).grid(row=0, column=0, padx=5)
    tk.Button(frame_top, text="Deserializer", width=18,
              command=lambda: show_devices("Deserializer", frame_devices, frame_options)).grid(row=0, column=1, padx=5)

    root.mainloop()

if __name__ == '__main__':
    main()
