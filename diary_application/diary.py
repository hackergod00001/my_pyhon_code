import os
import datetime
from add_entry import create_diary_entry
from view_entries import view_all_entries
from view_entry import view_entry_content
from search_entries import search_entries
from delete_entry import delete_entry

# Get the absolute path of the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the absolute path to the diary_entries folder
DIARY_FOLDER = os.path.join(script_dir, "diary_entries")


def main():
    if not os.path.exists(DIARY_FOLDER):
        os.makedirs(DIARY_FOLDER)

    while True:
        print("\n*** Personal Diary ***")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. View Entry Content")
        print("4. Search Entries")
        print("5. Delete Entry")
        print("6. Exit")

        choice = input("Select an option (1/2/3/4/5/6): ")

        if choice == "1":
            create_diary_entry(DIARY_FOLDER)
        elif choice == "2":
            view_all_entries(DIARY_FOLDER)
        elif choice == "3":
            timestamp_or_title = input(
                "Enter the timestamp or title of the entry you want to view: ")
            print("-" * 40)
            view_entry_content(DIARY_FOLDER, timestamp_or_title)
            print("-" * 40)
        elif choice == "4":
            keyword = input("Enter a keyword to search for entries: ")
            print("-" * 40)
            search_entries(DIARY_FOLDER, keyword)
            print("-" * 40)
        elif choice == "5":
            timestamp_or_title = input(
                "Enter the timestamp or title of the entry you want to delete: ")
            delete_entry(DIARY_FOLDER, timestamp_or_title)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
