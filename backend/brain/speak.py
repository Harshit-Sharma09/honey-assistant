#program to speak 
import pyttsx3                                                                            #for speaking 
import datetime
import playsound as ps

engine=pyttsx3.init()

my_bd=datetime.date(2006,5,4)
today_date=datetime.date.today()

if today_date.month==my_bd.month and today_date.day == my_bd.day:
    ps.playsound(r"data\birthday_wish.wav")
    engine.say("Happy Birthday,HARSHIT Sir! May your life’s code always compile successfully, every function return true happiness, and your daily loops be filled with joy and zero bugs. Wishing you a year of smooth-running success and endless smiles")
    
engine.say("welcome, I AM HONEY, how can i help you ")
engine.runAndWait()

def speaking(to_say):
    engine.say(to_say)
    engine.runAndWait()

