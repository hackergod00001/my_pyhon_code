import os


def view_entry_content(diary_folder, timestamp_or_title):
    entries = os.listdir(diary_folder)
    entry_found = False

    for entry_file in entries:
        with open(os.path.join(diary_folder, entry_file), "r") as file:
            entry_text = file.read()
            if timestamp_or_title.lower() in entry_text.lower():
                print("\n*** Diary Entry ***\n")
                print(entry_text)
                entry_found = True
                break

    if not entry_found:
        print("Entry not found.")
