# Pythono3 code to rename multiple
# files in a directory or folder
 
# importing os module
import os
 
# Function to rename multiple files
def main():
   
    folder = "./dataset"
    for count, filename in enumerate(os.listdir(folder)):
        dst = filename[1:]
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)

main()