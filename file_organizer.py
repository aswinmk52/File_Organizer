#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import filedialog

def organize_files():
    """Organizes files based on their extensions."""

    # Get the source directory from the user
    source_directory = filedialog.askdirectory(title="Select Source Directory")
    if not source_directory:
        return

    # ... (rest of your file organization logic from the previous example)

    # Categorizing each file extensions to a dictionary
    file_categories = {'.txt':'Documents', '.doc':'Documents', '.docx':'Documents', '.pdf':'Documents', '.xlsx':'Documents', '.jpg':'Images', '.jpeg':'Images', '.png':'Images', '.mp3':'Musics', '.wav':'Musics', '.mp4':'Videos', '.mkv':'Videos', '.psd':'Photoshop_Files', '.exe':'Applications', '.apk':'Applications', '.html':'HTML_Files', '.zip':'Compressed_Files'}

    # Get source directory from the user
    #source_directory = input("Enter the path to the source directory: ")

    # Traverse the source directory
    for filename in os.listdir(source_directory):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Determine the category
        category = file_categories.get(file_extension, 'Others')

        # Create a category path does not exists
        category_path = os.path.join(source_directory, category)
        os.makedirs(category_path, exist_ok = True)

        # Move the file to appropriate category folder
        source_path = os.path.join(source_directory, filename)
        destination_path = os.path.join(category_path, filename)
        os.rename(source_path, destination_path)
    print("File organization completed")
    window.destroy()
# Create the main window
window = tk.Tk()
window.title("File Organizer")

# Create a button to trigger file organization
organize_button = tk.Button(window, text="Organize Files", command=organize_files)
organize_button.pack(pady=20)

# Run the main event loop
window.mainloop()
