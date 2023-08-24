import os
import datetime


def create_diary_entry(diary_folder):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    title = input("Enter the title of the entry: ")
    content = input("Enter the content of the entry: ")

    entry = f"Timestamp: {timestamp}\nTitle: {title}\nContent:\n{content}"

    entry_file = os.path.join(diary_folder, f"{timestamp}.txt")

    with open(entry_file, "w") as file:
        file.write(entry)

    print("\nDiary entry created successfully!")
