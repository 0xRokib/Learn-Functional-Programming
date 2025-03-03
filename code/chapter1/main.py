# Mutable vs. Immutable Data

# Lists Are Mutable:
ages = [16, 21, 30]  # A list of ages
ages.append(80)  # Adding a new element to the list (modifies the original list)
# Result: [16, 21, 30, 80]


# Tuples Are Immutable:
ages = (16, 21, 30)  # A tuple of ages
more_ages = (80,)  # A new single-element tuple (comma is required)
all_ages = ages + more_ages  # Creating a new tuple (original tuple remains unchanged)
# Result: (16, 21, 30, 80)


# Imperative vs. Declarative Code
# Imperative Styling (Python with Tkinter):
from tkinter import *  # Import Tkinter module=
master = Tk()  # Create a main window
master.geometry("200x100")  # Set window size
button = Button(master, text="Submit", fg="red").pack()  # Create a red button
master.mainloop()  # Start the GUI event loop


# Imperative vs. Functional Approach for Averaging Numbers

# Imperative Approach:
def get_average(nums):
    total = 0  # Initialize total sum
    for num in nums:  # Iterate over the list
        total += num  # Accumulate sum
    return total / len(nums)  # Return average

# Example usage:
# get_average([10, 20, 30]) -> 20.0


# Functional Approach:
def get_average(nums):
    return sum(nums) / len(nums)  # Use built-in sum function for a declarative approach

# Example usage:
# get_average([10, 20, 30]) -> 20.0



