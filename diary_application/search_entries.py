import os


def search_entries(diary_folder, keyword):
    entries = os.listdir(diary_folder)
    matching_entries = []

    for entry_file in entries:
        with open(os.path.join(diary_folder, entry_file), "r") as file:
            entry_text = file.read()
            if keyword.lower() in entry_text.lower():
                matching_entries.append(entry_text)

    if matching_entries:
        print("\n*** Matching Diary Entries ***\n")
        for entry in matching_entries:
            print(entry)
            print("-" * 40)
    else:
        print("No matching entries found.")
