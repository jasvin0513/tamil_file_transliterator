import sys
import os
from transliterator import transliterate

if len(sys.argv) != 2:
    print("Usage: python script.py <directory>")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"The specified path '{directory}' is not a directory.")
    sys.exit(1)

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        transliterated_name = transliterate(filename)
        formatted_name = transliterated_name.replace("_", " ")
        new_file_path = os.path.join(directory, formatted_name)
        os.rename(file_path, new_file_path)
