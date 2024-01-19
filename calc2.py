import tkinter as tk

class Calculator:
    def __init__(self, master):
        master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]
        row = 1
        col = 0
        for button in buttons:
            tk.Button(
                master,
                text=button,
                width=5,
                command=lambda t=button: self.button_click(t)
            ).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except ZeroDivisionError:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error: Division by zero")
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, char)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
