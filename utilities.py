import zipfile
import os
import subprocess
from pynput.keyboard import Key, Controller
import time

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW


def compress_file(path):
    ind = path.rfind("\\")
    zpath = path[:ind]
    zpath += "\\" 
    li = []
    li = path.split("\\")
    zpath += path.split("\\")[len(li) - 1] + ".zip"
    
    fzip = zipfile.ZipFile(zpath, 'w')
    
    for folder, subfolders, files in os.walk(path):
        for file in files:
            fzip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), path), compress_type = zipfile.ZIP_DEFLATED)
    
    fzip.close()

def decompress_file(path):
    ind = path.rfind(".")
    dpath = path[:ind]
    fzip = zipfile.ZipFile(path)
    fzip.extractall(dpath)
    fzip.close()

def tabs_switching_operation() :
    keyboard = Controller()
    keyboard.press(Key.alt)
    time.sleep(0.5)
    keyboard.press(Key.tab)
    time.sleep(0.5)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)  

def search_file(path, file_name):
    #path is the path of directory where file is located
    file_list = os.listdir(path)
    if file_name in file_list:
        print("File Exists in: ", path)
    else:
        print("File not found")

def rename_file(path, file_name, after_rename):
    file_list = os.listdir(path)

    if file_name in file_list:
        if(after_rename == file_name):
            print('File already exists')
        cur_path = path+'/'+file_name
        renamed_path = path+'/'+after_rename
        os.rename(cur_path, renamed_path)
    else :
        print("Cannot rename file! File does not exist")

def shutdown():
    subprocess.Popen("shutdown /s", startupinfo=si, shell=True).wait()

def restart():
    subprocess.Popen("shutdown /r", startupinfo=si, shell=True).wait()