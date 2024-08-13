import os
import shutil

def organize_files(directory_to_organize):
    
    file_type_mapping = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        'Documents': ['pdf', 'docx', 'txt', 'xlsx', 'pptx'],
        'Videos': ['mp4', 'mov', 'avi', 'mkv'],
        'Music': ['mp3', 'wav', 'aac'],
        'Archives': ['zip', 'rar', 'tar', 'gz'],
        'Scripts': ['py', 'js', 'html', 'css']
    }

    
    for folder in file_type_mapping.keys():
        folder_path = os.path.join(directory_to_organize, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

   
    for file_name in os.listdir(directory_to_organize):
        
        if os.path.isdir(os.path.join(directory_to_organize, file_name)):
            continue

   
        file_extension = file_name.split('.')[-1].lower()

        
        for folder, extensions in file_type_mapping.items():
            if file_extension in extensions:
                source = os.path.join(directory_to_organize, file_name)
                destination = os.path.join(directory_to_organize, folder, file_name)
                shutil.move(source, destination)
                break

    print(f"Files in {directory_to_organize} have been organized successfully.")

if __name__ == "__main__":
    
    directory_to_organize = input("Please enter the path of the directory you want to organize: ")
    
    if os.path.exists(directory_to_organize):
        organize_files(directory_to_organize)
    else:
        print("The specified directory does not exist. Please check the path and try again.")
