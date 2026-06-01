import tkinter as tk
from ui import show_devices

def main():
    root = tk.Tk()
    root.title("GMSL Config Tool")
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
