# Python-based command-line application

## Project Description

Develop a Python-based command-line personal diary application that allows users to create and manage their diary entries directly from the terminal. Users should be able to write new entries, view existing entries, search for entries by keywords, and delete entries. The diary entries should be stored in text files- **You don't have to make any GUL** Upload the code as -py file or -zip file.

## Project Requirements

1. **Adding Entries:** Users should be able to add new diary entries with a title and content Each entry should have a unique timestamp.
2. **Viewing Entries:** Users should be able to view a list of all diary entries, displaying titles and timestamps.
3. **Viewing Entry Content:** Users should be able to view the full content of a specific diary entry using its timestamp or title.
4. **Searching Entries:** Users should be able to search for diary entries by providing keywords. The program should display a list of matching entries.
5. **Deleting Entries:** Users should be able to delete specific diary entries using their timestamps or titles.
6. The table columns for diary entries could include the following:
    - **Timestamp:** This column stores the date and time when the diary entry was created. It helps in identifying and sorting entries chronologically.
    - **Title:** This column stores a brief title or subject for the diary entry. It provides a quick overview of what the entry is about.
    - **Content:** This column stores the main content of the diary entry It contains the user's thoughts, reflections, or any information they want to record.

## Solution

This is a Python-based command-line personal diary application that allows users to create and manage their diary entries directly from the terminal. Users can write new entries, view existing entries, search for entries by keywords, and delete entries. Diary entries are stored in text files.

### Features

1. **Adding Entries:** Users can add new diary entries with a title and content. Each entry has a unique timestamp.

2. **Viewing Entries:** Users can view a list of all diary entries, displaying titles and timestamps.

3. **Viewing Entry Content:** Users can view the full content of a specific diary entry using its timestamp or title.

4. **Searching Entries:** Users can search for diary entries by providing keywords, and the program will display a list of matching entries.

5. **Deleting Entries:** Users can delete specific diary entries using their timestamps or titles.

### Project Structure

The project is organized into several Python files for better modularity and reusability:

- `diary.py`: The main script that ties everything together.
- `add_entry.py`: Contains the code for adding diary entries.
- `view_entries.py`: Contains the code for viewing all diary entries.
- `view_entry.py`: Contains the code for viewing the content of a specific diary entry.
- `search_entries.py`: Contains the code for searching diary entries by keyword.
- `delete_entry.py`: Contains the code for deleting diary entries.

## Usage

1. Run `diary.py` to start the application. or Enter the Command `python .\diary.py` after entering the directory where diary.py is stored on your system.
2. Choose from the menu options to perform various diary-related tasks.

## Getting Started

1. Clone this repository to your local machine.

2. Make sure you have Python installed.

3. Create a folder named `diary_entries` in the project directory. This folder will store your diary entries.

4. Run `diary.py` to start the application.

## Dependencies

- Python 3.x

## Author

Upmanyu Jha
