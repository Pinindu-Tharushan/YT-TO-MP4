from __future__ import unicode_literals
import youtube_dl
import os

os.system("apt update && apt upgrade")
os.system("pkg install nano")
os.system("clear")
print('''\007

\033[1;33m  _     _________   _______ ____     __  __ _____  _  _   
\033[1;32m \ \   / /__   __| |__   __/ __ \   |  \/  |  __ \| || |  
\033[1;33m  \ \_/ /   | |       | | | |  | |  | \  / | |__) | || |_ 
\033[1;32m   \   /    | |       | | | |  | |  | |\/| |  ___/|__   _|
\033[1;33m    | |     | |       | | | |__| |  | |  | | |       | |  
\033[1;32m    |_|     |_|       |_|  \____/   |_|  |_|_|       |_|  
                                                                                                                                                                                                       
\033[1;91mv1.1
\033[1;36m =============================================\033[1;m
\033[1;33m|         BEST YOUTUBE TO MP4 CONVERTER       |
\033[1;36m =============================================\033[00m''')

print()
print("[1] සිංහල ")
print("[2] English ")
print()
print("ඔබගේ භාෂාව තෝරන්න: ")
print("Select Your language: ")
ya = input("[+]=====> ")

x = ""

if ya == "1":
    sinhala();
elif ya == "2":
    english();
else:
    print("වැරදි ඇතුලත් කිරීමකි...!")
    print("invalid number...!")
    

def sinhala():
    x = input("වීඩියෝවෙහි LINK එක ඇතුලත් කරන්න: ")
    print()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([x])
    print()
    print("වීඩියෝ එක ඩවුන්ලෝඩ් වෙලා ඉවරයි....!")
    print("ඒක ඔබේ ඩිවයිස් එකට දාගන්න ඕන නං පහත ක්‍රමය අනුගමනය කරන්න.")
    print()
    print("nano sinhala.txt")
    print()
    print("ඉහත සදහන් ආකාරයට එම පාටය ඔබගේ terminal එකේ type කරන්න.")
    
    
def english():
    x = input("Video URL Address: ")
    ydl_opts = {}
    print()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([x])
    print()
    print("The video has been downloaded.")
    print("If you want to install it on your device, follow the step below.")
    print()
    print("nano english.txt")
    print()
    print("Type the same color in your terminal as mentioned above.")
    