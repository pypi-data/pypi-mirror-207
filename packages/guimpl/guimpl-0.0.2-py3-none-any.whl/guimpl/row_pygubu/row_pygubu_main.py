#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class RowPygubuUiApp:
    def __init__(self, master=None):
        # build ui
        self.main_frame = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_frame.configure(height=200, width=200)
        self.main_frame.geometry("768x576")
        self.frame_widgets = ttk.Labelframe(self.main_frame)
        self.frame_widgets.configure(height=200, text="Paramètres", width=335)
        self.MainNoteBook = ttk.Notebook(self.frame_widgets)
        self.MainNoteBook.configure(height=200, width=335)
        self.MainNoteBook.grid(column=0, row=0, rowspan=11, sticky="nsew")
        self.update_button = ttk.Button(self.frame_widgets)
        self.update_button.configure(cursor="hand2", text="Appliquer")
        self.update_button.grid(column=0, row=11, sticky="sew")
        self.update_button.configure(command=self.updatePlot)
        self.frame_widgets.grid(column=1, row=0, rowspan=3, sticky="nsew")
        self.frame_widgets.grid_propagate(0)
        self.frame_widgets.grid_anchor("center")
        self.frame_widgets.rowconfigure(10, weight=1)
        self.fig_canvas = tk.Canvas(self.main_frame)
        self.fig_canvas.grid(column=0, pady=5, row=0, rowspan=3, sticky="nsew")
        self.main_frame.rowconfigure(0, weight=2)
        self.main_frame.columnconfigure(0, weight=2)

        # Main widget
        self.mainwindow = self.main_frame

    def run(self):
        self.mainwindow.mainloop()

    def updatePlot(self):
        pass


if __name__ == "__main__":
    app = RowPygubuUiApp()
    app.run()
