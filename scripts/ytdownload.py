import subprocess as sb
import os

#global shit
app = "youtube-dl"
path = "-o '$HOME/Downloads/youtube-dl_songs/%(channel)s/%(title)s - %(channel)s.%(ext)s'"
title = "-f bestaudio -o '%(title)s - %(channel)s.%(ext)s'"
audiodownload = "-f bestaudio --extract-audio --audio-format mp3 --audio-quality 0"
thumbnaildownload = "--write-thumbnail --skip-download"
filename = "--get-filename"
#function to check if name is present or not
def check_name(name):
    names = []
    #load names form the history file
    with open("yt-download_history.txt",'r') as f:
        for line in f.readlines():
            l = line.strip("\n")
            names.append(l)
    f.close()
    if name in names:
        return True
    else:
        return False

#generate bash file
def generate_bash():
    with open("command.bash","w") as f:
        f.write(f"{app} {path} {audiodownload} {link}\n")
        f.write(f"{app} {path} {thumbnaildownload} {link}\n")
        f.write(f"{app} {title} {link} {filename} >> yt-download_history.txt")
    f.close()



link = input()

#get the video name
command = f"{app} {title} {link} {filename}"

name = sb.check_output(command,shell=True).decode().strip("\n")
if check_name(name):
    print("[*] Song is already Downloaded\n[*] Want to download again: ")
    x = input()
    if x == "y" or x =="Y":
        #store data in command.bash file and execute it
        generate_bash()
        os.system("./command.bash")
    else:
        exit(1)
else:
    generate_bash()
    os.system("./command.bash")
