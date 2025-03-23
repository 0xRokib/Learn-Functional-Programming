# A function that calculates the volume of a box using currying.
def box_volume(length):
    def with_width(width):
        def with_height(height):
            return length * width * height  # Compute the final volume
        return with_height
    return with_width

print(box_volume(3)(4)(5))  # Output: 60



# Function to adjust font size based on document type using currying.
def converted_font_size(font_size):
    def for_doc_type(doc_type):
        if doc_type == "txt":
            return font_size  # No change for text files
        if doc_type == "md":
            return font_size * 2  # Double font size for markdown
        if doc_type == "docx":
            return font_size * 3  # Triple font size for Word documents
        raise ValueError("invalid doc type")  # Handle invalid document types
    return for_doc_type

print(converted_font_size(12)("md"))  # Output: 24



# Function to count the number of lines containing a specific character sequence.
def lines_with_sequence(char):
    def with_length(length):
        sequence = char * length  # Generate the sequence
        def count_lines(doc):
            return sum(1 for line in doc.split("\n") if sequence in line)  # Count matching lines
        return count_lines
    return with_length

sample_doc = """aaaa
bbbb
ccdd
aabb"""
print(lines_with_sequence("a")(2)(sample_doc))  # Output: 2



# Function to generate an HTML table using currying.
def create_html_table(data_rows):
    rows = "".join(f"<tr>{''.join(f'<td>{cell}</td>' for cell in row)}</tr>" for row in data_rows)
    
    def create_table_headers(headers):
        nonlocal rows
        header_row = "<tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr>"
        return f"<table>{header_row}{rows}</table>"
    
    return create_table_headers

# Generating an HTML table
print(create_html_table([["Row 2, Cell 1", "Row 2, Cell 2"]])(["Header 1", "Header 2"]))



# Function to generate a markdown image link with an optional title using currying.
def create_markdown_image(alt_text):
    def with_url(url):
        url = url.replace("(", "%28").replace(")", "%29")  # Encode parentheses in the URL
        markdown = f"![{alt_text}]({url})"
        def with_title(title=None):
            return markdown if title is None else markdown[:-1] + f' "{title}")'  # Append title if provided
        return with_title
    return with_url

print(create_markdown_image("Example")("https://example.com")("Sample Title"))


# Function to resize an image while ensuring it stays within the specified min/max constraints.
def new_resizer(max_width, max_height):
    def set_min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise ValueError("minimum size cannot exceed maximum size")  # Ensure valid constraints
        def resize_image(width, height):
            # Adjust width and height within limits
            return min(max_width, max(min_width, width)), min(max_height, max(min_height, height))
        return resize_image
    return set_min_size

print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)
