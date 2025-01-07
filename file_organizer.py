#!/usr/bin/env python3

import os

# Categorizing each file extensions to a dictionary
file_categories = {'.txt':'Documents', '.doc':'Documents', '.docx':'Documents', '.pdf':'Documents', '.jpg':'Images', '.jpeg':'Images', '.png':'Images', '.mp3':'Musics', '.wav':'Musics', '.mp4':'Videos'}

# Get source directory from the user
source_directory = input("Enter the path to the source directory")

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

