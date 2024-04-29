import os
import imghdr
import tkinter as tk
from tkinter import font

def correct_image_extensions(directory):
    corrected_files = []
    for filename in os.listdir(directory):
        if not os.path.isfile(os.path.join(directory, filename)):
            continue

        file_path = os.path.join(directory, filename)
        try:
            image_format = imghdr.what(file_path)
            if image_format:
                correct_extension = f".{image_format}"
                if not filename.lower().endswith(correct_extension):
                    new_filename = f"{os.path.splitext(filename)[0]}{correct_extension}"
                    new_file_path = os.path.join(directory, new_filename)
                    os.rename(file_path, new_file_path)
                    corrected_files.append(new_filename)
            print(f"Processed {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    return corrected_files

root = tk.Tk()
root.withdraw()
root.geometry("800x600")
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=20)

from tkinter import filedialog

directory = filedialog.askdirectory(title="Select Directory")
if not directory:
    print("No directory selected. Exiting.")
    exit()

corrected_files = correct_image_extensions(directory)

print(f"Find and corrected {len(corrected_files)} files.")
