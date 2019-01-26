import speech_recognition as sr
import os
import files_folders_open as ffo
import organizebytype as oft
import music
import utilities

r = sr.Recognizer()
r.energy_threshold=2000
r.operation_timeout = 2

while True:
    with sr.Microphone() as source :
        print("Say something!")
        audio = r.listen( source )
    
    try:
        str = r.recognize_google(audio)
        str = str.lower()
        print(str)
        li = []
        def get_words(str):
            li = str.split()
            return li
             
        li = get_words(str)
        
        def opening(li):
            stri = ""
            open_flag = 0
            file_flag = 0
            drive_flag =  0
            folder_flag = 0
           
            for st in li:
                if st=="open":
                   open_flag = 1
                elif st=="drive":
                   drive_flag = 1
                   stri = li[1]
                elif st=="folder":
                    folder_flag = 1
                elif st=="file":
                    file_flag=1
                
                if len(li) == 0:
                    print("Invalid command")
                    break
                elif(open_flag==1 and drive_flag==1):
                    ffo.open_drive(stri)
                    break
                elif(open_flag==1 and folder_flag==1):
                    li = li[2:]
                    li = "".join(li).lower()
                    file_list = os.listdir(ffo.path)
                    nw_li=[]
                    for i in file_list:
                        tmp = i.split(" ")
                        nw_li.append("".join(tmp).lower())
                    if li in nw_li:
                        stri = file_list[nw_li.index(li)]
                    else :
                        break
                    ffo.open_folder(stri)
                    break
                elif(open_flag==1 and file_flag==1):
                    sz = len(li)
                    li_n = li[2:sz-1]
                    li_n = "".join(li_n).lower()
                    li_n+='.'
                    li_n+=li[-1]
                    li_n = li_n.lower()
                    print(ffo.path)
                    file_list = os.listdir(ffo.path)
                    nw_li=[]
                    for i in file_list:
                        tmp = i.split(" ")
                        nw_li.append("".join(tmp).lower())
                    print(li_n)
                    if li_n in nw_li:
                        stri = file_list[nw_li.index(li_n)]
                    else :
                        break
                    ffo.open_file(stri)
                    break
                elif(str == "organize" or str == "organised"):
                    oft.organize(ffo.path)
                    break
                elif (str == "go back"):
                    ffo.close_current_folder()
                    break
                elif (str == "close"):
                    ffo.close_this()
                    break
                else:
                    continue
        if "open" in li or "Open" in li or "close" in li or "back" in li or "organise" in li:
            opening(li)
        elif ("play" in li or "Play" in li) and ("music" in li or "Music" in li):
            music.play_music(li[1])
        elif "switch" in li:
            utilities.tabs_switching_operation()
        elif "bye" in li:
            break
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
