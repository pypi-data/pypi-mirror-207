import tkinter as tk
import tkinter.ttk as ttk

from guimpl.row_pygubu.axewidgetsbaseframe import AxeWidgetsBaseFrameWidget


class MainAxeWidgetsFrameWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(MainAxeWidgetsFrameWidget, self).__init__(master, **kw)
        self.canvas = tk.Canvas(self)
        self.canvas.configure(height=800, width=320)
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.base_widgets_frame = AxeWidgetsBaseFrameWidget(self.scrollable_frame)

        self.axe_settings_frame = self.base_widgets_frame.axe_settings_frame
        self.choose_line_combo = self.base_widgets_frame.choose_line_combo
        self.line_settings_frame = self.base_widgets_frame.line_settings_frame
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
