import os
import time
import shutil

path=input("Enter source")
time=time.time()-(30*24*60*60)

if(os.path.exists(path)==true):
    for root_folder, folder, file in os.walk(path):
        folder_path=os.path.join(root_folder, folder)
        file_path=os.path.join(root_folder, file)
        
        if(os.stat(file_path).st_ctime > time):
            os.remove(file_path)
            
        if(os.stat(folder_path).st_ctime > time):
            shutil.rmtree(folder_path)

else:
    print("path not found")
            
            
            
    
