from __future__ import unicode_literals
import youtube_dl
import os

os.system("clear")
print('''\007

\033[1;33m  _     _________   _______ ____     __  __ _____ _  _   
\033[1;32m \ \   / /__   __| |__   __/ __ \   |  \/  |  __ \ || |  
\033[1;33m  \ \_/ /   | |       | | | |  | |  | \  / | |__) ||| |_ 
\033[1;32m   \   /    | |       | | | |  | |  | |\/| |  ___/__   _|
\033[1;33m    | |     | |       | | | |__| |  | |  | | |      | |  
\033[1;32m    |_|     |_|       |_|  \____/   |_|  |_|_|      |_|\033[5;31m\033[1;91mv1.9

\033[1;36m =============================================\033[1;m
\033[1;33m|         BEST YOUTUBE TO MP4 CONVERTER       |
\033[1;36m =============================================\033[00m''')

print()
print('''\033[0;36m[1] සිංහල ''')
print('''\033[0;36m[2] English ''')
print()
print("\033[0;35mඔබගේ භාෂාව තෝරන්න: ")
print("\033[0;35mSelect Your language: ")
ya = input('''\033[5;31m[+]=====> ''')
print()

x = ""

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
    print('''\033[7;31m\033[0;35mnano sinhala.txt''')
    print()
    print("ඉහත සදහන් ආකාරයට එම පාටය ඔබගේ terminal එකේ type කරන්න.")
    print()
    
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
    print('''\033[7;31m\033[0;35mnano english.txt''')
    print()
    print("Type the same color in your terminal as mentioned above.")
    print()

if ya == "1":
    sinhala();
elif ya == "2":
    english();
else:
    print('''\033[0;31mවැරදි ඇතුලත් කිරීමකි...!''')
    print('''\033[0;31minvalid number...!''')
      