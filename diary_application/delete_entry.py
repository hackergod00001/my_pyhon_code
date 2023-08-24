import os


def delete_entry(diary_folder, timestamp_or_title):
    entries = os.listdir(diary_folder)
    entry_found = False

    for entry_file in entries:
        with open(os.path.join(diary_folder, entry_file), "r") as file:
            entry_text = file.read()
            if timestamp_or_title.lower() in entry_text.lower():
                try:
                    os.remove(os.path.join(diary_folder, entry_file))
                    print("\nDiary entry deleted successfully.")
                except PermissionError:
                    print("File is in use. Please try again later.")
                entry_found = True
                break

    if not entry_found:
        print("Entry not found.")
