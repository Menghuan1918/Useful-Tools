import os
import mimetypes

def correct_file_extensions(folder_path):
    original = []
    corrected = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type:
                correct_extension = mimetypes.guess_extension(mime_type)
                if correct_extension != os.path.splitext(filename)[1]:
                    new_file_path = os.path.splitext(file_path)[0] + correct_extension
                    original.append(file_path)
                    corrected.append(new_file_path)
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