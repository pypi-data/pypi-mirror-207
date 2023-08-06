import os


def get_non_empty_folders(folders):
    non_empty_folders = []

    for folder_path in folders:
        try:
            # Check if the folder exists
            if not os.path.exists(folder_path):
                print(f"Folder '{folder_path}' does not exist")
                continue

            # Check if the folder is empty
            is_empty = True
            for root, dirs, files in os.walk(folder_path):
                if files or dirs:
                    is_empty = False
                    break

            if not is_empty:
                non_empty_folders.append(folder_path)

        except OSError as e:
            print(f"Error occurred while checking folder '{folder_path}': {e}")

    return non_empty_folders