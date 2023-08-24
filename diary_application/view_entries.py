import os


def view_all_entries(diary_folder):
    entries = os.listdir(diary_folder)

    if entries:
        print("\n*** All Diary Entries ***\n")
        for entry_file in entries:
            with open(os.path.join(diary_folder, entry_file), "r") as file:
                entry_text = file.read().split("\n")
                timestamp = entry_text[0].replace("Timestamp: ", "")
                title = entry_text[1].replace("Title: ", "")
                content = entry_text[3]
                print(f"Timestamp: {timestamp}")
                print(f"Title: {title}")
                print(f"Content:\n{content}\n")
                print("-" * 40)
    else:
        print("No entries found.")
