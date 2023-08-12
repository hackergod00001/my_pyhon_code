import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calculator


def calculate_conversion():
    try:
        decimal_input = float(decimal_entry.get())
        base_input = int(base_combobox.get())

        if base_input not in [2, 8, 10, 16]:
            raise ValueError(
                'Base must be either of the following values: 2, 8, 10, 16')

        if decimal_input < 0:
            raise ValueError("Please enter a non-negative decimal number.")

        base_result = calculator.decimal_to_base(decimal_input, base_input)
        base_result_label.config(text=f"Converted result: {base_result}")

        decimal_result = calculator.base_to_decimal(base_result, base_input)
        decimal_result_label.config(
            text=f"Converted back to decimal: {decimal_result}")

        show_calculation_visual(decimal_input, base_input,
                                base_result, decimal_result)

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def show_calculation_visual(decimal_input, base_input, base_result, decimal_result):
    calculation_text.config(state=tk.NORMAL)
    calculation_text.delete("1.0", tk.END)

    calculation_text.insert(
        tk.END, "Visual for Decimal to Base Conversion:\n\n")
    calculator.show_calculation_visual(
        decimal_input, base_input, base_result, True)

    calculation_text.insert(tk.END, "\n---------------------------------\n\n")

    calculation_text.insert(
        tk.END, "Visual for Base to Decimal Conversion:\n\n")
    calculator.show_calculation_visual(
        base_result, base_input, decimal_result, False)

    calculation_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Number Base Converter")

decimal_label = ttk.Label(root, text="Enter a decimal number:")
decimal_label.pack()
decimal_entry = ttk.Entry(root)
decimal_entry.pack()

base_label = ttk.Label(root, text="Select a base value:")
base_label.pack()
base_combobox = ttk.Combobox(root, values=[2, 8, 10, 16])
base_combobox.pack()

calculate_button = ttk.Button(
    root, text="Calculate", command=calculate_conversion)
calculate_button.pack()

base_result_label = ttk.Label(root, text="")
base_result_label.pack()
decimal_result_label = ttk.Label(root, text="")
decimal_result_label.pack()

calculation_text = tk.Text(root, wrap=tk.WORD, height=15, state=tk.DISABLED)
calculation_text.pack()

root.mainloop()
