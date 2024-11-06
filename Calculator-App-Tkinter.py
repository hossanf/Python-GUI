import tkinter as tk
import math

# Create a Window using a tkinter object
window = tk.Tk()
window.geometry("600x300")
window.title("Basic Calculator App")

# Number inputs
number1 = tk.Label(text="Enter the 1st Number:")
number1.grid(column=0, row=0)
number1Entry = tk.Entry()
number1Entry.grid(column=1, row=0)

number2 = tk.Label(text="Enter the 2nd Number (if applicable):")
number2.grid(column=0, row=1)
number2Entry = tk.Entry()
number2Entry.grid(column=1, row=1)

# Operation selection
operationLabel = tk.Label(text="Select the Operation to Perform:")
operationLabel.grid(column=0, row=2)

selectOption = tk.StringVar(window)
selectOption.set("Select Operation")
operationMenu = tk.OptionMenu(window, selectOption, "Add", "Subtract", "Multiply", "Divide", "Modulus", "Power", "Square Root")
operationMenu.grid(column=1, row=2)

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
        
        # Perform the selected operation
        operation = selectOption.get()
        if operation == 'Add':
            result = "The addition result is {0}".format(a + b)
        elif operation == 'Subtract':
            result = "The subtraction result is {0}".format(a - b)
        elif operation == 'Multiply':
            result = "The multiplication result is {0}".format(a * b)
        elif operation == 'Divide':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = "The division result is {0}".format(a / b)
        elif operation == 'Modulus':
            result = "The modulus result is {0}".format(a % b)
        elif operation == 'Power':
            result = "The power result is {0}".format(math.pow(a, b))
        elif operation == 'Square Root':
            if a < 0:
                raise ValueError("Cannot take the square root of a negative number.")
            result = "The square root is {0}".format(math.sqrt(a))
        else:
            result = "Please select a valid operation."

    except ValueError as ve:
        result = str(ve)
    except ZeroDivisionError as zde:
        result = str(zde)

    # Display the result in the Text widget
    textArea = tk.Text(master=window, height=7, width=30)
    textArea.grid(column=1, row=4)
    textArea.delete(1.0, tk.END)
    textArea.insert(tk.END, result)

# Calculate button
calculateButton = tk.Button(window, text="Calculate", command=arithmeticOperation, bg="lightgreen")
calculateButton.grid(column=0, row=4)

# Run the application
window.mainloop()
