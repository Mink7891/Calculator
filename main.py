from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("320x580")
root.resizable(False, False)
root.maxsize(320, 580)

current_theme = "light"

themes = {
    "dark": {
        "bg": "#2e2e2e",
        "fg": "#ffffff",
        "button_bg": "#4e4e4e",
        "button_fg": "#ffffff",
        "label_bg": "#1e1e1e",
        "label_fg": "#ffffff",
    },
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "button_bg": "#d3d3d3",
        "button_fg": "#000000",
        "label_bg": "#f5f5f5",
        "label_fg": "#000000",
    }
}

numbers = []
operator = ""
new_number = True

def calculate(val1, val2, op):
    if op == "+":
        return val1 + val2
    elif op == "-":
        return val1 - val2
    elif op == "*":
        return val1 * val2
    elif op == "/":
        return val1 / val2
    return val2

def format_number(number_str):
    """Форматирует строку числа, удаляя лишние ведущие нули."""
    if "." in number_str:
        return str(float(number_str))
    else:
        return str(int(number_str))

def set_Text(text):
    global numbers, operator, new_number
    current_text = display.cget("text")

    if text == "C":
        numbers.clear()
        operator = ""
        new_number = True
        display.config(text="0")

    elif text in "/*-+":
        if current_text and not new_number:
            formatted_number = format_number(current_text)
            numbers.append(float(formatted_number))
            display.config(text="")

            if len(numbers) == 2:
                result = calculate(numbers[0], numbers[1], operator)
                numbers = [result]
                display.config(text=str(result))

        operator = text
        new_number = True

    elif text == "=":
        if operator and current_text and not new_number:
            formatted_number = format_number(current_text)
            numbers.append(float(formatted_number))
            result = calculate(numbers[0], numbers[1], operator)
            display.config(text=str(result))
            numbers = [result]
            operator = ""
            new_number = True

    elif text == ".":
        if "." not in current_text:
            display.config(text=current_text + text)

    else:
        if new_number:
            display.config(text=text)
            new_number = False
        else:
            display.config(text=format_number(current_text + text))

def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    theme = themes[current_theme]

    root.config(bg=theme["bg"])
    frm.config(bg=theme["bg"])

    display.config(bg=theme["label_bg"], fg=theme["label_fg"])


    for btn in buttons:
        btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    theme_button.config(bg=theme["button_bg"], fg=theme["button_fg"])

frm = Frame(root, bg=themes[current_theme]["bg"], padx=10, pady=10)
frm.grid(row=0, column=0, sticky="nsew")
display = Label(frm, font=("Arial", 24, "bold"), justify="right",
                bg=themes[current_theme]["label_bg"], fg=themes[current_theme]["label_fg"], anchor="e", text="0",
                relief="sunken", padx=10, pady=10)
display.grid(column=0, row=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")


buttons_data = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("=", 5, 3),
]

buttons = []
for (text, row, col) in buttons_data:
    btn = Button(
        frm, text=text, command=lambda t=text: set_Text(t),
        bg=themes[current_theme]["button_bg"], fg=themes[current_theme]["button_fg"],
        font=("Arial", 14), width=4, height=2, relief="raised", bd=2)
    btn.grid(row=row, column=col, sticky="nsew",
             padx=5, pady=5, ipadx=5, ipady=5)
    buttons.append(btn)

theme_button = Button(root, text="Toggle Theme", command=toggle_theme,
                      bg=themes[current_theme]["button_bg"], fg=themes[current_theme]["button_fg"],
                      font=("Arial", 14), relief="raised", bd=2)
theme_button.grid(row=6, column=0, pady=10, padx=10, sticky="nsew")


for i in range(5):
    frm.rowconfigure(i, weight=1)
    frm.columnconfigure(i, weight=1)

root.mainloop()
