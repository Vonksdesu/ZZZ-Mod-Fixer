# --- START OF FILE zzz-mod-fixer-gui.py ---

import os
import sys
import json
import datetime
import time
import struct
import shutil
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkfont
from pathlib import Path
from PIL import Image, ImageTk
import importlib.util


if getattr(sys, 'frozen', False):
    _BASE_DIR = Path(sys._MEIPASS)
    _DATA_DIR = Path(sys.executable).parent
else:
    _BASE_DIR = Path(__file__).parent
    _DATA_DIR = _BASE_DIR

_ICON_CACHE_DIR = _BASE_DIR / "Assets" / "Icons"
_FOLDER_ICON_PATH = _ICON_CACHE_DIR / "folder.png"
_REFRESH_ICON_PATH = _ICON_CACHE_DIR / "refresh.png"


class _GuiStdout:
    def __init__(self, gui):
        self._gui = gui
        self._buffer = ""

    def write(self, data):
        if not data:
            return
        self._buffer += data
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            if self._should_filter(line):
                continue
            self._gui.after(0, lambda l=line: self._gui._append_cli_output(l + "\n"))

    def flush(self):
        if self._buffer:
            cleaned = "" if self._should_filter(self._buffer) else self._buffer
            if cleaned:
                self._gui.after(0, lambda b=cleaned: self._gui._append_cli_output(b))
            self._buffer = ""

    @staticmethod
    def _should_filter(text: str) -> bool:
        normalized = text.strip().lower()
        if not normalized:
            return False
        return normalized.startswith("press") and ("exit" in normalized or "quit" in normalized)




class _ToolTip:
    def __init__(self, widget, text):
        self._widget = widget
        self._text = text
        self._tip = None
        widget.bind('<Enter>', self._show)
        widget.bind('<Leave>', self._hide)
        widget.bind('<Motion>', self._move)

    def _show(self, event=None):
        if self._tip is not None:
            return
        self._tip = tk.Toplevel(self._widget)
        self._tip.overrideredirect(True)
        self._tip.attributes('-topmost', True)
        label = tk.Label(self._tip, text=self._text, bg='#ffffe0', fg='#000000', relief='solid', borderwidth=1, padx=4, pady=2, font=('Tahoma', 9))
        label.pack()
        self._move(event)

    def _move(self, event=None):
        if self._tip is None:
            return
        x = self._widget.winfo_pointerx() + 12
        y = self._widget.winfo_pointery() + 12
        self._tip.geometry(f'+{x}+{y}')

    def _hide(self, event=None):
        if self._tip is not None:
            self._tip.destroy()
            self._tip = None

class ZZZModFixerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ZZZ Mod Fixer GUI")
        self.geometry("1100x720")
        self.minsize(1100, 720)

        icon_path = _BASE_DIR / "Assets" / "Icons" / "zzzlogo.png"
        if icon_path.exists():
            try:
                img = Image.open(icon_path)
                photo = ImageTk.PhotoImage(img)
                self.iconphoto(True, photo)
                self._icon_img = photo
            except Exception:
                pass

        self._init_style()
        self._current_section = None
        self._section_frames = {}
        self._action_buttons = []
        self._path_entry = None
        self._path_placeholders = {
            "Hash Character Mods Updater": "Drive:\\...\\ZZMI\\Mods",
            "Jane Doe Remapper": "Drive:\\...\\ZZMI\\Mods\\(Your_JaneDoe_Folder_Mod)",
            "Dialyn Remapper": "Drive:\\...\\ZZMI\\Mods\\(Your_Dialyn_Folder_Mod)",
            "Guides": "",
        }
        self._mod_paths = {
            "Hash Character Mods Updater": "",
            "Jane Doe Remapper": "",
            "Dialyn Remapper": "",
            "Guides": "",
        }
        self._config_path = _DATA_DIR / "Config" / "config.json"
        self._load_config()
        self._init_vars()
        self._init_layout()
        self._bind_sidebar_hover()
        self._apply_path_placeholder()

    def _init_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        bg = "#1e1e1e"
        fg = "#FFFFFF"
        panel = "#252526"
        accent = "#F68B2F"
        muted = "#B0B0B0"
        sidebar_bg = "#252526"
        sidebar_hover = "#2A2A2A"
        sidebar_active = "#252526"

        self.configure(background=bg)

        style.configure(".", background=bg, foreground=fg, fieldbackground=panel, bordercolor="#3e3e42", lightcolor="#3e3e42", darkcolor="#3e3e42", font=("Segoe UI", 9, "bold"))
        style.configure("TFrame", background=panel)
        style.configure("Panel.TFrame", background=panel)
        style.configure("Sidebar.TFrame", background=sidebar_bg)
        style.configure("TLabel", background=panel, foreground=fg, font=("Segoe UI", 9, "bold"))
        style.configure("Muted.TLabel", background=panel, foreground=muted, font=("Segoe UI", 9, "bold"))
        style.configure("Sidebar.TLabel", background=sidebar_bg, foreground=fg, font=("Segoe UI", 9, "bold"))
        style.configure("TButton", background=panel, foreground=fg, padding=(10, 6), font=("Segoe UI", 9, "bold"))
        style.configure("Topbar.TButton", background=panel, foreground=fg, padding=(8, 5), borderwidth=1, focusthickness=0, font=("Segoe UI", 9, "bold"))
        style.map("Topbar.TButton",
                  background=[("active", "#2d2d30"), ("hover", "#2d2d30")],
                  foreground=[("disabled", "#bbbbbb")],
                  focuscolor=[("", "")])
        style.configure("Accent.TButton", background="#F68B2F", foreground="#ffffff", borderwidth=0, focusthickness=0, padding=(12, 8), font=("Segoe UI", 9, "bold"))
        style.map("Accent.TButton", background=[("active", "#ff8c42")], foreground=[("disabled", "#bbbbbb")], focuscolor=[("", "")])
        style.configure("TEntry", fieldbackground=panel, font=("Segoe UI", 9, "bold"))
        style.configure("TCombobox", fieldbackground=panel, font=("Segoe UI", 9, "bold"))
        style.configure("TCheckbutton", background=panel, foreground="#ffffff", font=("Segoe UI", 9, "bold"))
        style.map("TCheckbutton",
                  background=[("active", "#2d2d30")],
                  foreground=[("active", "#ffffff")],
                  focuscolor=[("!focus", "")])
        style.configure("TNotebook", background=panel)
        style.configure("TNotebook.Tab", padding=(12, 8), font=("Segoe UI", 9, "bold"))

        self._bg = bg
        self._fg = fg
        self._panel = panel
        self._accent = accent
        self._muted = muted
        self._sidebar_bg = sidebar_bg
        self._sidebar_hover = sidebar_hover
        self._sidebar_active = sidebar_active

    def _load_config(self):
        default_data = {
            "active_section": "Hash Character Mods Updater",
            "mod_paths": {
                "Hash Character Mods Updater": {
                    "frame_hash_updater_path": "",
                    "ini_backup_folder": "",
                    "ini_checkbox_status": False,
                    "buf_backup_folder": "",
                    "buf_checkbox_status": False,
                },
                "Jane Doe Remapper": {
                    "frame_janedoe_remapper_path": "",
                    "buf_backup_folder": "",
                    "buf_checkbox_status": False,
                },
                "Dialyn Remapper": {
                    "frame_dialyn_remapper_path": "",
                    "buf_backup_folder": "",
                    "buf_checkbox_status": False,
                },
            },
        }
        try:
            if self._config_path.exists():
                with open(self._config_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if "mod_path" in data:
                    del data["mod_path"]
                if "mod_paths" in data:
                    for section, cfg in default_data["mod_paths"].items():
                        if section not in data["mod_paths"]:
                            data["mod_paths"][section] = cfg
                        elif not isinstance(data["mod_paths"][section], dict):
                            data["mod_paths"][section] = cfg
                        else:
                            merged_section = {
                                key: data["mod_paths"][section].get(key, default_val)
                                for key, default_val in cfg.items()
                            }
                            data["mod_paths"][section] = merged_section
                merged = {**default_data, **data}
                self._config = merged
                return
        except Exception:
            pass
        self._config = default_data

    def _save_config(self):
        try:
            self._config_path.parent.mkdir(parents=True, exist_ok=True)
            current_section = self._current_section or self._config.get("active_section", "Hash Character Mods Updater")
            self._config.pop("mod_path", None)
            self._config["active_section"] = current_section
            with open(self._config_path, "w", encoding="utf-8") as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
        except Exception as exc:
            print(f"Failed to save config: {exc}")

    def _init_vars(self):
        current_section = self._config.get("active_section", "Hash Character Mods Updater")
        mod_paths_cfg = self._config.get("mod_paths", {})
        self._mod_paths = {
            "Hash Character Mods Updater": mod_paths_cfg.get("Hash Character Mods Updater", {}).get("frame_hash_updater_path", ""),
            "Jane Doe Remapper": mod_paths_cfg.get("Jane Doe Remapper", {}).get("frame_janedoe_remapper_path", ""),
            "Dialyn Remapper": mod_paths_cfg.get("Dialyn Remapper", {}).get("frame_dialyn_remapper_path", ""),
            "Guides": "",
        }
        hash_cfg = mod_paths_cfg.get("Hash Character Mods Updater", {})
        janedoe_remapper_cfg = mod_paths_cfg.get("Jane Doe Remapper", {})
        dialyn_remapper_cfg = mod_paths_cfg.get("Dialyn Remapper", {})
        section_cfg = mod_paths_cfg.get(current_section, {})
        self.mod_path = tk.StringVar(value=section_cfg.get("frame_hash_updater_path" if current_section == "Hash Character Mods Updater" else "frame_janedoe_remapper_path" if current_section == "Jane Doe Remapper" else "frame_dialyn_remapper_path" if current_section == "Dialyn Remapper" else "", ""))
        # Hash Character Mods Updater exclusive vars
        self.ini_backup_folder = tk.StringVar(value=hash_cfg.get("ini_backup_folder", ""))
        self.ini_checkbox_status = tk.BooleanVar(value=bool(hash_cfg.get("ini_checkbox_status", False)))
        self.buf_backup_folder = tk.StringVar(value=hash_cfg.get("buf_backup_folder", ""))
        self.buf_checkbox_status = tk.BooleanVar(value=bool(hash_cfg.get("buf_checkbox_status", False)))
        # Remapper exclusive vars
        self.jane_remapper_buf_backup_folder = tk.StringVar(value=janedoe_remapper_cfg.get("buf_backup_folder", ""))
        self.jane_remapper_buf_checkbox_status = tk.BooleanVar(value=bool(janedoe_remapper_cfg.get("buf_checkbox_status", False)))
        self.dialyn_remapper_buf_backup_folder = tk.StringVar(value=dialyn_remapper_cfg.get("buf_backup_folder", ""))
        self.dialyn_remapper_buf_checkbox_status = tk.BooleanVar(value=bool(dialyn_remapper_cfg.get("buf_checkbox_status", False)))
        self.status_var = tk.StringVar(value="Active")
        self.progress_var = tk.DoubleVar(value=0.0)
        self.active_section_var = tk.StringVar(value="")

        self.ini_backup_folder.trace_add("write", lambda *args: self._on_setting_changed())
        self.buf_backup_folder.trace_add("write", lambda *args: self._on_setting_changed())
        self.jane_remapper_buf_backup_folder.trace_add("write", lambda *args: self._on_setting_changed())
        self.jane_remapper_buf_checkbox_status.trace_add("write", lambda *args: self._on_setting_changed())
        self.dialyn_remapper_buf_backup_folder.trace_add("write", lambda *args: self._on_setting_changed())
        self.dialyn_remapper_buf_checkbox_status.trace_add("write", lambda *args: self._on_setting_changed())

    def _init_layout(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        sidebar = ttk.Frame(self, style="Sidebar.TFrame")
        sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=(0, 0))
        sidebar.columnconfigure(0, weight=1)

        main = ttk.Frame(self)
        main.grid(row=0, column=1, sticky="nsew")
        main.columnconfigure(0, weight=1)
        main.rowconfigure(2, weight=1)
        main.rowconfigure(2, weight=1)

        topbar = ttk.Frame(main, padding=(12, 10), style="Panel.TFrame")
        topbar.grid(row=0, column=0, sticky="nsew", padx=(0, 0), pady=(0, 0))
        topbar.columnconfigure(1, weight=1)

        self._build_sidebar(sidebar)
        self._build_topbar(topbar)
        self._main_topbar = topbar
        sep1 = tk.Frame(main, height=6, bg="#1e1e1e")
        sep1.grid(row=1, column=0, sticky="ew")
        self._main_topbar_sep = sep1
        self._build_main_area(main)
        sep2 = tk.Frame(main, height=6, bg="#1e1e1e")
        sep2.grid(row=3, column=0, sticky="ew")
        self._build_log_area(main)

        initial = self._config.get("active_section", "Hash Character Mods Updater")
        if initial not in self._section_frames:
            initial = "Hash Character Mods Updater"
        self._show_section(initial)

    def _build_sidebar(self, parent):
        header = tk.Frame(parent, bg=self._sidebar_bg)
        header.grid(row=0, column=0, sticky="ew", pady=(15, 15))

        logo_path = _BASE_DIR / "Assets" / "Icons" / "zzzsidebarlogo.png"
        if logo_path.exists():
            try:
                img = Image.open(logo_path).convert("RGBA")
                sidebar_width = 220
                ratio = sidebar_width / img.width
                new_size = (sidebar_width, int(img.height * ratio))
                img = img.resize(new_size, Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                logo_label = tk.Label(header, image=photo, bg=self._sidebar_bg)
                logo_label.image = photo
                logo_label.pack(fill="both", expand=True)
            except Exception:
                pass

        top_sep = tk.Frame(parent, height=1, bg="#555555")
        top_sep.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        header_label = tk.Label(parent, text="MAIN", bg=self._sidebar_bg, fg="#FFFFFF", font=("Segoe UI", 9, "bold"), anchor="w")
        header_label.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 8))

        options = [
            ("Hash Character Mods Updater", "Updating All Mods Hashes"),
            ("Jane Doe Remapper", "Remapping Jane Doe Blend Indices"),
            ("Dialyn Remapper", "Remapping Dialyn Blend Indices"),
        ]

        self.sidebar_buttons = []
        self.sidebar_items = []
        self._sidebar_options = options

        active_section = self._config.get("active_section", "Hash Character Mods Updater")

        for idx, (title, desc) in enumerate(options, start=0):
            item_frame = tk.Frame(parent, bg=self._sidebar_bg)
            item_frame.grid(row=idx + 3, column=0, sticky="ew", padx=0, pady=0)
            item_frame.columnconfigure(1, weight=1)

            border_canvas = tk.Canvas(item_frame, width=0, bg=self._accent, highlightthickness=0)
            border_canvas.place(x=0, y=0, relheight=1)

            icon_canvas = tk.Canvas(item_frame, width=20, height=20, bg=self._sidebar_bg, highlightthickness=0)
            icon_canvas.grid(row=0, column=0, padx=(12, 8), pady=8)
            
            if title == active_section:
                self._draw_hash_icon(icon_canvas, self._accent)
            else:
                self._draw_diamond_icon(icon_canvas, self._accent)

            text_frame = tk.Frame(item_frame, bg=self._sidebar_bg)
            text_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 12), pady=8)

            title_label = tk.Label(text_frame, text=title, bg=self._sidebar_bg, fg=self._fg, font=("Segoe UI", 9, "bold"), anchor="w")
            title_label.pack(fill="x")

            desc_label = tk.Label(text_frame, text=desc, bg=self._sidebar_bg, fg=self._muted, font=("Segoe UI", 8), anchor="w")
            desc_label.pack(fill="x")

            for widget in [item_frame, icon_canvas, text_frame, title_label, desc_label]:
                widget.bind("<Enter>", lambda e, i=idx: self._on_sidebar_item_enter(i))
                widget.bind("<Leave>", lambda e, i=idx: self._on_sidebar_item_leave(i))
                widget.bind("<Button-1>", lambda e, t=title: self._on_sidebar_click(t))

            self.sidebar_buttons.append(item_frame)
            self.sidebar_items.append({
                "frame": item_frame,
                "border": border_canvas,
                "icon": icon_canvas,
                "title": title_label,
                "desc": desc_label,
                "text_frame": text_frame,
                "title_text": title,
                "index": idx,
            })

        guide_label = tk.Label(parent, text="GUIDE", bg=self._sidebar_bg, fg="#FFFFFF", font=("Segoe UI", 9, "bold"), anchor="w")
        guide_label.grid(row=7, column=0, sticky="ew", padx=12, pady=(28, 8))

        guides_title = "Guides"
        guides_desc = "How To Use the Tool"
        guides_item_frame = tk.Frame(parent, bg=self._sidebar_bg)
        guides_item_frame.grid(row=8, column=0, sticky="ew", padx=0, pady=0)
        guides_item_frame.columnconfigure(1, weight=1)

        guides_border = tk.Canvas(guides_item_frame, width=0, bg=self._accent, highlightthickness=0)
        guides_border.place(x=0, y=0, relheight=1)

        guides_icon = tk.Canvas(guides_item_frame, width=20, height=20, bg=self._sidebar_bg, highlightthickness=0)
        guides_icon.grid(row=0, column=0, padx=(12, 8), pady=8)

        if guides_title == active_section:
            self._draw_hash_icon(guides_icon, self._accent)
        else:
            self._draw_diamond_icon(guides_icon, self._accent)

        guides_text_frame = tk.Frame(guides_item_frame, bg=self._sidebar_bg)
        guides_text_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 12), pady=8)

        guides_title_label = tk.Label(guides_text_frame, text=guides_title, bg=self._sidebar_bg, fg=self._fg, font=("Segoe UI", 9, "bold"), anchor="w")
        guides_title_label.pack(fill="x")

        guides_desc_label = tk.Label(guides_text_frame, text=guides_desc, bg=self._sidebar_bg, fg=self._muted, font=("Segoe UI", 8), anchor="w")
        guides_desc_label.pack(fill="x")

        for widget in [guides_item_frame, guides_icon, guides_text_frame, guides_title_label, guides_desc_label]:
            widget.bind("<Enter>", lambda e, i=len(self.sidebar_items): self._on_sidebar_item_enter(i))
            widget.bind("<Leave>", lambda e, i=len(self.sidebar_items): self._on_sidebar_item_leave(i))
            widget.bind("<Button-1>", lambda e, t=guides_title: self._on_sidebar_click(t))

        self.sidebar_buttons.append(guides_item_frame)
        self.sidebar_items.append({
            "frame": guides_item_frame,
            "border": guides_border,
            "icon": guides_icon,
            "title": guides_title_label,
            "desc": guides_desc_label,
            "text_frame": guides_text_frame,
            "title_text": guides_title,
            "index": len(self.sidebar_items),
        })

        parent.rowconfigure(9, weight=1)

        bottom_frame = tk.Frame(parent, bg=self._sidebar_bg)
        bottom_frame.grid(row=10, column=0, sticky="ew", padx=0, pady=(0, 10))
        bottom_frame.columnconfigure(0, weight=1)

        bottom_sep = tk.Frame(bottom_frame, height=1, bg="#555555")
        bottom_sep.pack(fill="x", padx=0, pady=(0, 10))

        version_label = tk.Label(bottom_frame, text="v2.0.0 GUI", bg=self._sidebar_bg, fg=self._muted, font=("Segoe UI", 8), anchor="w")
        version_label.pack(fill="x", padx=12)

    def _bind_sidebar_hover(self):
        pass

    def _on_sidebar_item_enter(self, idx):
        item = self.sidebar_items[idx]
        if item["title_text"] == self._current_section:
            return
        bg = self._sidebar_hover
        item["frame"].configure(bg=bg)
        item["border"].configure(width=0)
        item["icon"].configure(bg=bg)
        item["text_frame"].configure(bg=bg)
        item["title"].configure(bg=bg)
        item["desc"].configure(bg=bg)

    def _on_sidebar_item_leave(self, idx):
        item = self.sidebar_items[idx]
        if item["title_text"] == self._current_section:
            bg = self._sidebar_active
            item["border"].configure(width=3)
        else:
            bg = self._sidebar_bg
            item["border"].configure(width=0)
        item["frame"].configure(bg=bg)
        item["icon"].configure(bg=bg)
        item["text_frame"].configure(bg=bg)
        item["title"].configure(bg=bg)
        item["desc"].configure(bg=bg)

    def _update_sidebar_active_state(self, active_title):
        for idx, item in enumerate(self.sidebar_items):
            if item["title_text"] == active_title:
                bg = self._sidebar_active
                item["border"].configure(width=3)
                self._draw_hash_icon(item["icon"], self._accent)
            else:
                bg = self._sidebar_bg
                item["border"].configure(width=0)
                self._draw_diamond_icon(item["icon"], self._accent)
            item["frame"].configure(bg=bg)
            item["icon"].configure(bg=bg)
            item["text_frame"].configure(bg=bg)
            item["title"].configure(bg=bg)
            item["desc"].configure(bg=bg)

    def _build_topbar(self, parent):
        ttk.Label(parent, text="Target Folder:").grid(row=0, column=0, sticky="w")

        entry_wrapper = tk.Frame(parent, bg="#3e3e42", padx=1, pady=1)
        entry_wrapper.grid(row=0, column=1, sticky="ew", padx=(10, 10))

        self._path_entry = tk.Entry(entry_wrapper, textvariable=self.mod_path, bg="#252526", fg="#f0f0f0", insertbackground="#f0f0f0", relief="flat", highlightthickness=0, readonlybackground="#252526", borderwidth=0, font=("Segoe UI", 9, "bold"))
        self._path_entry.pack(fill="both", expand=True)
        self._path_entry.configure(state="readonly")

        ttk.Button(parent, text="Browse", style="Topbar.TButton", command=self._browse_folder).grid(row=0, column=2, sticky="e")
        ttk.Button(parent, text="Refresh", style="Topbar.TButton", command=self._refresh_folder).grid(row=0, column=3, sticky="e", padx=(6, 0))

        self.mod_path.trace_add("write", lambda *args: self._on_mod_path_changed())
        self._path_entry.bind("<FocusIn>", self._on_path_focus_in)
        self._path_entry.bind("<FocusOut>", self._on_path_focus_out)
        self.bind("<Button-1>", self._on_window_click)

    def _build_main_area(self, parent):
        container = ttk.Frame(parent)
        container.grid(row=2, column=0, sticky="nsew")
        container.columnconfigure(0, weight=1)
        container.columnconfigure(2, weight=1)
        container.rowconfigure(0, weight=1)

        left = ttk.Frame(container, padding=(12, 12), style="Panel.TFrame")
        left.grid(row=0, column=0, sticky="nsew")
        left.columnconfigure(0, weight=1)

        sep = tk.Frame(container, width=6, bg="#1e1e1e")
        sep.grid(row=0, column=1, sticky="ns")

        right = ttk.Frame(container, padding=(12, 12), style="Panel.TFrame")
        right.grid(row=0, column=2, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(0, weight=1)

        self.left_container = left
        self.right_container = right
        self._main_sep = sep

        self._build_hash_updater_content(left, right)
        self._build_jane_doe_remapper_content(left, right)
        self._build_dialyn_remapper_content(left, right)
        self._build_guides_content(left, right)

    def _build_hash_updater_content(self, left_parent, right_parent):
        left_widgets = []

        ini_checkbox = tk.Checkbutton(left_parent, text="Create INI Backup Folder", variable=self.ini_checkbox_status, bg="#252526", fg="#ffffff", selectcolor="#252526", activebackground="#2d2d30", activeforeground="#ffffff", highlightthickness=0, takefocus=0, relief="flat", bd=0, font=("Segoe UI", 9, "bold"), command=lambda: self._on_checkbox_clicked("Create INI Backup Folder", self.ini_checkbox_status, self._on_hash_ini_toggle))
        self._add_checkbox_hover(ini_checkbox)
        left_widgets.append({"widget": ini_checkbox, "options": {"row": 0, "column": 0, "sticky": "w"}})

        lbl = ttk.Label(left_parent, text="Path To Decided Folder To Backup INI")
        left_widgets.append({"widget": lbl, "options": {"row": 1, "column": 0, "sticky": "w"}})

        ini_entry_wrapper = tk.Frame(left_parent, bg="#3e3e42", padx=1, pady=1)
        ini_entry_wrapper.grid(row=2, column=0, sticky="ew", pady=(5, 30))
        ini_entry_wrapper.columnconfigure(0, weight=1)

        ini_entry = tk.Entry(ini_entry_wrapper, textvariable=self.ini_backup_folder, bg="#252526", fg="#f0f0f0", insertbackground="#f0f0f0", relief="flat", highlightthickness=0, readonlybackground="#252526", borderwidth=0, font=("Segoe UI", 9, "bold"))
        ini_entry.grid(row=0, column=0, sticky="ew")

        ini_icon_frame = tk.Frame(ini_entry_wrapper, bg="#252526")
        ini_icon_frame.grid(row=0, column=1, sticky="ns")

        ini_folder_icon = self._create_folder_icon_canvas(ini_icon_frame, lambda: self._browse_backup_folder("ini"), tooltip="Browse INI Backup Folder")
        ini_folder_icon.pack(side="left", padx=(3, 1))

        ini_refresh_icon = self._create_refresh_icon_canvas(ini_icon_frame, lambda: self._refresh_backup_folder("ini"), tooltip="Refresh INI Backup Folder")
        ini_refresh_icon.pack(side="left", padx=(1, 3))

        left_widgets.append({"widget": ini_entry_wrapper, "options": {"row": 2, "column": 0, "sticky": "ew", "pady": (5, 30)}})

        buf_checkbox = tk.Checkbutton(left_parent, text="Create BUF Backup Folder", variable=self.buf_checkbox_status, bg="#252526", fg="#ffffff", selectcolor="#252526", activebackground="#2d2d30", activeforeground="#ffffff", highlightthickness=0, takefocus=0, relief="flat", bd=0, font=("Segoe UI", 9, "bold"), command=lambda: self._on_checkbox_clicked("Create BUF Backup Folder", self.buf_checkbox_status, self._on_hash_buf_toggle))
        self._add_checkbox_hover(buf_checkbox)
        left_widgets.append({"widget": buf_checkbox, "options": {"row": 3, "column": 0, "sticky": "w"}})

        lb2 = ttk.Label(left_parent, text="Path To Decided Folder To Backup BUF")
        left_widgets.append({"widget": lb2, "options": {"row": 4, "column": 0, "sticky": "w"}})

        buf_entry_wrapper = tk.Frame(left_parent, bg="#3e3e42", padx=1, pady=1)
        buf_entry_wrapper.grid(row=5, column=0, sticky="ew", pady=(4, 10))
        buf_entry_wrapper.columnconfigure(0, weight=1)

        buf_entry = tk.Entry(buf_entry_wrapper, textvariable=self.buf_backup_folder, bg="#252526", fg="#f0f0f0", insertbackground="#f0f0f0", relief="flat", highlightthickness=0, readonlybackground="#252526", borderwidth=0, font=("Segoe UI", 9, "bold"))
        buf_entry.grid(row=0, column=0, sticky="ew")

        buf_icon_frame = tk.Frame(buf_entry_wrapper, bg="#252526")
        buf_icon_frame.grid(row=0, column=1, sticky="ns")

        buf_folder_icon = self._create_folder_icon_canvas(buf_icon_frame, lambda: self._browse_backup_folder("buf"), tooltip="Browse BUF Backup Folder")
        buf_folder_icon.pack(side="left", padx=(3, 1))

        buf_refresh_icon = self._create_refresh_icon_canvas(buf_icon_frame, lambda: self._refresh_backup_folder("buf"), tooltip="Refresh BUF Backup Folder")
        buf_refresh_icon.pack(side="left", padx=(1, 3))

        left_widgets.append({"widget": buf_entry_wrapper, "options": {"row": 5, "column": 0, "sticky": "ew", "pady": (4, 10)}})

        btn = ttk.Button(left_parent, text="Update Hashes", style="Accent.TButton", command=self._run_update_hashes)
        left_widgets.append({"widget": btn, "options": {"row": 6, "column": 0, "sticky": "ew", "pady": (16, 4)}})
        self._action_buttons.append(btn)

        clear_btn = ttk.Button(left_parent, text="Clear CLI", style="Accent.TButton", command=self._clear_cli_action)
        left_widgets.append({"widget": clear_btn, "options": {"row": 7, "column": 0, "sticky": "ew", "pady": (4, 4)}})
        self._action_buttons.append(clear_btn)

        info = ttk.Frame(right_parent)
        info.columnconfigure(0, weight=1)
        info.rowconfigure(1, weight=1)

        ttk.Label(info, text="CLI Output").grid(row=0, column=0, sticky="w")

        cli_frame = tk.Frame(info, bg="#0c0c0c")
        cli_frame.grid(row=1, column=0, sticky="nsew")
        cli_frame.columnconfigure(0, weight=1)
        cli_frame.rowconfigure(0, weight=1)

        self.hash_cli_output = tk.Text(cli_frame, bg="#0c0c0c", fg="#e6e6e6", insertbackground="#e6e6e6", relief="flat", wrap="word", font=("Consolas", 9), exportselection=True)
        self.hash_cli_output.grid(row=0, column=0, sticky="nsew")
        self.hash_cli_output.config(state="disabled")
        self.hash_cli_output.bind("<<Paste>>", lambda e: "break")

        cli_scroll = ttk.Scrollbar(cli_frame, orient="vertical", command=self.hash_cli_output.yview)
        cli_scroll.grid(row=0, column=1, sticky="ns")
        self.hash_cli_output.configure(yscrollcommand=cli_scroll.set)
        cli_scroll.grid_remove()
        self._cli_scroll = cli_scroll

        self._section_frames["Hash Character Mods Updater"] = {
            "left_widgets": left_widgets,
            "right": info,
            "ini_entry": ini_entry,
            "buf_entry": buf_entry,
            "ini_icons": {"folder": ini_folder_icon, "refresh": ini_refresh_icon, "frame": ini_icon_frame},
            "buf_icons": {"folder": buf_folder_icon, "refresh": buf_refresh_icon, "frame": buf_icon_frame},
            "hash_cli_output": self.hash_cli_output,
        }

        self._on_hash_ini_toggle()
        self._on_hash_buf_toggle()

    def _build_jane_doe_remapper_content(self, left_parent, right_parent):
        left_widgets = []

        buf_checkbox = tk.Checkbutton(left_parent, text="Create BUF Backup Folder", variable=self.jane_remapper_buf_checkbox_status, bg="#252526", fg="#ffffff", selectcolor="#252526", activebackground="#2d2d30", activeforeground="#ffffff", highlightthickness=0, takefocus=0, relief="flat", bd=0, font=("Segoe UI", 9, "bold"), command=lambda: self._on_checkbox_clicked("Create BUF Backup Folder", self.jane_remapper_buf_checkbox_status, self._on_jane_remapper_buf_toggle))
        self._add_checkbox_hover(buf_checkbox)
        left_widgets.append({"widget": buf_checkbox, "options": {"row": 0, "column": 0, "sticky": "w"}})

        lb2 = ttk.Label(left_parent, text="Path To Decided Folder To Backup BUF")
        left_widgets.append({"widget": lb2, "options": {"row": 1, "column": 0, "sticky": "w"}})

        buf_entry_wrapper = tk.Frame(left_parent, bg="#3e3e42", padx=1, pady=1)
        buf_entry_wrapper.grid(row=2, column=0, sticky="ew", pady=(4, 10))
        buf_entry_wrapper.columnconfigure(0, weight=1)

        buf_entry = tk.Entry(buf_entry_wrapper, textvariable=self.jane_remapper_buf_backup_folder, bg="#252526", fg="#f0f0f0", insertbackground="#f0f0f0", relief="flat", highlightthickness=0, readonlybackground="#252526", borderwidth=0, font=("Segoe UI", 9, "bold"))
        buf_entry.grid(row=0, column=0, sticky="ew")

        buf_icon_frame = tk.Frame(buf_entry_wrapper, bg="#252526")
        buf_icon_frame.grid(row=0, column=1, sticky="ns")

        buf_folder_icon = self._create_folder_icon_canvas(buf_icon_frame, lambda: self._browse_backup_folder("jane_remapper_buf"), tooltip="Browse BUF Backup Folder")
        buf_folder_icon.pack(side="left", padx=(3, 1))

        buf_refresh_icon = self._create_refresh_icon_canvas(buf_icon_frame, lambda: self._refresh_backup_folder("jane_remapper_buf"), tooltip="Refresh BUF Backup Folder")
        buf_refresh_icon.pack(side="left", padx=(1, 3))

        left_widgets.append({"widget": buf_entry_wrapper, "options": {"row": 2, "column": 0, "sticky": "ew", "pady": (4, 10)}})

        btn = ttk.Button(left_parent, text="Remap Now", style="Accent.TButton", command=self._run_jane_remapper)
        left_widgets.append({"widget": btn, "options": {"row": 3, "column": 0, "sticky": "ew", "pady": (16, 4)}})
        self._action_buttons.append(btn)

        clear_btn = ttk.Button(left_parent, text="Clear CLI", style="Accent.TButton", command=self._clear_cli_action)
        left_widgets.append({"widget": clear_btn, "options": {"row": 4, "column": 0, "sticky": "ew", "pady": (4, 4)}})
        self._action_buttons.append(clear_btn)

        jane_note = self._create_satan1c_note(left_parent)
        left_widgets.append({"widget": jane_note, "options": {"row": 5, "column": 0, "sticky": "ew", "pady": (10, 4)}})

        info = ttk.Frame(right_parent)
        info.columnconfigure(0, weight=1)
        info.rowconfigure(1, weight=1)

        ttk.Label(info, text="CLI Output").grid(row=0, column=0, sticky="w")

        cli_frame = tk.Frame(info, bg="#0c0c0c")
        cli_frame.grid(row=1, column=0, sticky="nsew")
        cli_frame.columnconfigure(0, weight=1)
        cli_frame.rowconfigure(0, weight=1)

        cli_output = tk.Text(cli_frame, bg="#0c0c0c", fg="#e6e6e6", insertbackground="#e6e6e6", relief="flat", wrap="word", font=("Consolas", 9), exportselection=True)
        cli_output.grid(row=0, column=0, sticky="nsew")
        cli_output.config(state="disabled")
        cli_output.bind("<<Paste>>", lambda e: "break")

        cli_scroll = ttk.Scrollbar(cli_frame, orient="vertical", command=cli_output.yview)
        cli_scroll.grid(row=0, column=1, sticky="ns")
        cli_output.configure(yscrollcommand=cli_scroll.set)
        cli_scroll.grid_remove()

        self._section_frames["Jane Doe Remapper"] = {
            "left_widgets": left_widgets,
            "right": info,
            "buf_entry": buf_entry,
            "buf_icons": {"folder": buf_folder_icon, "refresh": buf_refresh_icon, "frame": buf_icon_frame},
            "hash_cli_output": cli_output,
            "_cli_scroll": cli_scroll,
        }

        self._on_jane_remapper_buf_toggle()

    def _build_dialyn_remapper_content(self, left_parent, right_parent):
        left_widgets = []

        buf_checkbox = tk.Checkbutton(left_parent, text="Create BUF Backup Folder", variable=self.dialyn_remapper_buf_checkbox_status, bg="#252526", fg="#ffffff", selectcolor="#252526", activebackground="#2d2d30", activeforeground="#ffffff", highlightthickness=0, takefocus=0, relief="flat", bd=0, font=("Segoe UI", 9, "bold"), command=lambda: self._on_checkbox_clicked("Create BUF Backup Folder", self.dialyn_remapper_buf_checkbox_status, self._on_dialyn_remapper_buf_toggle))
        self._add_checkbox_hover(buf_checkbox)
        left_widgets.append({"widget": buf_checkbox, "options": {"row": 0, "column": 0, "sticky": "w"}})

        lb2 = ttk.Label(left_parent, text="Path To Decided Folder To Backup BUF")
        left_widgets.append({"widget": lb2, "options": {"row": 1, "column": 0, "sticky": "w"}})

        buf_entry_wrapper = tk.Frame(left_parent, bg="#3e3e42", padx=1, pady=1)
        buf_entry_wrapper.grid(row=2, column=0, sticky="ew", pady=(4, 10))
        buf_entry_wrapper.columnconfigure(0, weight=1)

        buf_entry = tk.Entry(buf_entry_wrapper, textvariable=self.dialyn_remapper_buf_backup_folder, bg="#252526", fg="#f0f0f0", insertbackground="#f0f0f0", relief="flat", highlightthickness=0, readonlybackground="#252526", borderwidth=0, font=("Segoe UI", 9, "bold"))
        buf_entry.grid(row=0, column=0, sticky="ew")

        buf_icon_frame = tk.Frame(buf_entry_wrapper, bg="#252526")
        buf_icon_frame.grid(row=0, column=1, sticky="ns")

        buf_folder_icon = self._create_folder_icon_canvas(buf_icon_frame, lambda: self._browse_backup_folder("dialyn_remapper_buf"), tooltip="Browse BUF Backup Folder")
        buf_folder_icon.pack(side="left", padx=(3, 1))

        buf_refresh_icon = self._create_refresh_icon_canvas(buf_icon_frame, lambda: self._refresh_backup_folder("dialyn_remapper_buf"), tooltip="Refresh BUF Backup Folder")
        buf_refresh_icon.pack(side="left", padx=(1, 3))

        left_widgets.append({"widget": buf_entry_wrapper, "options": {"row": 2, "column": 0, "sticky": "ew", "pady": (4, 10)}})

        btn = ttk.Button(left_parent, text="Remap Now", style="Accent.TButton", command=self._run_dialyn_remapper)
        left_widgets.append({"widget": btn, "options": {"row": 3, "column": 0, "sticky": "ew", "pady": (16, 4)}})
        self._action_buttons.append(btn)

        clear_btn = ttk.Button(left_parent, text="Clear CLI", style="Accent.TButton", command=self._clear_cli_action)
        left_widgets.append({"widget": clear_btn, "options": {"row": 4, "column": 0, "sticky": "ew", "pady": (4, 4)}})
        self._action_buttons.append(clear_btn)

        dialyn_note = self._create_satan1c_note(left_parent)
        left_widgets.append({"widget": dialyn_note, "options": {"row": 5, "column": 0, "sticky": "ew", "pady": (10, 4)}})

        info = ttk.Frame(right_parent)
        info.columnconfigure(0, weight=1)
        info.rowconfigure(1, weight=1)

        ttk.Label(info, text="CLI Output").grid(row=0, column=0, sticky="w")

        cli_frame = tk.Frame(info, bg="#0c0c0c")
        cli_frame.grid(row=1, column=0, sticky="nsew")
        cli_frame.columnconfigure(0, weight=1)
        cli_frame.rowconfigure(0, weight=1)

        cli_output = tk.Text(cli_frame, bg="#0c0c0c", fg="#e6e6e6", insertbackground="#e6e6e6", relief="flat", wrap="word", font=("Consolas", 9), exportselection=True)
        cli_output.grid(row=0, column=0, sticky="nsew")
        cli_output.config(state="disabled")
        cli_output.bind("<<Paste>>", lambda e: "break")

        cli_scroll = ttk.Scrollbar(cli_frame, orient="vertical", command=cli_output.yview)
        cli_scroll.grid(row=0, column=1, sticky="ns")
        cli_output.configure(yscrollcommand=cli_scroll.set)
        cli_scroll.grid_remove()

        self._section_frames["Dialyn Remapper"] = {
            "left_widgets": left_widgets,
            "right": info,
            "buf_entry": buf_entry,
            "buf_icons": {"folder": buf_folder_icon, "refresh": buf_refresh_icon, "frame": buf_icon_frame},
            "hash_cli_output": cli_output,
            "_cli_scroll": cli_scroll,
        }

        self._on_dialyn_remapper_buf_toggle()

    def _build_guides_content(self, left_parent, right_parent):
        info = ttk.Frame(right_parent)
        info.columnconfigure(0, weight=1)
        info.rowconfigure(0, weight=1)

        guides_path = _BASE_DIR / "Assets" / "Guide" / "GUIDES.md"

        try:
            from tkinterweb import HtmlFrame
            import markdown
            import re

            frame = HtmlFrame(info, messages_enabled=False, vertical_scrollbar="auto", horizontal_scrollbar="auto")
            frame.grid(row=0, column=0, sticky="nsew")

            if guides_path.exists():
                with open(guides_path, "r", encoding="utf-8") as f:
                    raw = f.read()

                # Pre-process: GitHub-style callouts > [!TYPE] → styled HTML div
                callout_cfg = {
                    "NOTE":     ("#1f6feb", "#388bfd", "&#x2139; NOTE"),
                    "TIP":      ("#1a7f37", "#3fb950", "&#9889; TIP"),         # Use Sparkles (✨) if the light bulb icon renders blank
                    "WARNING":  ("#9e6a03", "#d29922", "&#x26A0; WARNING"),
                    "CAUTION":  ("#b62324", "#f85149", "&#x26D4; CAUTION"),       # Use No Entry (⛔) as it renders more reliably
                    "IMPORTANT":("#6639ba", "#ab7df8", "&#x1F4CC; IMPORTANT"),
                }


                def replace_callout(m):
                    ctype  = m.group(1).upper()
                    body   = m.group(2)
                    # Strip leading '> ' from each body line
                    body   = re.sub(r"^> ?", "", body, flags=re.MULTILINE).strip()
                    cfg    = callout_cfg.get(ctype, ("#555555", "#aaaaaa", f"&#x26D4; {ctype}"))
                    # Process markdown on body so bold/code renders correctly
                    body_html = markdown.markdown(body, extensions=["fenced_code"])
                    return (
                        f'<div style="'
                        f'border-left:4px solid {cfg[0]};'
                        f'background:#161b22;'
                        f'padding:10px 16px;'
                        f'margin:14px 0;'
                        f'border-radius:0 6px 6px 0;'
                        f'">'
                        f'<p style="margin:0 0 6px 0;font-weight:bold;color:{cfg[1]}">{cfg[2]}</p>'
                        f'{body_html}'
                        f'</div>'
                    )

                raw = re.sub(
                    r"> \[!(NOTE|TIP|WARNING|CAUTION|IMPORTANT)\]\n((?:>.*\n?)*)",
                    replace_callout,
                    raw
                )

                html_body = markdown.markdown(
                    raw,
                    extensions=["tables", "fenced_code", "nl2br"]
                )

                # Pre-process: replace fenced code blocks (```) with styled <div>
                def replace_fenced_code(m):
                    code = m.group(1)
                    code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                    return (
                        '<div style="background:#161b22;border:1px solid #30363d;'
                        'border-radius:6px;padding:12px 16px;margin:12px 0;'
                        'font-family:Consolas,Courier New,monospace;font-size:13px;'
                        'color:#e6edf3;line-height:1.5;white-space:pre-wrap;'
                        'word-wrap:break-word">'
                        f'{code}'
                        '</div>'
                    )
                raw = re.sub(r'```(?:\w*)\n(.*?)```', replace_fenced_code, raw, flags=re.DOTALL)

                html_body = markdown.markdown(
                    raw,
                    extensions=["tables", "fenced_code", "nl2br"]
                )

                github_css = """
                    * { box-sizing: border-box; }
                    body {
                        font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
                        font-size: 14px;
                        line-height: 1.7;
                        color: #e6edf3;
                        background-color: #0d1117;
                        padding: 28px 36px;
                        margin: 0;
                    }
                    h1 {
                        font-size: 2em;
                        font-weight: 700;
                        padding-bottom: 8px;
                        margin-top: 0;
                        margin-bottom: 16px;
                        border-bottom: 1px solid #30363d;
                        color: #e6edf3;
                    }
                    h2 {
                        font-size: 1.4em;
                        font-weight: 600;
                        padding-bottom: 6px;
                        margin-top: 28px;
                        margin-bottom: 12px;
                        border-bottom: 1px solid #30363d;
                        color: #e6edf3;
                    }
                    h3 {
                        font-size: 1.1em;
                        font-weight: 600;
                        margin-top: 20px;
                        margin-bottom: 8px;
                        color: #e6edf3;
                    }
                    p { margin: 8px 0 12px 0; }
                    a { color: #58a6ff; text-decoration: none; }
                    a:hover { text-decoration: underline; }
                    strong { color: #e6edf3; font-weight: 600; }
                    em { color: #e6edf3; }
                    code {
                        background: #161b22;
                        border: 1px solid #30363d;
                        border-radius: 4px;
                        padding: 2px 6px;
                        font-family: "Consolas", "Courier New", monospace;
                        font-size: 85%;
                        color: #f78166;
                    }
                    pre {
                        background: #161b22;
                        border: 1px solid #30363d;
                        border-radius: 6px;
                        padding: 16px;
                        margin: 14px 0;
                        overflow-x: auto;
                    }
                    pre code {
                        background: none;
                        border: none;
                        padding: 0;
                        color: #e6edf3;
                        font-size: 13px;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%;
                        margin: 16px 0;
                        font-size: 13px;
                    }
                    th {
                        background: #161b22;
                        color: #e6edf3;
                        font-weight: 600;
                        border: 1px solid #30363d;
                        padding: 8px 14px;
                        text-align: center;
                    }
                    td {
                        border: 1px solid #30363d;
                        padding: 8px 14px;
                        color: #e6edf3;
                    }
                    tr:nth-child(even) td { background: #161b22; }
                    tr:nth-child(odd)  td { background: #0d1117; }
                    blockquote {
                        border-left: 4px solid #30363d;
                        margin: 10px 0;
                        padding: 4px 16px;
                        color: #8b949e;
                    }
                    hr {
                        border: none;
                        border-top: 5px solid #30363d;
                        margin: 24px 0;
                    }
                    ul, ol {
                        padding-left: 24px;
                        margin: 8px 0 12px 0;
                    }
                    li { margin: 4px 0; }
                """

                full_html = (
                    "<!DOCTYPE html><html><head>"
                    "<meta charset='utf-8'>"
                    f"<style>{github_css}</style>"
                    "</head><body>"
                    f"{html_body}"
                    "</body></html>"
                )

                frame.load_html(full_html)

            else:
                error_html = (
                    "<!DOCTYPE html><html><head><meta charset='utf-8'>"
                    "<style>body{font-family:'Segoe UI',sans-serif;background:#0d1117;"
                    "color:#e6edf3;padding:32px;} h2{color:#f85149;} code{background:#161b22;"
                    "padding:2px 6px;border-radius:4px;color:#f78166;}</style></head><body>"
                    "<h2>⚠️ GUIDES.md Not Found</h2>"
                    f"<p>File not found at path:</p>"
                    f"<p><code>Assets/Guide/GUIDES.md</code></p>"
                    "<p>Please make sure <code>GUIDES.md</code> exists inside the "
                    "<code>Assets/Guide/</code> folder in this tool's directory.</p>"
                    "</body></html>"
                )
                frame.load_html(error_html)

        except ImportError as e:
            # Fallback: plain tk.Text if tkinterweb / markdown is not installed
            missing = "tkinterweb" if "tkinterweb" in str(e) else "markdown"

            fallback_outer = tk.Frame(info, bg="#0d1117")
            fallback_outer.grid(row=0, column=0, sticky="nsew")
            fallback_outer.columnconfigure(0, weight=1)
            fallback_outer.rowconfigure(1, weight=1)

            warn_lbl = tk.Label(
                fallback_outer,
                text=f"⚠️  Library '{missing}' is not installed. Falling back to plain text.\n"
                    f"Run:  pip install tkinterweb markdown",
                bg="#161b22", fg="#d29922",
                font=("Segoe UI", 9), anchor="w", padx=12, pady=8
            )
            warn_lbl.grid(row=0, column=0, sticky="ew")

            fallback = tk.Text(
                fallback_outer,
                bg="#0d1117", fg="#e6edf3",
                relief="flat", wrap="word",
                font=("Segoe UI", 10),
                padx=20, pady=16,
                insertbackground="#e6edf3"
            )
            fallback.grid(row=1, column=0, sticky="nsew")

            scroll = ttk.Scrollbar(fallback_outer, orient="vertical", command=fallback.yview)
            scroll.grid(row=1, column=1, sticky="ns")
            fallback.configure(yscrollcommand=scroll.set)

            if guides_path.exists():
                content = guides_path.read_text(encoding="utf-8")
            else:
                content = "GUIDES.md not found at Assets/Guide/GUIDES.md"
            fallback.insert("1.0", content)
            fallback.configure(state="disabled")

        self._section_frames["Guides"] = {
            "left_widgets": [],
            "right": info,
        }

    def _create_satan1c_note(self, parent):
        """
        Creates a flexible (word-wrap) 'Satan1c Repository' note widget
        with a clickable hyperlink that opens the browser.
        Used in Jane Doe Remapper and Dialyn Remapper.
        """
        _NOTE_URL  = "https://github.com/Satan1c/ZZMI_tools/wiki/Jane-2.5-fix"
        _NOTE_BG   = "#252526"
        _NOTE_FG   = "#888888"
        _LINK_FG   = "#F68B2F"
        _NOTE_FONT = ("Segoe UI", 8)

        container = tk.Frame(parent, bg=_NOTE_BG)
        container.columnconfigure(0, weight=1)

        txt = tk.Text(
            container,
            bg=_NOTE_BG,
            fg=_NOTE_FG,
            font=_NOTE_FONT,
            relief="flat",
            wrap="word",
            cursor="arrow",
            highlightthickness=0,
            borderwidth=0,
            width=1,
            height=1,
            exportselection=False,
            padx=0,
            pady=2,
        )
        txt.grid(row=0, column=0, sticky="ew")

        # --- note text content ---
        _PREFIX = (
            "NOTE: Before using this tool, it is recommended to visit the creator\u2019s "
            "GitHub repository to gain a deeper understanding of the underlying logic "
            "and avoid any errors.\u00a0\u00a0"
        )
        _LINK_LABEL = "Satan1c Repository"

        txt.insert("end", _PREFIX)
        txt.insert("end", _LINK_LABEL, "link")

        # hyperlink tag — underline only appears on hover
        txt.tag_config("link", foreground=_LINK_FG, underline=False)
        txt.tag_bind("link", "<Button-1>",
                     lambda e, url=_NOTE_URL: webbrowser.open(url))
        txt.tag_bind("link", "<Enter>",
                     lambda e: (txt.tag_config("link", underline=True), txt.config(cursor="hand2")))
        txt.tag_bind("link", "<Leave>",
                     lambda e: (txt.tag_config("link", underline=False), txt.config(cursor="arrow")))

        txt.config(state="disabled")

        # --- auto-resize height when width changes ---
        def _auto_height(event=None, _txt=txt):
            _txt.config(state="normal")
            _txt.update_idletasks()
            try:
                result = _txt.count("1.0", "end", "displaylines")
                lines = result[0] if isinstance(result, tuple) else result
                if not lines or lines < 1:
                    lines = 1
            except Exception:
                lines = 4
            _txt.config(height=lines, state="disabled")

        txt.bind("<Configure>", _auto_height)

        return container

    def _build_log_area(self, parent):
        bottom = ttk.Frame(parent, style="Panel.TFrame")
        bottom.grid(row=4, column=0, sticky="nsew", pady=(0, 0))
        bottom.rowconfigure(1, weight=1)
        bottom.columnconfigure(0, weight=1)

        header = ttk.Frame(bottom)
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="Log Activity").grid(row=0, column=0, sticky="w")
        ttk.Label(header, textvariable=self.status_var, style="Muted.TLabel").grid(row=0, column=1, sticky="e")

        self.log_text = tk.Text(bottom, height=10, bg="#0c0c0c", fg="#e6e6e6", insertbackground="#e6e6e6", relief="flat", wrap="word", font=("Consolas", 10), exportselection=True)
        self.log_text.grid(row=1, column=0, sticky="nsew", padx=(0, 0), pady=(6, 6))
        self.log_text.config(state="disabled")
        self.log_text.bind("<<Paste>>", lambda e: "break")
        self.log_text.tag_configure("log_ts", foreground="#808080")
        self.log_text.tag_configure("log_msg", foreground="#e6e6e6")
        self.log_text.tag_configure("log_detail", foreground="#ff9900")
        self._log("Active.")

    def _show_section(self, title):
        if self._current_section and self._current_section in self._section_frames:
            current = self._section_frames[self._current_section]
            for item in current.get("left_widgets", []):
                widget = item.get("widget") if isinstance(item, dict) else item
                try:
                    widget.grid_remove()
                except Exception:
                    pass
            if "right" in current:
                try:
                    current["right"].grid_remove()
                except Exception:
                    pass
            self._save_current_section_settings()
        else:
            for section in self._section_frames.values():
                for item in section.get("left_widgets", []):
                    widget = item.get("widget") if isinstance(item, dict) else item
                    try:
                        widget.grid_remove()
                    except Exception:
                        pass
                if "right" in section:
                    try:
                        section["right"].grid_remove()
                    except Exception:
                        pass

        section = self._section_frames.get(title)
        if not section:
            return

        self._current_section = title
        self._update_sidebar_active_state(title)
        for item in section.get("left_widgets", []):
            if isinstance(item, dict):
                widget = item["widget"]
                options = item.get("options", {})
                widget.grid(**options)
            else:
                widget = item
                widget.grid()
        section["right"].grid(row=0, column=0, sticky="nsew")
        self.active_section_var.set(f"In {title}")

        if title == "Guides":
            self._main_topbar.grid_remove()
            self._main_topbar_sep.grid_remove()
            self.left_container.grid_remove()
            self._main_sep.grid_remove()
            self.right_container.grid(row=0, column=0, columnspan=3, sticky="nsew")
        else:
            self._main_topbar.grid(row=0, column=0, sticky="nsew")
            self._main_topbar_sep.grid(row=1, column=0, sticky="ew")
            self.left_container.grid(row=0, column=0, sticky="nsew")
            self._main_sep.grid(row=0, column=1, sticky="ns")
            self.right_container.grid(row=0, column=2, sticky="nsew")

        self.left_container.columnconfigure(0, weight=1)
        self.right_container.rowconfigure(0, weight=1)
        self.right_container.columnconfigure(0, weight=1)

        self._restore_section_path(title)
        self._restore_section_settings(title)
        self._save_config()

    def _save_current_section_settings(self):
        if not self._current_section:
            return
        current_path = self.mod_path.get()
        placeholder = self._path_placeholders.get(self._current_section, "")
        all_placeholders = set(self._path_placeholders.values())
        if current_path and current_path not in all_placeholders:
            self._mod_paths[self._current_section] = current_path
        section_cfg = self._config["mod_paths"].setdefault(self._current_section, {})
        if self._current_section == "Hash Character Mods Updater":
            section_cfg["frame_hash_updater_path"] = current_path
            section_cfg["ini_backup_folder"] = self.ini_backup_folder.get()
            section_cfg["ini_checkbox_status"] = bool(self.ini_checkbox_status.get())
            section_cfg["buf_backup_folder"] = self.buf_backup_folder.get()
            section_cfg["buf_checkbox_status"] = bool(self.buf_checkbox_status.get())
        elif self._current_section == "Jane Doe Remapper":
            section_cfg["frame_janedoe_remapper_path"] = current_path
            section_cfg["buf_backup_folder"] = self.jane_remapper_buf_backup_folder.get()
            section_cfg["buf_checkbox_status"] = bool(self.jane_remapper_buf_checkbox_status.get())
        elif self._current_section == "Dialyn Remapper":
            section_cfg["frame_dialyn_remapper_path"] = current_path
            section_cfg["buf_backup_folder"] = self.dialyn_remapper_buf_backup_folder.get()
            section_cfg["buf_checkbox_status"] = bool(self.dialyn_remapper_buf_checkbox_status.get())

    def _restore_section_settings(self, section):
        section_cfg = self._config["mod_paths"].get(section, {})
        if section == "Hash Character Mods Updater":
            self.ini_backup_folder.set(section_cfg.get("ini_backup_folder", ""))
            self.ini_checkbox_status.set(bool(section_cfg.get("ini_checkbox_status", False)))
            self.buf_backup_folder.set(section_cfg.get("buf_backup_folder", ""))
            self.buf_checkbox_status.set(bool(section_cfg.get("buf_checkbox_status", False)))
        elif section == "Jane Doe Remapper":
            self.jane_remapper_buf_backup_folder.set(section_cfg.get("buf_backup_folder", ""))
            self.jane_remapper_buf_checkbox_status.set(bool(section_cfg.get("buf_checkbox_status", False)))
        elif section == "Dialyn Remapper":
            self.dialyn_remapper_buf_backup_folder.set(section_cfg.get("buf_backup_folder", ""))
            self.dialyn_remapper_buf_checkbox_status.set(bool(section_cfg.get("buf_checkbox_status", False)))

    def _restore_section_path(self, section):
        placeholder = self._path_placeholders.get(section, "")
        saved_path = self._mod_paths.get(section, "")
        if saved_path and saved_path not in self._path_placeholders.values():
            self.mod_path.set(saved_path)
            self._path_entry.configure(foreground="#ffffff")
        else:
            self.mod_path.set(placeholder)
            self._path_entry.configure(foreground="#aaaaaa")

    def _on_checkbox_clicked(self, text, var, ui_handler=None):
        self._log(f"Checkbox clicked: {text} = {var.get()}")
        if ui_handler:
            ui_handler()
        self._on_setting_changed()

    def _on_hash_ini_toggle(self):
        section = self._section_frames.get("Hash Character Mods Updater")
        entry = section.get("ini_entry") if isinstance(section, dict) else None
        icons = section.get("ini_icons") if isinstance(section, dict) else None
        if entry:
            enabled = bool(self.ini_checkbox_status.get())
            entry.configure(
                state="readonly",
                bg="#252526" if enabled else "#1e1e1e",
                readonlybackground="#252526" if enabled else "#1e1e1e",
                fg="#f0f0f0" if enabled else "#aaaaaa",
            )
        if icons:
            enabled = bool(self.ini_checkbox_status.get())
            icons["frame"].configure(bg="#252526" if enabled else "#1e1e1e")
            self._set_icon_state(icons["folder"], enabled)
            self._set_icon_state(icons["refresh"], enabled)

    def _on_hash_buf_toggle(self):
        section = self._section_frames.get("Hash Character Mods Updater")
        entry = section.get("buf_entry") if isinstance(section, dict) else None
        icons = section.get("buf_icons") if isinstance(section, dict) else None
        if entry:
            enabled = bool(self.buf_checkbox_status.get())
            entry.configure(
                state="readonly",
                bg="#252526" if enabled else "#1e1e1e",
                readonlybackground="#252526" if enabled else "#1e1e1e",
                fg="#f0f0f0" if enabled else "#aaaaaa",
            )
        if icons:
            enabled = bool(self.buf_checkbox_status.get())
            icons["frame"].configure(bg="#252526" if enabled else "#1e1e1e")
            self._set_icon_state(icons["folder"], enabled)
            self._set_icon_state(icons["refresh"], enabled)

    def _on_jane_remapper_buf_toggle(self):
        section = self._section_frames.get("Jane Doe Remapper")
        entry = section.get("buf_entry") if isinstance(section, dict) else None
        icons = section.get("buf_icons") if isinstance(section, dict) else None
        if entry:
            enabled = bool(self.jane_remapper_buf_checkbox_status.get())
            entry.configure(
                state="readonly",
                bg="#252526" if enabled else "#1e1e1e",
                readonlybackground="#252526" if enabled else "#1e1e1e",
                fg="#f0f0f0" if enabled else "#aaaaaa",
            )
        if icons:
            enabled = bool(self.jane_remapper_buf_checkbox_status.get())
            icons["frame"].configure(bg="#252526" if enabled else "#1e1e1e")
            self._set_icon_state(icons["folder"], enabled)
            self._set_icon_state(icons["refresh"], enabled)

    def _on_dialyn_remapper_buf_toggle(self):
        section = self._section_frames.get("Dialyn Remapper")
        entry = section.get("buf_entry") if isinstance(section, dict) else None
        icons = section.get("buf_icons") if isinstance(section, dict) else None
        if entry:
            enabled = bool(self.dialyn_remapper_buf_checkbox_status.get())
            entry.configure(
                state="readonly",
                bg="#252526" if enabled else "#1e1e1e",
                readonlybackground="#252526" if enabled else "#1e1e1e",
                fg="#f0f0f0" if enabled else "#aaaaaa",
            )
        if icons:
            enabled = bool(self.dialyn_remapper_buf_checkbox_status.get())
            icons["frame"].configure(bg="#252526" if enabled else "#1e1e1e")
            self._set_icon_state(icons["folder"], enabled)
            self._set_icon_state(icons["refresh"], enabled)

    def _create_folder_icon_canvas(self, parent, command, tooltip=None):
        canvas = tk.Canvas(parent, width=14, height=14, bg="#252526", highlightthickness=0, relief="flat")
        canvas._icon_type = "folder"
        canvas._icon_command = command
        canvas.configure(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: command())
        self._set_icon_png(canvas, _FOLDER_ICON_PATH, enabled=True)
        if tooltip:
            _ToolTip(canvas, tooltip)
        return canvas

    def _create_refresh_icon_canvas(self, parent, command, tooltip=None):
        canvas = tk.Canvas(parent, width=14, height=14, bg="#252526", highlightthickness=0, relief="flat")
        canvas._icon_type = "refresh"
        canvas._icon_command = command
        canvas.configure(cursor="hand2")
        canvas.bind("<Button-1>", lambda e: command())
        self._set_icon_png(canvas, _REFRESH_ICON_PATH, enabled=True)
        if tooltip:
            _ToolTip(canvas, tooltip)
        return canvas

    def _add_checkbox_hover(self, checkbox):
        normal_bg = "#252526"
        hover_bg = "#2d2d30"
        checkbox.bind("<Enter>", lambda e: checkbox.configure(bg=hover_bg))
        checkbox.bind("<Leave>", lambda e: checkbox.configure(bg=normal_bg))

    def _set_icon_png(self, canvas, png_path, enabled):
        canvas.delete("all")
        if Image is not None and ImageTk is not None:
            try:
                img = Image.open(png_path)
                if img.mode != "RGBA":
                    img = img.convert("RGBA")
                alpha = img.split()[-1]
                fg = (240, 240, 240, 255) if enabled else (120, 120, 120, 255)
                colored = Image.new("RGBA", img.size, fg)
                colored.putalpha(alpha)
                photo = ImageTk.PhotoImage(colored)
                canvas.create_image(7, 7, image=photo)
                canvas._photo = photo
                return
            except Exception:
                pass
        try:
            photo = tk.PhotoImage(file=str(png_path))
            canvas.create_image(7, 7, image=photo)
            canvas._photo = photo
        except Exception:
            pass

    def _set_icon_state(self, canvas, enabled):
        bg = "#252526" if enabled else "#1e1e1e"
        canvas.configure(bg=bg, cursor="hand2" if enabled else "")
        icon_type = getattr(canvas, "_icon_type", "")
        if icon_type == "folder":
            self._set_icon_png(canvas, _FOLDER_ICON_PATH, enabled)
        elif icon_type == "refresh":
            self._set_icon_png(canvas, _REFRESH_ICON_PATH, enabled)

    def _draw_hash_icon(self, canvas, color="#F68B2F"):
        canvas.delete("all")
        bar_width = 3
        gap = 5
        canvas.create_rectangle(3, 5, 17, 8, fill=color, outline=color)
        canvas.create_rectangle(3, 12, 17, 15, fill=color, outline=color)
        canvas.create_rectangle(5, 3, 8, 17, fill=color, outline=color)
        canvas.create_rectangle(12, 3, 15, 17, fill=color, outline=color)

    def _draw_diamond_icon(self, canvas, color="#F68B2F"):
        canvas.delete("all")
        w, h = 20, 20
        cx, cy = w // 2, h // 2
        size = 6
        canvas.create_polygon(
            cx, cy - size,
            cx + size, cy,
            cx, cy + size,
            cx - size, cy,
            fill=color, outline=color
        )

    def _draw_active_gradient(self, canvas, width=60):
        canvas.delete("all")
        canvas.configure(width=width, bg=self._sidebar_bg)
        bg = self._sidebar_bg
        r_bg, g_bg, b_bg = int(bg[1:3], 16), int(bg[3:5], 16), int(bg[5:7], 16)
        img = Image.new("RGBA", (width, 20), (0, 0, 0, 0))
        px = img.load()
        for x in range(width):
            fade = 1.0 - (x / width)
            alpha = int(55 * fade)
            r = int(r_bg + (200 - r_bg) * fade)
            g = int(g_bg + (120 - g_bg) * fade)
            b = int(b_bg + (40 - b_bg) * fade)
            for y in range(20):
                px[x, y] = (r, g, b, alpha)
        gradient = ImageTk.PhotoImage(img)
        canvas._gradient_img = gradient
        canvas.create_image(0, 0, anchor="nw", image=gradient)

    def _browse_backup_folder(self, kind):
        if kind == "ini" and not self.ini_checkbox_status.get():
            return
        if kind == "buf" and not self.buf_checkbox_status.get():
            return
        if kind == "jane_remapper_buf" and not self.jane_remapper_buf_checkbox_status.get():
            return
        if kind == "dialyn_remapper_buf" and not self.dialyn_remapper_buf_checkbox_status.get():
            return
        if kind == "ini":
            initialdir = self.ini_backup_folder.get()
        elif kind == "buf":
            initialdir = self.buf_backup_folder.get()
        elif kind == "jane_remapper_buf":
            initialdir = self.jane_remapper_buf_backup_folder.get()
        elif kind == "dialyn_remapper_buf":
            initialdir = self.dialyn_remapper_buf_backup_folder.get()
        else:
            initialdir = ""
        selected = filedialog.askdirectory(initialdir=initialdir or ".")
        if selected:
            if kind == "ini":
                self.ini_backup_folder.set(selected)
                self._log(f"Selected INI backup folder: {selected}")
            elif kind == "buf":
                self.buf_backup_folder.set(selected)
                self._log(f"Selected BUF backup folder: {selected}")
            elif kind == "jane_remapper_buf":
                self.jane_remapper_buf_backup_folder.set(selected)
                self._log(f"Selected BUF backup folder: {selected}")
            elif kind == "dialyn_remapper_buf":
                self.dialyn_remapper_buf_backup_folder.set(selected)
                self._log(f"Selected BUF backup folder: {selected}")
            self._save_current_section_settings()
            self._save_config()

    def _refresh_backup_folder(self, kind):
        if kind == "ini" and not self.ini_checkbox_status.get():
            return
        if kind == "buf" and not self.buf_checkbox_status.get():
            return
        if kind == "jane_remapper_buf" and not self.jane_remapper_buf_checkbox_status.get():
            return
        if kind == "dialyn_remapper_buf" and not self.dialyn_remapper_buf_checkbox_status.get():
            return
        if kind == "ini":
            current = self.ini_backup_folder.get()
        elif kind == "buf":
            current = self.buf_backup_folder.get()
        elif kind == "jane_remapper_buf":
            current = self.jane_remapper_buf_backup_folder.get()
        elif kind == "dialyn_remapper_buf":
            current = self.dialyn_remapper_buf_backup_folder.get()
        else:
            current = ""
        if not current:
            self._log(f"Refresh {kind.upper()} backup folder: (empty)")
            return
        self._log(f"Refreshing {kind} backup folder scan...")
        threading.Thread(target=self._refresh_backup_worker, args=(kind,), daemon=True).start()

    def _refresh_backup_worker(self, kind):
        try:
            if kind == "ini":
                folder = Path(self.ini_backup_folder.get())
            elif kind == "buf":
                folder = Path(self.buf_backup_folder.get())
            elif kind == "jane_remapper_buf":
                folder = Path(self.jane_remapper_buf_backup_folder.get())
            elif kind == "dialyn_remapper_buf":
                folder = Path(self.dialyn_remapper_buf_backup_folder.get())
            else:
                return
            if not folder.exists():
                self._log(f"Refresh {kind} backup folder: Folder not found.")
                return
            items = sorted(p.name for p in folder.iterdir())[:20]
            summary = "\n".join(items) if items else "(empty)"
            self._log(f"Scanned {kind} backup folder: {folder}\n{summary}")
        except Exception as exc:
            self._log(f"Refresh {kind} backup folder failed: {exc}")

    def _on_sidebar_click(self, title):
        if getattr(self, "_is_busy", False):
            return
        self._log(f"Sidebar clicked: {title}")
        self._show_section(title)

    def _on_path_focus_in(self, event):
        if self.focus_get() == self._path_entry:
            self._path_entry.configure(foreground="#ffffff")

    def _on_path_focus_out(self, event):
        self.after_idle(self._apply_path_placeholder)

    def _on_window_click(self, event):
        try:
            widget_under_cursor = self.winfo_containing(event.x_root, event.y_root)
        except Exception:
            return

        target_path_entry = getattr(self, "_path_entry", None)
        ini_entry = self._section_frames.get("Hash Character Mods Updater", {}).get("ini_entry") if isinstance(self._section_frames.get("Hash Character Mods Updater"), dict) else None
        buf_entry = self._section_frames.get("Hash Character Mods Updater", {}).get("buf_entry") if isinstance(self._section_frames.get("Hash Character Mods Updater"), dict) else None
        jane_remapper_buf_entry = self._section_frames.get("Jane Doe Remapper", {}).get("buf_entry") if isinstance(self._section_frames.get("Jane Doe Remapper"), dict) else None
        dialyn_remapper_buf_entry = self._section_frames.get("Dialyn Remapper", {}).get("buf_entry") if isinstance(self._section_frames.get("Dialyn Remapper"), dict) else None
        log_text = getattr(self, "log_text", None)
        cli_output = self._section_frames.get(self._current_section, {}).get("hash_cli_output") if isinstance(self._section_frames.get(self._current_section), dict) else None

        focused = self.focus_get()

        if target_path_entry and focused == target_path_entry and widget_under_cursor not in (target_path_entry, None):
            self.focus_set()

        if ini_entry and focused == ini_entry and widget_under_cursor not in (ini_entry, None):
            ini_entry.selection_clear()
            self.focus_set()

        if buf_entry and focused == buf_entry and widget_under_cursor not in (buf_entry, None):
            buf_entry.selection_clear()
            self.focus_set()

        if jane_remapper_buf_entry and focused == jane_remapper_buf_entry and widget_under_cursor not in (jane_remapper_buf_entry, None):
            jane_remapper_buf_entry.selection_clear()
            self.focus_set()

        if dialyn_remapper_buf_entry and focused == dialyn_remapper_buf_entry and widget_under_cursor not in (dialyn_remapper_buf_entry, None):
            dialyn_remapper_buf_entry.selection_clear()
            self.focus_set()

        for text_widget in (log_text, cli_output):
            if text_widget is None:
                continue
            if focused == text_widget and widget_under_cursor not in (text_widget, None):
                try:
                    text_widget.config(state="normal")
                    text_widget.tag_remove("sel", "1.0", "end")
                    text_widget.config(state="disabled")
                except Exception:
                    pass
                self.focus_set()

    def _browse_folder(self):
        selected = filedialog.askdirectory(initialdir=self.mod_path.get() or ".")
        if selected:
            self.mod_path.set(selected)
            self._save_current_section_settings()
            self._log(f"Selected folder: {selected}")
            self._save_config()
            if self._path_entry:
                self._path_entry.configure(foreground="#ffffff")

    def _on_mod_path_changed(self, *args):
        self._save_current_section_settings()
        self._save_config()
        if self._path_entry and self.mod_path.get():
            self._path_entry.configure(foreground="#ffffff")

    def _on_setting_changed(self, *args):
        self._save_current_section_settings()
        self._save_config()

    def _update_current_mod_path(self, path):
        section = self._current_section or self._config.get("active_section", "Hash Character Mods Updater")
        placeholder = self._path_placeholders.get(section, "")
        all_placeholders = set(self._path_placeholders.values())
        if path and path not in all_placeholders:
            self._mod_paths[section] = path

    def _apply_path_placeholder(self):
        if not self._path_entry:
            return
        section = self._current_section or self._config.get("active_section", "Hash Character Mods Updater")
        placeholder = self._path_placeholders.get(section, "")
        current = self.mod_path.get()
        all_placeholders = set(self._path_placeholders.values())
        if not current or current in all_placeholders:
            self.mod_path.set(placeholder)
            self._path_entry.configure(foreground="#aaaaaa")

    def _refresh_folder(self):
        self._log("Refreshing folder scan...")
        threading.Thread(target=self._refresh_worker, daemon=True).start()

    def _refresh_worker(self):
        try:
            folder = Path(self.mod_path.get())
            if not folder.exists():
                self._log("Folder not found.")
                return
            items = sorted(p.name for p in folder.iterdir())[:20]
            summary = "\n".join(items) if items else "(empty)"
            self._log(f"Scanned: {folder}\n{summary}")
        except Exception as exc:
            self._log(f"Refresh failed: {exc}")

    def _run_update_hashes(self):
        self._set_busy(True)
        self._log("Update hashes started...")
        threading.Thread(target=self._update_hashes_worker, daemon=True).start()

    def _run_jane_remapper(self):
        self._set_busy(True)
        self._log("Jane Doe Remap started...")
        threading.Thread(target=self._jane_remapper_worker, daemon=True).start()

    def _jane_remapper_worker(self):
        try:
            self.after(0, lambda: self._clear_cli_output())
            folder = Path(self.mod_path.get())
            self._log(f"Input: {folder}")

            if not folder.exists():
                self._log("Folder not found.")
                self.after(0, lambda: self._set_busy(False))
                return

            if self.jane_remapper_buf_checkbox_status.get() and not self.jane_remapper_buf_backup_folder.get():
                self._log("Please Select the Path for BUF Backup Folder.")
                self.after(0, lambda: self._set_busy(False))
                return

            script_path = _BASE_DIR / "Jane.remapper.py"
            if not script_path.exists():
                self._log(f"Remapper script not found: {script_path}")
                self.after(0, lambda: self._set_busy(False))
                return

            spec = importlib.util.spec_from_file_location("jane_remapper", str(script_path))
            module = importlib.util.module_from_spec(spec)

            original_stdout = sys.stdout
            sys.stdout = _GuiStdout(self)
            try:
                spec.loader.exec_module(module)
            except Exception:
                sys.stdout = original_stdout
                raise

            original_remap_binary = module.remap_binary

            def patched_remap_binary(target_hash, file_path, timestamp):
                try:
                    byte_data = file_path.read_bytes()
                except Exception as e:
                    print(f"Failed to read file {file_path.name}: {e}")
                    return

                num_vertices = len(byte_data) // module.STRIDE
                if num_vertices == 0:
                    return

                output_bytes = bytearray(len(byte_data))

                if target_hash == 'e42171df':
                    mapping = module.HAIR_MAPPINGS
                elif target_hash == 'd06a9206':
                    mapping = module.HAND_MAPPINGS
                elif target_hash == 'hair':
                    mapping = module.HAIR_MAPPINGS
                elif target_hash == 'hand':
                    mapping = module.HAND_MAPPINGS
                else:
                    print(f"  Skipping {file_path.name}: unknown blend category '{target_hash}'")
                    return

                for x in range(num_vertices):
                    group = x * module.STRIDE
                    weights = byte_data[group : group + 16]
                    indices = struct.unpack('<4I', byte_data[group + 16 : group + 32])
                    mapped_indices = [mapping.get(idx, idx) for idx in indices]
                    mapped_bytes = struct.pack('<4I', *mapped_indices)
                    output_bytes[group : group + 16] = weights
                    output_bytes[group + 16 : group + 32] = mapped_bytes

                backup_name = f"remap_backup_{timestamp}-{file_path.name}"
                do_backup = self.jane_remapper_buf_checkbox_status.get() and self.jane_remapper_buf_backup_folder.get()
                if do_backup:
                    backup_path = Path(self.jane_remapper_buf_backup_folder.get()) / '(.buf) JaneDoe Backup' / backup_name
                    try:
                        os.makedirs(str(backup_path.parent), exist_ok=True)
                    except Exception as e:
                        print(f"⚠  Failed to create JaneDoe backup folder at '{backup_path.parent}': {e}")
                        backup_path = None
                else:
                    backup_path = None

                if backup_path is not None:
                    try:
                        shutil.copy2(file_path, backup_path)
                        print(f"-> Remapped: {file_path.name} (Backed up to: {backup_path})")
                    except Exception as e:
                        print(f"Warning: Failed to create backup of {file_path.name}: {e}")
                else:
                    print(f"-> Remapped: {file_path.name}")

                try:
                    file_path.write_bytes(output_bytes)
                except Exception as e:
                    print(f"✖ Error: Failed to write remapped file {file_path.name}: {e}")

            module.remap_binary = patched_remap_binary
            module.input = lambda prompt="": None

            original_cwd = os.getcwd()
            os.chdir(str(folder))
            try:
                module.main()
            finally:
                os.chdir(original_cwd)

            sys.stdout = original_stdout
            self.after(0, lambda: self._set_busy(False))
            self.after(0, lambda: self._log("Jane Doe Remap finished."))
        except Exception as exc:
            import traceback
            sys.stdout = original_stdout
            self.after(0, lambda: self._set_busy(False))
            self.after(0, lambda: self._log(f"Jane Doe Remap failed: {exc}"))
            self.after(0, lambda: self._log(traceback.format_exc()))

    def _run_dialyn_remapper(self):
        self._set_busy(True)
        self._log("Dialyn Remap started...")
        threading.Thread(target=self._dialyn_remapper_worker, daemon=True).start()

    def _dialyn_remapper_worker(self):
        try:
            self.after(0, lambda: self._clear_cli_output())
            folder = Path(self.mod_path.get())
            self._log(f"Input: {folder}")

            if not folder.exists():
                self._log("Folder not found.")
                self.after(0, lambda: self._set_busy(False))
                return

            if self.dialyn_remapper_buf_checkbox_status.get() and not self.dialyn_remapper_buf_backup_folder.get():
                self._log("Please Select the Path for BUF Backup Folder.")
                self.after(0, lambda: self._set_busy(False))
                return

            script_path = _BASE_DIR / "Dialyn.remapper.py"
            if not script_path.exists():
                self._log(f"Remapper script not found: {script_path}")
                self.after(0, lambda: self._set_busy(False))
                return

            spec = importlib.util.spec_from_file_location("dialyn_remapper", str(script_path))
            module = importlib.util.module_from_spec(spec)

            original_stdout = sys.stdout
            sys.stdout = _GuiStdout(self)
            try:
                spec.loader.exec_module(module)
            except Exception:
                sys.stdout = original_stdout
                raise

            original_remap_binary = module.remap_binary

            def patched_remap_binary(target_hash, file_path, timestamp):
                try:
                    byte_data = file_path.read_bytes()
                except Exception as e:
                    print(f"Failed to read file {file_path.name}: {e}")
                    return

                num_vertices = len(byte_data) // module.STRIDE
                if num_vertices == 0:
                    return

                output_bytes = bytearray(len(byte_data))
                mapping = module.BLEND_MAPPING

                for v in range(num_vertices):
                    offset = v * module.STRIDE
                    output_bytes[offset:offset+16] = byte_data[offset:offset+16]
                    indices = struct.unpack_from('<4I', byte_data, offset + 16)
                    mapped_indices = [mapping.get(idx, idx) for idx in indices]
                    output_bytes[offset + 16:offset + 32] = struct.pack('<4I', *mapped_indices)

                backup_name = f"remap_backup_{timestamp}-{file_path.name}"
                do_backup = self.dialyn_remapper_buf_checkbox_status.get() and self.dialyn_remapper_buf_backup_folder.get()
                if do_backup:
                    backup_path = Path(self.dialyn_remapper_buf_backup_folder.get()) / '(.buf) Dialyn Backup' / backup_name
                    try:
                        os.makedirs(str(backup_path.parent), exist_ok=True)
                    except Exception as e:
                        print(f"⚠  Failed to create Dialyn backup folder at '{backup_path.parent}': {e}")
                        backup_path = None
                else:
                    backup_path = None

                if backup_path is not None:
                    try:
                        shutil.copy2(file_path, backup_path)
                        print(f"-> Remapped: {file_path.name} (Backed up to: {backup_path})")
                    except Exception as e:
                        print(f"Warning: Failed to create backup of {file_path.name}: {e}")
                else:
                    print(f"-> Remapped: {file_path.name}")

                try:
                    file_path.write_bytes(output_bytes)
                except Exception as e:
                    print(f"✖ Error: Failed to write remapped file {file_path.name}: {e}")

            module.remap_binary = patched_remap_binary
            module.input = lambda prompt="": None

            original_cwd = os.getcwd()
            os.chdir(str(folder))
            try:
                module.main()
            finally:
                os.chdir(original_cwd)

            sys.stdout = original_stdout
            self.after(0, lambda: self._set_busy(False))
            self.after(0, lambda: self._log("Dialyn Remap finished."))
        except Exception as exc:
            import traceback
            sys.stdout = original_stdout
            self.after(0, lambda: self._set_busy(False))
            self.after(0, lambda: self._log(f"Dialyn Remap failed: {exc}"))
            self.after(0, lambda: self._log(traceback.format_exc()))

    def _update_hashes_worker(self):
        try:
            self.after(0, lambda: self._clear_cli_output())
            folder = Path(self.mod_path.get())
            self._log(f"Input: {folder}")

            if not folder.exists():
                self._log("Folder not found.")
                self.after(0, lambda: self._set_busy(False))
                return

            script_path = _BASE_DIR / "zzz-mod-fixer.py"
            if not script_path.exists():
                self._log(f"CLI script not found: {script_path}")
                self.after(0, lambda: self._set_busy(False))
                return

            errors = []
            if self.ini_checkbox_status.get() and not self.ini_backup_folder.get():
                errors.append("Please Select the Path for INI Backup Folder.")
            if self.buf_checkbox_status.get() and not self.buf_backup_folder.get():
                errors.append("Please Select the Path for BUF Backup Folder.")

            if errors:
                for error in errors:
                    self._log(error)
                self.after(0, lambda: self._set_busy(False))
                return

            spec = importlib.util.spec_from_file_location("zzz_mod_fixer", str(script_path))
            module = importlib.util.module_from_spec(spec)

            original_stdout = sys.stdout
            sys.stdout = _GuiStdout(self)
            try:
                spec.loader.exec_module(module)
            except Exception:
                sys.stdout = original_stdout
                raise

            gui = self

            original_save = module.Ini.save

            def patched_save(self):
                if self._touched:
                    basename = os.path.basename(self.filepath).split('.ini')[0]
                    do_ini_backup = gui.ini_checkbox_status.get() and gui.ini_backup_folder.get()
                    do_buf_backup = gui.buf_checkbox_status.get() and gui.buf_backup_folder.get()

                    if do_ini_backup:
                        backup_dir = Path(gui.ini_backup_folder.get()) / '(.ini) Caches'
                        try:
                            os.makedirs(str(backup_dir), exist_ok=True)
                        except Exception as e:
                            print(f"⚠  Failed to create INI backup folder at '{backup_dir}': {e}")
                            backup_dir = None
                    else:
                        backup_dir = None

                    if backup_dir:
                        backup_dir = str(backup_dir.absolute())
                        backup_filename = f'DISABLED_BACKUP_{int(time.time())}_{basename}.txt'
                        backup_fullpath = os.path.join(backup_dir, backup_filename)

                        try:
                            import shutil
                            shutil.move(self.filepath, backup_fullpath)
                            print(f'Created Backup: {backup_filename} at {backup_dir}')
                        except Exception as e:
                            print(f"⚠  Failed to relocate backup externally (Different Drive/Access): {e}")
                            try:
                                backup_fallback_filename = f'DISABLED_BACKUP_{int(time.time())}.{basename}.txt'
                                backup_fallback_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
                                backup_fallback_path = os.path.join(backup_fallback_dir, backup_fallback_filename)
                                with open(self.filepath, 'r', encoding=self.encoding) as original_file:
                                    original_content = original_file.read()
                                with open(backup_fallback_path, 'w', encoding=self.encoding) as backup_file:
                                    backup_file.write(original_content)
                                print(f'Created Backup (Emergency): {backup_fallback_filename} at {backup_fallback_dir}')
                            except Exception as ex:
                                print(f"✖ Failed to create emergency backup: {ex}")

                    with open(self.filepath, 'w', encoding=self.encoding) as updated_ini:
                        updated_ini.write(self.content)

                    if len(self.modified_buffers) > 0:
                        print('Writing updated buffers')
                        if do_buf_backup:
                            buf_backup_dir = Path(gui.buf_backup_folder.get()) / '(.buf) Backup'
                            try:
                                os.makedirs(str(buf_backup_dir), exist_ok=True)
                            except Exception as e:
                                print(f"⚠  Failed to create BUF backup folder at '{buf_backup_dir}': {e}")
                                buf_backup_dir = None
                        else:
                            buf_backup_dir = None

                        for filepath, data in self.modified_buffers.items():
                            original_path = Path(filepath)
                            if original_path.exists():
                                if buf_backup_dir:
                                    try:
                                        relative = original_path.relative_to(Path(self.filepath).parent)
                                        backup_file = Path(str(buf_backup_dir)) / relative
                                    except ValueError:
                                        backup_file = Path(str(buf_backup_dir)) / original_path.name
                                    try:
                                        os.makedirs(str(backup_file.parent), exist_ok=True)
                                        import shutil
                                        shutil.copy2(str(original_path), str(backup_file))
                                        print(f'\tBacked up: {original_path.name} -> {backup_file}')
                                    except Exception as be:
                                        print(f"\t⚠  Failed to backup {original_path.name}: {be}")
                            with open(filepath, 'wb') as f:
                                f.write(data)
                            print('\tSaved: {}'.format(filepath))
                    print('Updates applied')
                else:
                    print('No changes applied')
                print()

            module.Ini.save = patched_save

            if not folder.exists():
                self._log("Folder not found.")
                self.after(0, lambda: self._set_busy(False))
                return

            self.after(0, lambda: self._log("Running..."))
            try:
                ini_files = [f for f in folder.rglob('*.ini') if not f.name.upper().startswith('DISABLED') and not f.name.upper().startswith('DESKTOP')]
                if not ini_files:
                    print("No .ini files found in current directory and subdirectories.")
                else:
                    module.process_folder(str(folder))
            finally:
                sys.stdout = original_stdout

            self.after(0, lambda: self._set_busy(False))
            self.after(0, lambda: self._log("Update Hashes finished."))
        except Exception as exc:
            import traceback
            sys.stdout = original_stdout
            self.after(0, lambda: self._set_busy(False))
            self.after(0, lambda: self._log(f"Update Hashes failed: {exc}"))
            self.after(0, lambda: self._log(traceback.format_exc()))


    def _set_busy(self, busy: bool):
        self._is_busy = busy
        state = "disabled" if busy else "normal"
        for btn in getattr(self, "_action_buttons", []):
            try:
                btn.configure(state=state)
            except Exception:
                pass
        self.status_var.set("Running..." if busy else "Active")

    def _clear_cli_output(self):
        section = self._section_frames.get(self._current_section)
        target = section.get("hash_cli_output") if section else None
        if target is not None:
            target.config(state="normal")
            target.delete("1.0", "end")
            target.config(state="disabled")
        self._update_cli_scrollbar()

    def _clear_cli_action(self):
        section = self._section_frames.get(self._current_section)
        target = section.get("hash_cli_output") if section else None
        if target is None:
            self._log("No Process Found to Clean Up.")
            return

        target.config(state="normal")
        content = target.get("1.0", "end").strip()
        if not content:
            self._log("No Process Found to Clean Up.")
        else:
            target.delete("1.0", "end")
            self._log("CLI Output has been cleared.")
        target.config(state="disabled")
        self._update_cli_scrollbar()

    def _update_cli_scrollbar(self):
        section = self._section_frames.get(self._current_section)
        target = section.get("hash_cli_output") if section else None
        scrollbar = getattr(self, "_cli_scroll", None)
        if target is None or scrollbar is None:
            return
        try:
            has_content = bool(target.get("1.0", "end").strip())
            if has_content:
                scrollbar.grid()
            else:
                scrollbar.grid_remove()
        except Exception:
            pass

    def _append_cli_output(self, text: str):
        section = self._section_frames.get(self._current_section)
        target = section.get("hash_cli_output") if section else None
        if target is None:
            return

        def append():
            target.config(state="normal")
            target.insert("end", text)
            target.see("end")
            target.config(state="disabled")
            self._update_cli_scrollbar()

        if threading.current_thread() is threading.main_thread():
            append()
        else:
            self.after(0, append)

    def _log(self, message: str):
        timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
        def append():
            self.log_text.config(state="normal")
            self.log_text.insert("end", f"{timestamp} ", "log_ts")
            if ":" in message:
                before, after = message.split(":", 1)
                self.log_text.insert("end", f"{before}:", "log_msg")
                self.log_text.insert("end", f"{after}\n", "log_detail")
            else:
                self.log_text.insert("end", f"{message}\n", "log_msg")
            self.log_text.see("end")
            self.log_text.config(state="disabled")
        if threading.current_thread() is threading.main_thread():
            append()
        else:
            self.after(0, append)


def main():
    app = ZZZModFixerGUI()
    app.mainloop()


if __name__ == "__main__":
    main()