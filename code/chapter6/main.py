# 1. Word Count Aggregator
def word_count_aggregator():
    # Initialize a count variable to track total words
    count = 0
    
    def add_word_count(doc):
        """Counts the words in the given document and updates the total count."""
        nonlocal count
        count += len(doc.split())  # Count words in the current document
        return count  # Return updated total word count
    
    return add_word_count

# Example usage
counter = word_count_aggregator()
print(counter("Hello world"))  # Output: 2
print(counter("Python closures are useful"))  # Output: 5


# 2. New Collection (without modifying the original list)
def new_collection(initial_docs):
    # Create a copy of the initial document list to prevent modification
    docs = initial_docs[:]
    
    def add_doc(doc):
        """Adds a new document to the collection."""
        docs.append(doc)
        return docs  # Return updated list
    
    return add_doc

# Example usage
collection = new_collection(["doc1", "doc2", "doc3"])
print(collection("doc4"))  # Output: ['doc1', 'doc2', 'doc3', 'doc4']


# 3. Clipboard System
def new_clipboard():
    # Dictionary to store copied key-value pairs
    clipboard = {}
    
    def copy_to_clipboard(key, value):
        """Copies a key-value pair to the clipboard."""
        clipboard[key] = value

    def paste_from_clipboard(key):
        """Returns the value from the clipboard for the given key or an empty string if not found."""
        return clipboard.get(key, "")
    
    return copy_to_clipboard, paste_from_clipboard

# Example usage
copy, paste = new_clipboard()
copy("greeting", "Hello World!")
print(paste("greeting"))  # Output: Hello World!
print(paste("missing_key"))  # Output: ""


# 4. User Words (Adding words to spellchecker)
def user_words(initial_words):
    # Convert the tuple to a set for efficient word storage
    words = set(initial_words)
    
    def add_word(word):
        """Adds a new word to the spellchecker."""
        words.add(word)
        return tuple(words)  # Return words as a tuple
    
    return add_word

# Example usage
spell_checker = user_words(("hello", "world"))
print(spell_checker("Python"))  # Output: ('hello', 'world', 'Python')



# 5. CSS Styles Management
def css_styles(initial_styles):
    # Create a copy of the initial styles dictionary to avoid modifying the original
    styles = {k: v.copy() for k, v in initial_styles.items()}
    
    def add_style(selector, property, value):
        """Adds or updates a CSS style for a given selector."""
        if selector not in styles:
            styles[selector] = {}  # Create a new dictionary for the selector if not present
        styles[selector][property] = value  # Update or add the style property
        return styles  # Return the updated styles dictionary
    
    return add_style

# Example usage
styles = css_styles({"body": {"color": "black"}})
print(styles("h1", "font-size", "24px"))
# Output: {'body': {'color': 'black'}, 'h1': {'font-size': '24px'}}


# 6. Line Breaking
def line_breaker(line_length):
    def add_word_to_lines(lines, word):
        """Breaks text into lines based on the specified line length."""
        if not lines:
            return [word]  # If no lines exist, create the first line with the word
        
        current_line = lines[-1]
        if len(current_line) + len(word) + 1 > line_length:
            lines.append(word)  # Start a new line if adding the word exceeds length
        else:
            lines[-1] += " " + word  # Append word to the last line with a space
        
        return lines  # Return updated lines list
    
    return add_word_to_lines

# Example usage
breaker = line_breaker(10)
print(breaker([], "Hello"))  # Output: ['Hello']
print(breaker(["Hello"], "World!"))  # Output: ['Hello World!']



# 7. Currying Example (Converted Font Size)
def converted_font_size(font_size):
    """Returns a function that applies font scaling based on document type."""
    def apply_doc_type(doc_type):
        scaling = {"header": 2, "body": 1, "footer": 0.8}  # Define scaling factors
        return font_size * scaling.get(doc_type, 1)  # Apply scaling based on doc_type
    
    return apply_doc_type

# Example usage
font_converter = converted_font_size(12)
print(font_converter("header"))  # Output: 24
print(font_converter("body"))  # Output: 12
print(font_converter("footer"))  # Output: 9.6


# 8. Document Formatter 
def document_formatter():
    # Initialize an empty document string
    document = ""
    
    def add_content(content):
        """Appends content to the document string."""
        nonlocal document
        document += content
        return document  # Return updated document
    
    return add_content


