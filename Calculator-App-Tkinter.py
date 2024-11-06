import tkinter as tk
import math

# Create a Window using a tkinter object
window = tk.Tk()
window.geometry("600x350")
window.title("Basic Calculator App")

# Number inputs
number1 = tk.Label(text="Enter the 1st Number:")
number1.grid(column=0, row=0, padx=10, pady=10)
number1Entry = tk.Entry(width=15)
number1Entry.grid(column=1, row=0, padx=10, pady=10)

number2 = tk.Label(text="Enter the 2nd Number (if applicable):")
number2.grid(column=0, row=1, padx=10, pady=10)
number2Entry = tk.Entry(width=15)
number2Entry.grid(column=1, row=1, padx=10, pady=10)

# Operation selection
operationLabel = tk.Label(text="Select the Operation to Perform:")
operationLabel.grid(column=0, row=2, padx=10, pady=10)

selectOption = tk.StringVar(window)
selectOption.set("Select Operation")
operationMenu = tk.OptionMenu(window, selectOption, "Add", "Subtract", "Multiply", "Divide", "Modulus", "Power",
                              "Square Root")
operationMenu.grid(column=1, row=2, padx=10, pady=10)


# Function to perform the arithmetic operation
def arithmeticOperation():
    try:
        # Check if the first number is provided
        if not number1Entry.get():
            raise ValueError("Please enter the 1st number.")
        a = float(number1Entry.get())

        # Check if the second number is required and provided
        b = None
        if selectOption.get() not in ["Square Root"]:
            if not number2Entry.get():
                raise ValueError("Please enter the 2nd number.")
            b = float(number2Entry.get())

        # Perform the selected operation and format result string
        operation = selectOption.get()
        if operation == 'Add':
            result = f"{a} + {b} = {a + b}"
        elif operation == 'Subtract':
            result = f"{a} - {b} = {a - b}"
        elif operation == 'Multiply':
            result = f"{a} * {b} = {a * b}"
        elif operation == 'Divide':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = f"{a} / {b} = {a / b}"
        elif operation == 'Modulus':
            result = f"{a} % {b} = {a % b}"
        elif operation == 'Power':
            result = f"{a} ^ {b} = {math.pow(a, b)}"
        elif operation == 'Square Root':
            if a < 0:
                raise ValueError("Cannot take the square root of a negative number.")
            result = f"√{a} = {math.sqrt(a)}"
        else:
            result = "Please select a valid operation."

    except ValueError as ve:
        result = str(ve)
    except ZeroDivisionError as zde:
        result = str(zde)

    # Display the result in the Text widget
    textArea.config(state="normal")  # Enable editing for update
    textArea.delete(1.0, tk.END)  # Clear previous content
    textArea.insert(tk.END, result)  # Insert new result
    textArea.config(state="disabled")  # Disable editing after update


# Calculate button
calculateButton = tk.Button(window, text="Calculate", command=arithmeticOperation, bg="lightgreen")
calculateButton.grid(column=0, row=3, columnspan=2, padx=10, pady=15)

# Result display
textArea = tk.Text(master=window, height=3, width=30, font=("Arial", 12), wrap="word", state="disabled")
textArea.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
