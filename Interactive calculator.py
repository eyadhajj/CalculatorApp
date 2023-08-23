import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1_value = float(Calculator.num1.get())  # Get the value from the first Entry widget
        num2_value = float(Calculator.num2.get())  # Get the value from the second Entry widget
        result = num1_value + num2_value
        messagebox.showinfo("Result", f"Sum: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values.")

def subtract():
    try:
        num1_value = float(Calculator.num1.get())  # Get the value from the first Entry widget
        num2_value = float(Calculator.num2.get())  # Get the value from the second Entry widget
        result = num1_value - num2_value
        messagebox.showinfo("Result", f"Subtraction value: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values.")

def divide():
    try:
        num1_value = float(Calculator.num1.get())  # Get the value from the first Entry widget
        num2_value = float(Calculator.num2.get())  # Get the value from the second Entry widget
        result = num1_value / num2_value
        messagebox.showinfo("Result", f"Division value: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values.")

def multiply():
    try:
        num1_value = float(Calculator.num1.get())  # Get the value from the first Entry widget
        num2_value = float(Calculator.num2.get())  # Get the value from the second Entry widget
        result = num1_value * num2_value
        messagebox.showinfo("Result", f"Multiplication value: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values.")

class Numbers():
    def input_one():
        Calculator.num1.insert(tk.END, "1")

    def input_one_2():
        Calculator.num2.insert(tk.END, "1")

    def input_two():
        Calculator.num1.insert(tk.END, "2")

    def input_two_2():
        Calculator.num2.insert(tk.END, "2")

    def input_three():
        Calculator.num1.insert(tk.END, "3")

    def input_three_2():
        Calculator.num2.insert(tk.END, "3")

    def input_four():
        Calculator.num1.insert(tk.END, "4")

    def input_four_2():
        Calculator.num2.insert(tk.END, "4")

    def input_five():
        Calculator.num1.insert(tk.END, "5")

    def input_five_2():
        Calculator.num2.insert(tk.END, "5")

    def input_six():
        Calculator.num1.insert(tk.END, "6")

    def input_six_2():
        Calculator.num2.insert(tk.END, "6")

    def input_seven():
        Calculator.num1.insert(tk.END, "7")

    def input_seven_2():
        Calculator.num2.insert(tk.END, "7")

    def input_eight():
        Calculator.num1.insert(tk.END, "8")

    def input_eight_2():
        Calculator.num2.insert(tk.END, "8")

    def input_nine():
        Calculator.num1.insert(tk.END, "9")

    def input_nine_2():
        Calculator.num2.insert(tk.END, "9")

    def input_zero():
        Calculator.num1.insert(tk.END, "0")

    def input_zero_2():
        Calculator.num2.insert(tk.END, "0")

    def input_dot():
        Calculator.num1.insert(tk.END, ".")

    def input_dot_2():
        Calculator.num2.insert(tk.END, ".")

class Calculator():
    # Create the main application window
    root = tk.Tk()
    root.title("Calculator App")


    # Create a frame to hold the input widgets
    input_frame = tk.Frame(root)
    input_frame.pack(padx=100, pady=50)

    # Create a label widget
    label = tk.Label(root, text="Welcome to my Calculator App!")
    label.pack(padx=10, pady=10, side="top")

    # Create Entry widgets for integer input
    num1 = tk.Entry(root)
    num1.pack(padx=10, pady=10)

    num2 = tk.Entry(root)
    num2.pack(padx=10, pady=10)

    # Create a button widget
    button = tk.Button(root, text="Add (+)", command=add)
    button.pack(padx=10, pady=10, side="left")

    # Create a button widget
    button = tk.Button(root, text="Subtract (-)", command=subtract)
    button.pack(padx=10, pady=10, side="left")

    # Create a button widget
    button = tk.Button(root, text="Multiplication (*)", command=multiply)
    button.pack(padx=10, pady=10, side="right")

    # Create a button widget
    button = tk.Button(root, text="Division (/)", command=divide)
    button.pack(padx=10, pady=10, side="left")

"""
    # Create a button widget to input "1"
    input1_button = tk.Button(input_frame, text="1", command=Numbers.input_one)
    input1_button.pack(side="left", padx=5, pady=5)

    # Create a button widget to input "1"
    input1_button2 = tk.Button(input_frame, text="1", command=Numbers.input_one_2)
    input1_button2.pack(side="right", padx=5, pady=5)


    # Create a button widget to input "2"
    input1_button = tk.Button(input_frame, text="2", command=Numbers.input_two)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "2"
    input1_button2 = tk.Button(input_frame, text="2", command=Numbers.input_two_2)
    input1_button2.pack(side="right", padx=5, pady=5)


    # Create a button widget to input "3"
    input1_button = tk.Button(input_frame, text="3", command=Numbers.input_three)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "3"
    input1_button2 = tk.Button(input_frame, text="3", command=Numbers.input_three_2)
    input1_button2.pack(side="right", padx=5, pady=5)

    # Create a button widget to input "4"
    input1_button = tk.Button(input_frame, text="4", command=Numbers.input_four)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "4"
    input1_button2 = tk.Button(input_frame, text="4", command=Numbers.input_four_2)
    input1_button2.pack(side="right", padx=5, pady=5)


    # Create a button widget to input "5"
    input1_button = tk.Button(input_frame, text="5", command=Numbers.input_five)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "5"
    input1_button2 = tk.Button(input_frame, text="5", command=Numbers.input_five_2)
    input1_button2.pack(side="right", padx=5, pady=5)

    # Create a button widget to input "6"
    input1_button = tk.Button(input_frame, text="6", command=Numbers.input_six)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "6"
    input1_button2 = tk.Button(input_frame, text="6", command=Numbers.input_six_2)
    input1_button2.pack(side="right", padx=5, pady=5)

    # Create a button widget to input "7"
    input1_button = tk.Button(input_frame, text="7", command=Numbers.input_seven)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "7"
    input1_button2 = tk.Button(input_frame, text="7", command=Numbers.input_seven_2)
    input1_button2.pack(side="right", padx=5, pady=5)

    # Create a button widget to input "8"
    input1_button = tk.Button(input_frame, text="8", command=Numbers.input_eight)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "8"
    input1_button2 = tk.Button(input_frame, text="8", command=Numbers.input_eight_2)
    input1_button2.pack(side="right", padx=5, pady=5)

    # Create a button widget to input "9"
    input1_button = tk.Button(input_frame, text="9", command=Numbers.input_nine)
    input1_button.pack(side="left", padx=5, pady=5)


    # Create a button widget to input "9"
    input1_button2 = tk.Button(input_frame, text="9", command=Numbers.input_nine_2)
    input1_button2.pack(side="right", padx=5, pady=5)
    """

# Start the main event loop
Calculator.root.mainloop()
