###############################################################
#####     ORGANIZE IMAGES BY MODIFIED YEAR                #####
#####     AUTHOR: GARRETT PETER BARDINI (GPB)             #####
#####     CREATE_DATE: 2022/09/16                         #####
#####     LAST_MODIFIED: 2022/09/16                       #####
###############################################################
import os
import time
import shutil

folder = input('Input a Folder Path with images you would like to organize by modified year: ')
start_time = time.time()
for dir_, _, files in os.walk(folder):
    for file_name in files:
        file_path = os.path.join(dir_, file_name)
        # file_year_c = time.ctime(os.path.getctime(file_path))[-4:] # CREATE DATE | SYSTEM DATE 
        file_year_m = time.ctime(os.path.getmtime(file_path))[-4:] # LAST MODIFIED DATE | SOURCE DATE
        new_path = os.path.join(folder,file_year_m)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        shutil.move(file_path,os.path.join(new_path,file_name))

for path, _, _ in os.walk(folder, topdown=False):
    if len(os.listdir(path)) == 0:
        print(f"Removing Folder: {path}")
        os.rmdir(path)

execution_time = (time.time() - start_time)
print('Executed in: ' + str(execution_time) + '  seconds.') 