import tkinter as tk

# Basic Calculator App Using Tkinter as  GUI


# Create a Window using a tkinter object
# - geometry
# - title to give it a heading
# invoke it setting it equal to the window object and using Tk function
window = tk.Tk()
window.geometry("600x300")
window.title("Basic Calculator App")

# Label and Entry field for number 1
number1 = tk.Label(text= "Enter the 1st Number: ")
number1.grid(column=0, row=0)
number1Entry = tk.Entry()
number1Entry.grid(column=1, row=0)

# Label and Entry field for number 2
number2 = tk.Label(text= "Enter the 2nd Number: ")
number2.grid(column=0, row=1)
number2Entry = tk.Entry()
number2Entry.grid(column=1, row=1)

# Select the Operation to perform Label and Drop down Menu
operationLabel = tk.Label(text = "Select the Operation to Perform: ")
operationLabel.grid(column=0, row=2)

selectOption = tk.StringVar(window)
selectOption.set("Select Operation")
operationMenu = tk.OptionMenu(window, selectOption, "Add", "Subtract", "Multiply", "Divide")
operationMenu.grid(column=1, row=2)

# Function to Perform Calculation logic, 
# - takes user input in 2 fields
# - User selects operation to perform 
def arithmeticOperation():
    a = int(number1Entry.get())
    b = int(number2Entry.get())
    operation = selectOption.get()

    if operation == 'Add':
        s = a + b
        result = "The addition result is {0}".format(s)
    elif operation == 'Subtract':
        s = a - b
        result = "The subtraction result is {0}".format(s)
    elif operation == 'Multiply':
        s = a * b
        result = "The multiplication result is {0}".format(s)
    elif operation == 'Divide':
        s = a / b
        result = "The division result is {0}".format(s)
    textArea = tk.Text(master=window, height=7, width=20)
    textArea.grid(column=1, row=3)
    textArea.insert(tk.END, result)


# Note: Button must be place after function definition
calculateButton = tk.Button(window, text="Calculate", command=arithmeticOperation, bg="lightgreen")
calculateButton.grid(column=0,row=3)

# To run the window we need a mainloop() method on our window object
# This method should be called before running any Tkinter application
window.mainloop()
