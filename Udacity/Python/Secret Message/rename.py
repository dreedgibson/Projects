import os

def rename_files():
    # get files names from folder
    path = "C:\Users\Dennis\Desktop\Projects\Udacity\Python\Secret Message\prank"
    file_list = os.listdir(path)
    saved_path = os.getcwd()
    os.chdir(path)

    # for each file, rename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))     
    os.chdir(saved_path)
    
rename_files()
