import os

def delete_downloads():
    downloads_path = os.path.expanduser("~") + "/Downloads"  

    try:
        
        files = os.listdir(downloads_path)

        
        for file_name in files:
            file_path = os.path.join(downloads_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        print("All files in Downloads deleted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_downloads()
