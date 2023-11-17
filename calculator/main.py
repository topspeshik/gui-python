import tkinter as tk
from ViewModel import ViewModel

def validateNumbers(P):
        if P == '':
            return True
        elif P in ['/', '*', '-', '+','1/x','x²','√','⌫','CE', 'C','±','.','%']:
            return True
        elif P.isdigit():
            return True
        else:
            try:
                float(P)
                return  True
            except:
                return False


window = tk.Tk()
window.title("Calculator")
window.geometry('360x510')

reg = window.register(validateNumbers)

startValue = tk.StringVar(value='0')
input_entry = tk.Entry(window, bg="#ebecef", bd=0, textvariable=startValue, font=('Segoe UI', 32, 'bold'), justify='right')
input_entry.config(validate="key", validatecommand =(reg, '%P'))
input_entry.grid(column=0, row=1, columnspan=4, sticky='wens', padx =8)

history_lbl = tk.Label(window, bg="#ebecef", text="", font=('Segoe UI', 12), anchor='e')
history_lbl.grid(column=0, row=0, columnspan=4, sticky='wens', padx =8)

viewModel = ViewModel(input_entry, history_lbl)

btn = [['%', '√', 'x²', '1/x'],
       ['CE', 'C', '⌫', '/'],
       ['7', '8', '9', '*'],
       ['4', '5', '6', '-'],
       ['1', '2', '3', '+'],
       ['±', '0', '.', '=']]

for i in range(2, 8):
    for j in range(4):
        btn_lbl = btn[i - 2][j]
        if btn_lbl.isdigit():
            tk.Button(window, text=btn_lbl, bd=0,bg="#fcfcfc", font=('Segoe UI Semibold', 12),
                      command=lambda l=btn_lbl: viewModel.parseButton(l)).grid(column=j,
                                                                               row=i,
                                                                               sticky='wens',
                                                                               padx=2,
                                                                               pady=2)
        else:
            tk.Button(window, text=btn_lbl, bd=0, bg="#D2ECEC", font=('Segoe UI Semibold', 12),
                      command=lambda l=btn_lbl: viewModel.parseButton(l)).grid(column=j,
                                                                               row=i,
                                                                               sticky='wens',
                                                                               padx=2,
                                                                               pady=2)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(8):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
