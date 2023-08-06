import tkinter.ttk as ttk


class DoubleSpinbox:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.spinbox1 = ttk.Spinbox(
            self.frame,
            width=(self.frame.__sizeof__() // 2) - 5,
            increment=1.0,
            from_=float("-inf"),
            to=float("inf"),
        )
        self.spinbox1.grid(row=0, column=0)
        self.spinbox2 = ttk.Spinbox(
            self.frame,
            width=(self.frame.__sizeof__() // 2) - 5,
            increment=1.0,
            from_=float("-inf"),
            to=float("inf"),
        )
        self.spinbox2.grid(row=0, column=1)
        self.double_spinbox_var = [0, 0]

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def get(self):
        self.double_spinbox_var[0] = float(self.spinbox1.get())
        self.double_spinbox_var[1] = float(self.spinbox2.get())
        return tuple(self.double_spinbox_var.copy())

    def set_value(self, value: list = [0, 0]):
        self.double_spinbox_var[0] = value[0]
        self.double_spinbox_var[1] = value[1]
        self.spinbox1.set(self.double_spinbox_var[0])
        self.spinbox2.set(self.double_spinbox_var[1])

    def get_var(self):
        return self.double_spinbox_var
