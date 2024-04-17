import os
import sys

# python replace_in_directory.py /path/to/directory 'old_text' 'new_text'

def replace_in_file(file_path, old_text, new_text):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if 'title' in line:
                line = line.replace(old_text, new_text)
            file.write(line)

def traverse_directory(directory, old_text, new_text):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                replace_in_file(file_path, old_text, new_text)

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     print("Usage: python replace_in_directory.py <directory_path> <old_text> <new_text>")
    #     sys.exit(1)
    
    folder_path = sys.argv[1]
    # old_text = sys.argv[2]
    # new_text = sys.argv[3]
    old_text = 'blog.aihub2022.top'
    new_text = '从零开始学AI learn AI from Scratch'
    
    traverse_directory(folder_path, old_text, new_text)
    print("替换完成。")
