import os

def list_files_in_folder(folder_path):
    # Kontrollera om mappen finns
    if not os.path.isdir(folder_path):
        print("Mappen existerar inte.")
        return
    
    # Hämta alla filer i mappen
    pathes = os.listdir(folder_path)
    files = []
    for x in pathes:
        if os.path.isfile(os.path.join(folder_path, x)):
            files.append(x)
 

    
    for i in range(len(files)-1):
        file = files[i]
        if os.path.isfile(os.path.join(folder_path, file)):
            print(file)
            

folder_path = "c:\msys64"

list_files_in_folder(folder_path)