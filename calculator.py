import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + button_text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right')
entry.pack(fill='both', ipadx=8, ipady=8, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18), command=lambda b=btn: on_click(b))
        button.pack(side='left', expand=True, fill='both')

root.mainloop()
