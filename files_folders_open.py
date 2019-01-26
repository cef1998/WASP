import os
import subprocess
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
path = os.getcwd()
par_path = ""
def open_folder(folder_name):
    try:
        global path,par_path
        st = 'start /MAX "" "'+path+folder_name+'"'
        close_this()
        subprocess.Popen(st, startupinfo=si,shell=True).wait()
        path += folder_name + "\\"
        par_path = os.path.abspath(os.path.join(path,os.pardir))
    except OSError:
        print('Folder Not Found')
        os.system("start /MAX "+par_path)

def open_drive(drive_name):
    global path,par_path
    path = drive_name+":\\"
    par_path = os.path.abspath(os.path.join(path,os.pardir))
    st = 'start /MAX "" '+drive_name+":"
    subprocess.Popen(st, startupinfo=si,shell=True).wait()

def open_file(file_name):
    global path,par_path
    par_path = path
    path += file_name
    st = 'start /MAX "" "'+path+'"'
    subprocess.Popen(st, startupinfo=si,shell=True).wait()

def close_this():
    global path,par_path
    pth = path[:len(path)-1]
    st = 'taskkill /FI "WINDOWTITLE eq '+pth+'*"'
    print(st)
    subprocess.Popen(st, startupinfo=si,shell=True).wait()
    
def close_current_folder():
    try:
        global path,par_path
        par_path = os.path.abspath(os.path.join(path,os.pardir))
        temp_path = r"{}".format(path)
        temp_path.replace('\\\\','\\')
        st = 'taskkill /FI "WINDOWTITLE eq '+os.path.abspath(temp_path)+'*"'
        subprocess.Popen(st, startupinfo=si,shell=True).wait()
        st = 'start /MAX "" "'+par_path+'"'
        subprocess.Popen(st, startupinfo=si,shell=True).wait()
        path = par_path
        print(path)
    except OSError:
        print("File Not Found !!")

def close_current_file(fileName):
    st = 'taskkill /FI "WINDOWTITLE eq '+fileName+'*'
    subprocess.Popen(st, startupinfo=si,shell=True).wait()
