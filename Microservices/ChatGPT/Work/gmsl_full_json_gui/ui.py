import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import pathlib
from data import load_bitfields
from storage import save_config



class ModularGMSLApp(tb.Window):
    def __init__(self):
        super().__init__(themename="flatly")   # light theme
        self.title("GMSL Configurator - Modular (JSON-driven)")
        self.geometry("1200x720")
        self.minsize(1100, 640)

        self.bitfields = load_bitfields()  # loads bitfields.json

        # selection state
        self.kind = None       # 'serializers' or 'deserializers'
        self.device = None
        self.register = None
        # store selected values only for enabled fields
        # { "b7": {"type":"enum","value":"6Gbps"}, ... }
        self.values = {}

        self._build_header()
        self._build_columns()

    def _build_header(self):
        header = ttk.Frame(self, padding=6)
        header.pack(fill="x")
        base = pathlib.Path(__file__).parent
        ttk.Label(header, text="GMSL Configurator", font=("Segoe UI", 18, "bold")).pack(side="left")
        # optional: add logos if placed in folder (analog_logo.png, gmsl_logo.png)
        try:
            analog_p = base / "analog_logo.png"
            if analog_p.exists():
                img = Image.open(analog_p).resize((40,40))
                self.analog_img = ImageTk.PhotoImage(img)
                ttk.Label(header, image=self.analog_img).pack(side="left", padx=(8,6))
        except Exception:
            pass

    def _build_columns(self):
        main = ttk.Frame(self, padding=10)
        main.pack(fill="both", expand=True)

        # four columns (always visible)
        self.col1 = ttk.LabelFrame(main, text="1. Type", width=220, bootstyle="light")
        self.col2 = ttk.LabelFrame(main, text="2. Device", width=260, bootstyle="light")
        self.col3 = ttk.LabelFrame(main, text="3. Register", width=260, bootstyle="light")
        self.col4 = ttk.LabelFrame(main, text="4. Bitfields / Values", bootstyle="light")

        self.col1.pack(side="left", fill="y", padx=8, pady=8)
        self.col2.pack(side="left", fill="y", padx=8, pady=8)
        self.col3.pack(side="left", fill="y", padx=8, pady=8)
        self.col4.pack(side="left", fill="both", expand=True, padx=8, pady=8)

        self._init_col1()
        self._init_col2()
        self._init_col3()
        self._init_col4()

    # Column 1: Type
    def _init_col1(self):
        for w in self.col1.winfo_children(): w.destroy()
        ttk.Label(self.col1, text="Select Type", font=("Segoe UI", 12, "bold")).pack(pady=6)
        # read available top-level keys (expected: serializers, deserializers)
        for k in self.bitfields.keys():
            label = k.capitalize()
            ttk.Button(self.col1, text=label, width=18, bootstyle="outline-info",
                       command=lambda kind=k: self._set_type(kind)).pack(pady=6)

        ttk.Separator(self.col1).pack(fill="x", pady=6)
        ttk.Label(self.col1, text="Current:", font=("Segoe UI", 10)).pack(anchor="w", padx=6)
        self.lbl_type = ttk.Label(self.col1, text="None", font=("Segoe UI", 10, "italic"))
        self.lbl_type.pack(anchor="w", padx=6)

    def _set_type(self, kind):
        self.kind = kind
        self.device = None
        self.register = None
        self.values = {}
        self.lbl_type.config(text=kind[:-1].capitalize() if kind.endswith("s") else kind.capitalize())
        self._refresh_devices()
        self._refresh_registers()
        self._render_bitfields()

    # Column 2: Devices
    def _init_col2(self):
        for w in self.col2.winfo_children(): w.destroy()
        ttk.Label(self.col2, text="Devices", font=("Segoe UI", 12, "bold")).pack(pady=6)
        self.devices_box = ttk.Frame(self.col2)
        self.devices_box.pack(fill="both", expand=True, padx=6)
        ttk.Separator(self.col2).pack(fill="x", pady=6)
        self.lbl_device = ttk.Label(self.col2, text="Selected: None")
        self.lbl_device.pack(anchor="w", padx=6)

    def _refresh_devices(self):
        for w in self.devices_box.winfo_children(): w.destroy()
        if not self.kind:
            return
        for dev in self.bitfields[self.kind].keys():
            ttk.Button(self.devices_box, text=dev, width=22, bootstyle="info",
                       command=lambda d=dev: self._set_device(d)).pack(pady=4, anchor="w")

    def _set_device(self, dev):
        self.device = dev
        self.register = None
        self.values = {}
        self.lbl_device.config(text=f"Selected: {dev}")
        self._refresh_registers()
        self._render_bitfields()

    # Column 3: Registers
    def _init_col3(self):
        for w in self.col3.winfo_children(): w.destroy()
        ttk.Label(self.col3, text="Registers", font=("Segoe UI", 12, "bold")).pack(pady=6)
        self.registers_box = ttk.Frame(self.col3)
        self.registers_box.pack(fill="both", expand=True, padx=6)
        ttk.Separator(self.col3).pack(fill="x", pady=6)
        self.lbl_register = ttk.Label(self.col3, text="Selected: None")
        self.lbl_register.pack(anchor="w", padx=6)

    def _refresh_registers(self):
        for w in self.registers_box.winfo_children(): w.destroy()
        if not (self.kind and self.device):
            return
        regs = self.bitfields[self.kind][self.device].get("registers", {})
        for addr in regs.keys():
            ttk.Button(self.registers_box, text=addr, width=18, bootstyle="secondary",
                       command=lambda a=addr: self._set_register(a)).pack(pady=4, anchor="w")

    def _set_register(self, addr):
        self.register = addr
        self.values = {}
        self.lbl_register.config(text=f"Selected: {addr}")
        self._render_bitfields()

    # Column 4: Bitfields / Values
    def _init_col4(self):
        for w in self.col4.winfo_children(): w.destroy()
        header = ttk.Frame(self.col4)
        header.pack(fill="x")
        ttk.Label(header, text="Bitfields / Values", font=("Segoe UI", 12, "bold")).pack(side="left", pady=6)
        ttk.Button(header, text="Save Configuration", bootstyle="success", command=self._save).pack(side="right", padx=6)
        self.fields_frame = ttk.Frame(self.col4)
        self.fields_frame.pack(fill="both", expand=True, padx=6, pady=8)

    def _render_bitfields(self):
        for w in self.fields_frame.winfo_children(): w.destroy()
        if not (self.kind and self.device and self.register):
            ttk.Label(self.fields_frame, text="Select type, device and register to edit bitfields.").pack(pady=8)
            return

        regs = self.bitfields[self.kind][self.device].get("registers", {})
        bits = regs.get(self.register, {}).get("bits", {})
        if not bits:
            ttk.Label(self.fields_frame, text="No bitfields for this register.").pack(pady=8)
            return

        # Render 8 bit rows b7..b0 (so order matches bit positions)
        for i in range(7, -1, -1):
            bitpos = str(i)
            info = bits.get(bitpos)
            row = ttk.Frame(self.fields_frame, padding=6)
            row.pack(fill="x", pady=4)
            if not info:
                ttk.Label(row, text=f"Bit {bitpos} (unused)", width=28).pack(side="left", padx=6)
                continue

            name = info.get("name", f"BIT{bitpos}")
            ttk.Label(row, text=f"{name} (b{bitpos})", width=32).pack(side="left", padx=6)

            btype = info.get("type", "enum")
            vals = info.get("values", [])

            # Enable checkbox: when unchecked, we remove entry from self.values
            en_var = tk.IntVar(value=0)
            en_chk = ttk.Checkbutton(row, text="Enable", variable=en_var, bootstyle="secondary")
            en_chk.pack(side="right", padx=6)

            # widget area for selecting a value
            widget_frame = ttk.Frame(row)
            widget_frame.pack(side="left", padx=6)

            # store closures with correct binding of bitpos
            if btype == "bool":
                var = tk.IntVar(value=0)
                chk = ttk.Checkbutton(widget_frame, text=(vals[-1] if vals else "On"), variable=var, bootstyle="info")
                chk.pack(side="left", padx=4)

                def make_bool_set(bp, varref, enref, valslist):
                    def setter(*_):
                        if enref.get():
                            # map 1 -> second value (if exists), else first
                            if varref.get() == 1 and len(valslist) > 1:
                                val = valslist[1]
                            else:
                                val = valslist[0]
                            self.values[bp] = {"type": "bool", "value": val}
                        else:
                            self.values.pop(bp, None)
                    return setter
                chk.configure(command=make_bool_set(bitpos, var, en_var, vals))

            elif btype == "multi":
                inner = ttk.Frame(widget_frame)
                inner.pack(side="left", padx=6)
                # for each option make a checkbox
                for opt in vals:
                    v = tk.IntVar(value=0)
                    cb = ttk.Checkbutton(inner, text=opt, variable=v, bootstyle="primary-toolbutton")
                    cb.pack(side="left", padx=4)

                    def make_multi(bp, label, varref, enref):
                        def updater(*_):
                            cur = list(self.values.get(bp, {}).get("values", []))
                            if enref.get() and varref.get():
                                if label not in cur:
                                    cur.append(label)
                            else:
                                if label in cur:
                                    cur.remove(label)
                            if cur:
                                self.values[bp] = {"type": "multi", "values": cur}
                            else:
                                self.values.pop(bp, None)
                        return updater
                    cb.configure(command=make_multi(bitpos, opt, v, en_var))

            elif btype == "int":
                sb = ttk.Spinbox(widget_frame, from_=info.get("min", 0), to=info.get("max", 255), width=8)
                sb.pack(side="left", padx=4)

                def make_int(bp, sbref, enref):
                    def setter(*_):
                        if enref.get():
                            try:
                                val = int(sbref.get())
                            except Exception:
                                val = 0
                            self.values[bp] = {"type": "int", "value": val}
                        else:
                            self.values.pop(bp, None)
                    return setter
                # Spinbox command triggers when arrows used; also trace variable with bind
                sb.configure(command=make_int(bitpos, sb, en_var))
                sb.bind("<KeyRelease>", make_int(bitpos, sb, en_var))

            else:  # enum or default
                combo = ttk.Combobox(widget_frame, values=vals, state="readonly", width=18)
                combo.pack(side="left", padx=6)

                def make_enum(bp, combo_ref, enref):
                    def setter(*_):
                        if enref.get() and combo_ref.get():
                            self.values[bp] = {"type": "enum", "value": combo_ref.get()}
                        else:
                            self.values.pop(bp, None)
                    return setter
                combo.bind("<<ComboboxSelected>>", make_enum(bitpos, combo, en_var))

    def _save(self):
        if not (self.kind and self.device and self.register):
            tb.utils.show_alert(title="Error", message="Select type, device and register before saving", alert="danger")
            return
        cfg = {
            "timestamp": __import__("datetime").datetime.now().isoformat(),
            "type": self.kind,
            "device": self.device,
            "register": self.register,
            "bits": self.values
        }
        fname = save_config(cfg)
        tb.utils.show_alert(title="Saved", message=f"Configuration saved to {fname}", alert="success")
