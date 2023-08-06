#!/usr/bin/python3
from tkinter import ttk
import tkinter as tk


class AutowidgetsBaseFrameWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(AutowidgetsBaseFrameWidget, self).__init__(master, **kw)
        self.configure(height=200, width=300)
        self.pack(side="top")


if __name__ == "__main__":
    root = tk.Tk()
    widget = AutowidgetsBaseFrameWidget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
