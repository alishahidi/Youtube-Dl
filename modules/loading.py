from pytube import YouTube
import sys
import subprocess
from termcolor import colored
from modules import access, creator, download, extract, media
import os
import time
import json
import requests
from pydub import AudioSegment
import ffmpeg
from pytube.cli import on_progress

colors = ("yellow", "blue", "red", "magenta", "cyan", "green")

def coloredBold(text, color):
    if color in colors:
        return colored(text, color = color, attrs = ["bold"])
    else:
        raise ValueError("color is not exists colors list")

def banner():
    with open(os.path.realpath("appData/banner"), "r") as banner:
        bannerText = banner.read()
    print(coloredBold("\n" + bannerText + "\n", "red"))


def clear():
    if os.name == "nt":
            os.system("cls")
    elif os.name == "posix":
            os.system("clear")

def loading():
    clear()
    banner()


def inputPlus(inputText):
    print("\n")
    inputValue = input(f"{colored('[', 'red')}{inputText}{colored(']', 'red')}$ ")
    print("\n")
    return inputValue;

def menu_creator(menuItems):
    menuContent = []
    count = 0
    for item in menuItems:
        content = f"{colored('[', 'red')}{count}{colored(']', 'red')} {colored(item, 'green', attrs = ['bold'])}"
        menuContent.append(content)
        count+=1
    return menuContent

def main_menu():
    print("\n")
    menus = menu_creator(["exit","video", "audio", "details"])
    for item in menus:
        print (item)
        time.sleep(.2)
    print("\n")

def check_dir():
    if os.path.exists("temp") is not True:
        os.makedirs("temp")
    if os.path.exists("result") is not True:
        os.makedirs("result")

def check_file():
    if not os.path.exists('message.txt'):
        with open('message.txt', 'w') as file:
            file.write("Type your message here.")

def delete_temp():
    if os.path.exists("temp"):
        filesList = os.listdir("temp")
        numReq = 0
        for file in filesList:
            path = f"temp/{file}"
            if os.path.exists(path):
                os.remove(path)
                numReq = numReq + 1
    else:
        os.makedirs("temp")

def run():
    access.access()
    check_dir()
    check_file()
    main_menu()
    state = inputPlus("Select option")
    if state == "0":
        return False
    argvs = sys.argv
    if len(sys.argv) - 1 == 0:
        link = inputPlus("Enter Link")
    else:
        link = argvs[1]
    loading()
    yt = creator.Youtube(link)

    if state == "1":
        extract.printStreams(yt, "video")
        itag = inputPlus("Enter selected itag")
        stream = creator.Stream(yt, itag)
        print(f"size is: {round(int(stream.filesize) / 1024)}KB")
        accept = inputPlus("Download anyway? (y => yes, n => no)")
        if(accept == False):
            return False
        download.download(yt, stream, "video")
        loading()
        print("\n")
        print("Save to result")
        print("\n")
    
        return True

    elif state == "2":
        extract.printStreams(yt, "audio")
        itag = inputPlus("Enter selected itag")
        stream = creator.Stream(yt, itag)
        print(f"size is: {round(int(stream.filesize) / 1024)}KB")
        accept = inputPlus("Download anyway? (y => yes, n => no)")
        if(accept == False):
            return False
        download.download(yt, stream, "audio")
        loading()
        print("\n")
        print("Save to result")
        print("\n")
        return True
    elif state == "3":
        extract.details(yt)

        