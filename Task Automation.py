import os
import shutil

# Define the path 
downloads_folder = "/storage/emulated/0/Download"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".sql", ".json", ".md", ".html", ".htm"],
    "Videos": [".mp4", ".mov", ".avi" ,".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".sh", ".bat"],
    "Miscellaneous": [".1-230922.0.", ".x"], 
}

def create_folders():
    for category in file_categories.keys():
        folder_path = os.path.join(downloads_folder, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files():
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in file_categories.items():
                if file_extension in extensions or any(ext in filename.lower() for ext in extensions):
                    dest_folder = os.path.join(downloads_folder, category)
                    shutil.move(file_path, dest_folder)
                    print(f"Moved: {filename} -> {category}")
                    moved = True
                    break
            if not moved:
              
                dest_folder = os.path.join(downloads_folder, "Miscellaneous")
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, dest_folder)
                print(f"Moved: {filename} -> Miscellaneous")

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("File organization complete.")
