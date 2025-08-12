import webbrowser
import pywhatkit as kit
import os
import re
import re._parser 

import json
#---------------------------------------------------
#finding app for opening app
def scan_apps(dirs):
    apps = {}
    for folder in dirs:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".exe"):
                    name = file.lower().replace(".exe", "")
                    if name not in apps:
                        apps[name] = os.path.join(root, file)
    return apps

# Load apps or scan if first time
if os.path.exists("apps.json"):
    with open("apps.json", "r") as f:
        apps = json.load(f)
else:
    #speak("Scanning apps. Please wait a moment...")
    folders = [
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        os.path.expanduser("~\\AppData\\Local\\Programs")
    ]
    apps = scan_apps(folders)
    with open("apps.json", "w") as f:
        json.dump(apps, f)
#-----------------------------------------------------

def do_task(sentence):

    if "OPEN" in sentence :
        #by chrome 
        chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        if "GOOGLE" in sentence:
            webbrowser.get("chrome").open("https://www.google.com/")
            return "yes...opening google"
        elif "YOUTUBE" in sentence:
            webbrowser.get("chrome").open("https://www.YOUTUBE.com/")
            return "yes...opening youtube"
        
        #by system apps 
        else:
            app_name = sentence.replace("OPEN", "").strip().lower()
            print("AAYA")
            found=False 
            for name in apps:
                if  app_name in name:
                    os.startfile(apps[name])
                    found=True
                    to_say=f"Opening {name}"
                    break
                
                if not found:
                    
                    apps = scan_apps(folders)
                    with open("apps.json", "w") as f:
                        json.dump(apps, f)

                    for name in apps:
                        if app_name in name:
                            os.startfile(apps[name]["path"])
                            to_say=(f"Opening {name}")
                            found = True
                            break

                    if not found:
                         to_say=(" couldn't find the app.")
            return to_say
                     
            #return "sorry , don't know this app "

    
    elif "CLOSE" in sentence :
        if "GOOGLE" in sentence or "YOUTUBE" in sentence :
            os.system("taskkill /im chrome.exe /f")

        else:
            app_name = sentence.replace("close", "").strip().lower()
            found = False
            for name in apps:
                if app_name in name:
                    exe_name = apps[name]["exe"]
                    os.system(f"taskkill /f /im {exe_name}")
                    to_say=(f"Trying to close {name}")
                    found = True
                    break
                if not found:
                    to_say=("App not found or not running.")
            return to_say

    elif "SEARCH" in sentence or ("PLAY" in sentence and "IN" in sentence):
        unwanted=r'\bSEARCH\b|\bIN YOUTUBE\b|\bIN GOOGLE\b|\bPLAY\b'
        if "IN YOUTUBE" in sentence:
            cleaned_text=re.sub(unwanted,'',sentence,flags=re.IGNORECASE)
            print(cleaned_text)
            kit.playonyt(cleaned_text)
            return "SEARCHING IN YOUTUBE"
        elif "IN GOOGLE" in sentence:
            cleaned_text=re.sub(unwanted,'',sentence,flags=re.IGNORECASE)
            print(cleaned_text)
            kit.search(cleaned_text)
            return "SEARCHING IN GOOGLE"
        else:
            return "sorry , can't open in this app "
        
while True:
    a=input("enter sentance :")
    print(do_task(a))

        
