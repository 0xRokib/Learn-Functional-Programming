# Decorator to count vowels in the input document
def vowel_counter(func_to_decorate):
    def wrapper(doc):
        # Count vowels in the document
        vowel_count = sum(1 for char in doc if char.lower() in "aeiou")
        print(f"Vowel count: {vowel_count}")
        # Call the original function
        return func_to_decorate(doc)
    return wrapper

@vowel_counter  # Applying the decorator
def process_doc(doc):
    print(f"Document: {doc}")

# Using the decorated function
process_doc("Hello World")



# Function to log both positional and keyword arguments
def args_logger(*args, **kwargs):
    # Log positional arguments
    for i, arg in enumerate(args, 1):
        print(f"{i}. {arg}")
    
    # Log keyword arguments, sorted by key
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")

# Example usage
args_logger("hello", "world", a=1, b=2)


# Decorator to log the number of times a function is called
def log_call_count(func_to_decorate):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        return func_to_decorate(*args, **kwargs)
    return wrapper

@log_call_count  # Applying the decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")




# Helper function to remove Markdown syntax
def convert_md_to_txt(text):
    return text.replace("#", "").strip()

# Decorator to remove Markdown syntax from string arguments
def markdown_to_text_decorator(func_to_decorate):
    def wrapper(*args, **kwargs):
        # Convert all string arguments to plain text
        new_args = [convert_md_to_txt(arg) if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: convert_md_to_txt(value) if isinstance(value, str) else value for key, value in kwargs.items()}
        return func_to_decorate(*new_args, **new_kwargs)
    return wrapper

@markdown_to_text_decorator  # Applying the decorator
def display_text(text):
    print(text)

# Using the decorated function
display_text("# Hello World")




# Function to replace a specific string in the text
def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            return decorated_func(text.replace(old, new))
        return wrapper
    return replace

# Decorators to escape HTML special characters
@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return text

# Example usage
print(tag_pre("<div>Sample & text</div>"))



from functools import lru_cache

# Decorator to cache the results of the factorial function
@lru_cache()
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(10))  # Computes factorial of 10
print(factorial(5))   # Computes factorial of 5 using cache



from functools import lru_cache

# Function to check if a word is a palindrome
@lru_cache()
def is_palindrome(word):
    # Base case: If word length is 1 or less, it's a palindrome
    if len(word) <= 1:
        return True
    # If the first and last characters are different, it's not a palindrome
    if word[0] != word[-1]:
        return False
    # Recursively check the middle part of the word
    return is_palindrome(word[1:-1])

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
