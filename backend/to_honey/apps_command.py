import webbrowser
import pywhatkit as kit
import os
import re
import json

#---------------------- Setup Scan Paths ------------------------------------------------------------
folders = [
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    os.path.expanduser("~\\AppData\\Local\\Programs")
]

#---------------------- App Scanner ------------------------------------------------------------------
def scan_apps(dirs):
    apps = {}
    for folder in dirs:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".exe"):
                    name = file.lower().replace(".exe", "")
                    if name not in apps:
                        apps[name] = {
                            "path": os.path.join(root, file),
                            "exe": file
                        }
    return apps

#---------------------- Load or Scan Apps ------------------------------------------------------------
if os.path.exists("apps.json"):
    with open("apps.json", "r") as f:
        apps = json.load(f)
else:
    print("Scanning apps for the first time...")
    apps = scan_apps(folders)
    with open("apps.json", "w") as f:
        json.dump(apps, f)

#---------------------- UWP Apps List ----------------------------------------------------------------
uwp_apps = {
    "camera": "microsoft.windows.camera:",
    "calendar": "start outlookcal:",
    "mail": "microsoft.windowscommunicationsapps:",
    "calculator": "calculator:",
    "photos": "start microsoft.windows.photos:",
    "maps": "bingmaps:",
    "store": "ms-windows-store:"
}

#---------------------- Close UWP App -----------------------------------------------------------------
def close_uwp_app(name):
    # Uses PowerShell through os.system to kill window by title
    os.system(f'powershell "Get-Process | Where-Object {{$_.MainWindowTitle -like \'*{name}*\'}} | Stop-Process -Force"')

#---------------------- Task Handler ------------------------------------------------------------------
def app_task(sentence):
    sentence_upper = sentence.upper()
    sentence_lower = sentence.lower()

    #_________open app___________
    if "OPEN" in sentence_upper:
        # Check for known web pages first
        chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

        # Open Google (excluding Google Sheets)
        if "GOOGLE" in sentence_upper and "SHEETS" not in sentence_upper:
            webbrowser.get("chrome").open("https://www.google.com/")
            return "Opening Google"

        # Open YouTube
        elif "YOUTUBE" in sentence_upper:
            webbrowser.get("chrome").open("https://www.youtube.com/")
            return "Opening YouTube"

        # UWP apps
        for uwp_name in uwp_apps:
            if uwp_name in sentence_lower:
                os.system(f"start {uwp_apps[uwp_name]}")
                return f"Opening {uwp_name.title()} (UWP App)"

        # Regular apps
        app_name = sentence_lower.replace("open", "").strip()
        for name in apps:
            if app_name in name:
                os.startfile(apps[name]["path"])
                return f"Opening {name}"

        # Rescan if not found
        apps.update(scan_apps(folders))
        with open("apps.json", "w") as f:
            json.dump(apps, f)

        for name in apps:
            if app_name in name:
                os.startfile(apps[name]["path"])
                return f"Opening {name}"

        return "Sorry, couldn't find the app."

    #_________close app__________
    elif "CLOSE" in sentence_upper:
        app_name = sentence_lower.replace("close", "").strip()
        if "GOOGLE" in sentence or "YOUTUBE" in sentence :
            os.system("taskkill /im chrome.exe /f")
            return "CLOSING SEARCHED WEB APPLICATION..."

        # Try closing UWP apps by window title
        for uwp_name in uwp_apps:
            if uwp_name in app_name:
                close_uwp_app(uwp_name.title())
                return f"Trying to close {uwp_name.title()} (UWP App)"

        # Try closing regular .exe apps
        for name in apps:
            if app_name in name:
                os.system(f"taskkill /f /im {apps[name]['exe']}")
                return f"Trying to close {name}"

        return "App not found or not running."
    
    #_________search in app______
    elif "SEARCH" in sentence_upper or ("PLAY" in sentence_upper and "IN" in sentence_upper):
        unwanted = r'\bSEARCH\b|\bIN YOUTUBE\b|\bIN GOOGLE\b|\bPLAY\b'
        cleaned_text = re.sub(unwanted, '', sentence, flags=re.IGNORECASE).strip()

        if "IN YOUTUBE" in sentence_upper:
            kit.playonyt(cleaned_text)
            return "Searching in YouTube"

        elif "IN GOOGLE" in sentence_upper:
            kit.search(cleaned_text)
            return "Searching in Google"

        return "Sorry, can't search in that app."

    return "I didn't understand the command."

#---------------------- Main Loop -------------------------------------------------------------------
'''while True:
    user_input = input("Enter sentence: ")
    print(do_task(user_input))'''
