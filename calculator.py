import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=1, padx=10, pady=10)

operation_var = tk.StringVar()
operation_var.set("+")

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=0, column=1, padx=10, pady=10)


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()