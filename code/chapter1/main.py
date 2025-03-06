# =========================================================
# 1. Mutable vs. Immutable Data
# =========================================================

# 1.1 Lists Are Mutable
ages = [16, 21, 30]  # A list of ages
ages.append(80)  # Adding a new element to the list (modifies the original list)
print(ages)  # Output: [16, 21, 30, 80]


# 1.2 Tuples Are Immutable
ages = (16, 21, 30)  # A tuple of ages
more_ages = (80,)  # A new single-element tuple (comma is required)
all_ages = ages + more_ages  # Creating a new tuple (original tuple remains unchanged)
print(all_ages)  # Output: (16, 21, 30, 80)


# =========================================================
# 2. Imperative vs. Declarative Code
# =========================================================

# 2.1 Imperative Styling (Python with Tkinter)
from tkinter import *  # Import Tkinter module

# Create a main window
master = Tk()  
master.geometry("200x100")  # Set window size

# Create a red button and pack it into the window
button = Button(master, text="Submit", fg="red").pack()  

# Start the GUI event loop
master.mainloop()  


# =========================================================
# 3. Imperative vs. Functional Approach for Averaging Numbers
# =========================================================

# 3.1 Imperative Approach
def get_average(nums):
    """Calculates the average of a list of numbers using an imperative approach."""
    total = 0  # Initialize total sum
    for num in nums:  # Iterate over the list
        total += num  # Accumulate sum
    return total / len(nums)  # Return average

# Example usage:
print(get_average([10, 20, 30]))  # Output: 20.0


# 3.2 Functional Approach
def get_average(nums):
    """Calculates the average of a list of numbers using a functional approach."""
    return sum(nums) / len(nums)  # Use built-in sum function for a declarative approach

# Example usage:
print(get_average([10, 20, 30]))  # Output: 20.0