#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class AxeWidgetsBaseFrameWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(AxeWidgetsBaseFrameWidget, self).__init__(master, **kw)
        self.axe_settings_frame = ttk.Labelframe(self)
        self.axe_settings_frame.configure(height=200, text="axe settings", width=300)
        self.axe_settings_frame.pack()
        self.choose_line_combo = ttk.Combobox(self)
        self.choose_line_var = tk.StringVar()
        self.choose_line_combo.configure(textvariable=self.choose_line_var)
        self.choose_line_combo.pack(side="top")
        self.line_settings_frame = ttk.Labelframe(self)
        self.line_settings_frame.configure(height=200, text="line settings", width=300)
        self.line_settings_frame.pack()
        self.configure(height=200, width=250)
        self.pack()


if __name__ == "__main__":
    root = tk.Tk()
    widget = AxeWidgetsBaseFrameWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
