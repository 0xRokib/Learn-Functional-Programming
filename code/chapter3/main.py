# 1. Pure Functions
# Example: Finding the Maximum Value in a List
def find_max(nums):
    max_val = float("-inf")  # Initialize with negative infinity
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

# Input
nums = [3, 1, 4, 1, 5, 9]
# Output
print(find_max(nums))  # Output: 9


# 2. Impure Functions
# Example: Modifying a Global Variable
global_max = float("-inf")  # Global variable

def find_max_impure(nums):
    global global_max  # Access the global variable
    for num in nums:
        if global_max < num:
            global_max = num

# Input
nums = [3, 1, 4, 1, 5, 9]
# Output
find_max_impure(nums)
print(global_max)  # Output: 9


# 3. Pass by Reference vs. Pass by Value
# Example: Modifying a List (Pass by Reference)
def modify_list(inner_lst):
    inner_lst.append(4)  # Modifies the original list

# Input
outer_lst = [1, 2, 3]
# Output
modify_list(outer_lst)
print(outer_lst)  # Output: [1, 2, 3, 4]

# Example: Modifying an Integer (Pass by Value)
def attempt_to_modify(inner_num):
    inner_num += 1  # Modifies a copy of the integer

# Input
outer_num = 1
# Output
attempt_to_modify(outer_num)
print(outer_num)  # Output: 1


# 4. Input and Output (I/O) in Pure Functions
# Example: Converting Text Case
def convert_case(text, target_format):
    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"Unsupported format: {target_format}")

# Input
text = "Hello, World!"
target_format = "uppercase"
# Output
print(convert_case(text, target_format))  # Output: HELLO, WORLD!


# 5. Memoization
# Example: Caching Word Count
def word_count_memo(document, memos):
    memos_copy = memos.copy()  # Create a copy of the memo dictionary
    if document in memos_copy:
        return memos_copy[document], memos_copy  # Return cached result
    word_count = len(document.split())  # Compute word count
    memos_copy[document] = word_count  # Cache the result
    return word_count, memos_copy

# Input
document = "This is a sample document."
memos = {}
# Output
word_count, memos = word_count_memo(document, memos)
print(word_count)  # Output: 5
print(memos)       # Output: {'This is a sample document.': 5}


# 6. Referential Transparency
# Example: Adding Two Numbers
def add(x, y):
    return x + y

# Input
x, y = 2, 3
# Output
print(add(x, y))  # Output: 5


# 7. Custom Commands and Side Effects
# Example: Adding a Custom Command
def add_custom_command(commands, new_command, function):
    commands_copy = commands.copy()  # Create a copy of the commands dictionary
    commands_copy[new_command] = function  # Add the new command
    return commands_copy

# Input
commands = {}
new_command = "greet"
function = lambda: print("Hello!")
# Output
updated_commands = add_custom_command(commands, new_command, function)
print(updated_commands)  # Output: {'greet': <function <lambda> at 0x...>}


# 8. Sorting Dates
# Example: Sorting Dates in "MONTH-DAY-YEAR" Format
def sort_dates(dates):
    return sorted(dates, key=lambda date: date.split("-")[::-1])

# Input
dates = ["12-31-2022", "01-15-2023", "10-05-2022"]
# Output
print(sort_dates(dates))  # Output: ['10-05-2022', '12-31-2022', '01-15-2023']


# 9. Organizing Keywords
# Example: Finding Keywords in a Document
def find_keywords(document):
    keywords = ["functional", "immutable", "declarative"]
    return [keyword for keyword in keywords if keyword in document.lower()]

# Input
document = "Functional programming is declarative and immutable."
# Output
print(find_keywords(document))  # Output: ['functional', 'immutable', 'declarative']