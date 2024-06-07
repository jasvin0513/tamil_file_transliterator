import sys
import os
from transliterator import transliterate

def truncate_filename(filename, max_length):
    if len(filename) <= max_length:
        return filename
    else:
        # Find the position of the ".mp3" extension
        extension_index = filename.rfind(".mp3")
        # Truncate the filename before the ".mp3" extension
        truncated_name = filename[:max_length - 4] + filename[extension_index:]
        return truncated_name

if len(sys.argv) != 2:
    print("Usage: python script.py <directory>")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"The specified path '{directory}' is not a directory.")
    sys.exit(1)

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path) and filename.endswith(".mp3"):
        transliterated_name = transliterate(filename)
        formatted_name = transliterated_name.replace("_", " ")
        new_formatted_name = truncate_filename(formatted_name, 40)
        new_file_path = os.path.join(directory, new_formatted_name)
        os.rename(file_path, new_file_path)