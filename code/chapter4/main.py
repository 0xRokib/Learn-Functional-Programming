# 1. Factorial Calculation
def factorial_r(x):
    """
    Calculate the factorial of a number using recursion.
    Base Case: If x is 0, return 1.
    Recursive Case: Multiply x by the factorial of x-1.
    """
    if x == 0:  # Base case
        return 1
    return x * factorial_r(x - 1)  # Recursive case

# Example usage
print(factorial_r(5))  # Output: 120


# 2. Zipmap Function
def zipmap(keys, values):
    """
    Create a dictionary by mapping two lists (keys and values) using recursion.
    Base Case: If either list is empty, return an empty dictionary.
    Recursive Case: Map the first key-value pair and recursively process the rest.
    """
    if len(keys) == 0 or len(values) == 0:  # Base case
        return {}
    rest = zipmap(keys[1:], values[1:])  # Recursive case
    rest[keys[0]] = values[0]
    return rest

# Example usage
zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)
print(zipped)
# Output: {'Avatar: The Last Airbender': 9.9, 'Avatar (in Papyrus font)': 6.1, 'The Last Airbender (Live Action)': 2.1}


# 3. Nested Sum
def sum_nested_list(lst):
    """
    Calculate the sum of all integers in a nested list using recursion.
    Base Case: If the item is an integer, add it to the total.
    Recursive Case: If the item is a list, recursively sum its elements.
    """
    total = 0 
    for item in lst:
        if isinstance(item, int):  # Base case
            total += item
        elif isinstance(item, list):  # Recursive case
            total += sum_nested_list(item)
    return total  

# Example usage
root = [1, 2, [3, 4]]
print(sum_nested_list(root))  # Output: 10


# 4. List Files in a Directory
def list_files(parent_directory, current_filepath=""):
    """
    Recursively list all file paths in a nested directory structure represented as a dictionary.
    Base Case: If the value is None, the key is a file, and its path is added to the list.
    Recursive Case: If the value is a dictionary, recursively process the nested directory.
    """
    file_paths = []
    for key in parent_directory:
        new_filepath = current_filepath + "/" + key if current_filepath else key
        if parent_directory[key] == None:  # Base case
            file_paths.append(new_filepath)
        else:  # Recursive case
            file_paths.extend(list_files(parent_directory[key], new_filepath))
    return file_paths

# Example usage
directory = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}

file_paths = list_files(directory)
print(file_paths)
# Output: ['/Documents/Proposal.docx', '/Documents/Receipts/January/receipt1.txt', '/Documents/Receipts/January/receipt2.txt', '/Documents/Receipts/February/receipt3.txt']