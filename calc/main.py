import tkinter as tk
import threading


def compute_expression(expr, result_var):
    try:
        result = eval(expr)
        result_var.set(result)
    except Exception:
        result_var.set("Ошибка")


class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор (упрощённый)")
        self.resizable(False, False)

        self.expr_var = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.expr_var, font=(None, 20), justify='right')
        entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, ch in enumerate(row):
                tk.Button(self, text=ch, width=5, height=2, font=(None, 18),
                          command=lambda ch=ch: self.press(ch)).grid(row=r, column=c, padx=5, pady=5)

        tk.Button(self, text='C', width=5, height=2, font=(None, 18),
                  command=self.clear).grid(row=5, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
        tk.Button(self, text='⌫', width=5, height=2, font=(None, 18),
                  command=self.back).grid(row=5, column=2, columnspan=2, sticky='nsew', padx=5, pady=5)

    def press(self, ch):
        if ch == '=':
            expr = self.expr_var.get()
            threading.Thread(target=compute_expression, args=(expr, self.expr_var), daemon=True).start()
        else:
            self.expr_var.set(self.expr_var.get() + ch)

    def clear(self):
        self.expr_var.set('')

    def back(self):
        self.expr_var.set(self.expr_var.get()[:-1])


if __name__ == '__main__':
    Calc().mainloop()
