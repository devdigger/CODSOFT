import tkinter as tk

def click_button(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for display
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
for i in range(1, 10):
    row = (i - 1) // 3 + 1
    col = (i - 1) % 3
    button = tk.Button(root, text=str(i), padx=20, pady=20, command=lambda i=i: click_button(i))
    button.grid(row=row, column=col)

button_font = ("Helvetica", 14, "bold")
# Create other buttons
# Create other buttons
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: click_button(0))
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=clear)
button_equal = tk.Button(root, text="=", padx=20, pady=20, command=calculate)  # Adjusted padx value
button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: click_button('+'))
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: click_button('-'))
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: click_button('*'))
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: click_button('/'))

# Place the buttons on the grid
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)


# Start the Tkinter event loop
root.mainloop()
