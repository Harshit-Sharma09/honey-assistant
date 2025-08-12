import random
import pyjokes
import pygame
import os

# Initialize the mixer
pygame.mixer.init()

# List of laugh sounds
laughs = [
    r"data\laugh1.wav",
    r"data\laugh2.wav",
    r"data\laugh3.wav"
]

# Path to the sing sound
sing = r"data\HumeAI_voice-preview_Twinkle twinkle for honey_.wav"

def play_sound(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until the sound finishes
            pygame.time.Clock().tick(10)
    else:
        print(f"File not found: {file_path}")


def act_task(task):
    #print("this is for testing ----------------", laughs)

    if "LAUGH" in task:
        l = random.choice(laughs)
        print(f"Playing: {l}")
        play_sound(l)

    elif "CRY" in task:
        return "Honey, never cry..."

    elif "SING" in task:
        print(f"Playing: {sing}")
        play_sound(sing)

    elif "JOKE" in task:
        joke = pyjokes.get_joke(language='en', category='all')
        return joke


#Test example: Use a simple input loop if you want

# while True:
#     a = str(input("Enter sentence: "))
#     print(act_task(a))





























'''from playsound import playsound
import pyjokes
import random




laughs=["data\\laugh1.wav",
        "data\\laugh2.wav",
        "data\\laugh3.wav"]

sing="data\\HumeAI_voice-preview_Twinkle twinkle for honey_.wav"
def act_task(task):
    print("this isfor testing ----------------", laughs)

    if "LAUGH" in task:
        l=random.choice(laughs)
        print(l)
        playsound(l)

    elif "CRY" in task:
        return "Honey, never cry..."
    
    elif "SING" in task :
        playsound(sing)

    elif "JOKE" in task:
        joke=pyjokes.get_joke(language='en',category='all')
        return joke

# while True:
#      a=str(input("enter sentence :"))
#      act_task(a)
    
    '''