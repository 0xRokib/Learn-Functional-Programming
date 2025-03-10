# Function Transformations

# --- 1. Higher-Order Function Example ---

# A simple multiply function
def multiply(x, y):
    return x * y

# A simple add function
def add(x, y):
    return x + y

# A higher-order function that returns a new function
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

# Create new functions using self_math with multiply and add
square_func = self_math(multiply)
double_func = self_math(add)

# Test the new functions
print(square_func(5))  # Expected output: 25 (5 * 5)
print(double_func(5))  # Expected output: 10 (5 + 5)


# --- 2. Assignment 1: Logging System ---

# Higher-order function to log messages with a given formatter
def get_logger(formatter):
    def logger(first, second):
        print(formatter(first, second))
    return logger

# Formatter functions for different log formats
def colon_delimit(first, second):
    return f"{first}: {second}"

def dash_delimit(first, second):
    return f"{first} - {second}"

# List of database errors
db_errors = ["out of memory", "cpu is pegged", "networking issue", "invalid syntax"]

# Create a logger with colon_delimit formatter
logger = get_logger(colon_delimit)

# Log errors using the logger
for err in db_errors:
    logger("Doc2Doc FATAL", err)


# --- 3. Assignment 2: Filter Command ---

# Higher-order function to filter content using two filters
def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option == "--one":
            return filter_one(content)
        elif option == "--two":
            return filter_two(content)
        elif option == "--three":
            return filter_two(filter_one(content))
        else:
            raise Exception("invalid option")
    return filter_cmd

# Filter functions
def replace_bad(text):
    return text.replace("bad", "good")

def replace_ellipsis(text):
    return text.replace("..", "...")

# Create a filter command using the replace functions
filter_cmd = get_filter_cmd(replace_bad, replace_ellipsis)

# Test the filter command with different options
print(filter_cmd("This is bad..", "--three"))  # Expected output: This is good...


# --- 4. Assignment 3: Advanced Filter Command ---

# Higher-order function to process content using multiple filters from a dictionary
def get_filter_cmd(filters):
    def filter_cmd(content, options, word_pairs):
        if not options:
            raise Exception("missing options")
        
        for option in options:
            if option in filters:
                content = filters[option](content, word_pairs)
            else:
                raise Exception("invalid option")
        
        return content
    
    return filter_cmd

# Filter functions with word pairs
def replace_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[1])
    return content

def remove_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], "")
    return content

def capitalize_sentences(content, word_pairs):
    return ". ".join(map(str.capitalize, content.split(". ")))

def uppercase_words(content, word_pairs):
    for pair in word_pairs:
        content = content.replace(pair[0], pair[0].upper())
    return content

# Define filters using the functions
filters = {
    "--replace": replace_words,
    "--remove": remove_words,
    "--capitalize": capitalize_sentences,
    "--uppercase": uppercase_words,
}

# Create a filter command with multiple filter options
filter_cmd = get_filter_cmd(filters)

# Test the filter command with the capitalize option
content = "this is a test. hello world."
print(filter_cmd(content, ["--capitalize"], []))  # Expected output: This is a test. Hello world.
