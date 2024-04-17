import sys
import re

def format_markdown(input_file):
    output_file = input_file.replace('.md', '.clean.md')

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove URL part from markdown syntax except for image syntax
    formatted_content = re.sub(r'(?<!\!)\[([^\[\]]+)\]\((.*?)\)', r'[\1]', content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    print(f"Formatted content written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python markdown-cleaner.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    format_markdown(input_file)
