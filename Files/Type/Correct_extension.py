import os
import mimetypes
import magic

def check(file_path):
    mime_type = magic.from_file(file_path,mime=True)
    if mime_type:
        correct_extension = mimetypes.guess_extension(mime_type)
        if correct_extension != os.path.splitext(file_path)[1]:
            new_file_path = os.path.splitext(file_path)[0] + correct_extension
            return file_path, new_file_path
    return None, None

def correct_file_extensions(folder_path):
    original = []
    corrected = []
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_path, new_file_path = check(file_path)
                if file_path:
                    original.append(file_path)
                    corrected.append(new_file_path)
    except Exception as e:
        print("Folder not found. Try it as a file path.")
        try:
            file_path, new_file_path = check(folder_path)
            if file_path:
                original.append(file_path)
                corrected.append(new_file_path)
        except FileNotFoundError:
            print("File not found! Please enter a valid folder path or file path.")
    return original, corrected

folder_path = input("Enter the folder path: ")
original, corrected = correct_file_extensions(folder_path)
if len(original) > 0:
    print(f"Find {len(original)} files with incorrect extensions:")
    if len(original) > 10:
        choose = input("Too many files to display, do you want to display them all? (y/N): ")
        if choose.lower() == 'y':
            for i in range(len(original)):
                print(f"{original[i]} -> {corrected[i]}")
    else:
        for i in range(len(original)):
            print(f"{original[i]} -> {corrected[i]}")
    print("=====================================")
    choose = input("Do you want to correct the extensions? (Y/n): ")
    if choose.lower() != 'n':
        for i in range(len(original)):
            os.rename(original[i], corrected[i])
        print("Extensions corrected successfully.")
else:
    print("=====================================")
    print("No files with incorrect extensions found.")