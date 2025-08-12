import re

from backend.brain.speak import speaking  
from backend.brain.listen import listening
from backend.brain.category_decision import categorize_sentence
from backend.to_honey.personal_Q import personal_ans
from backend.to_honey.apps_command import app_task
from backend.to_honey.greeting import greet
from backend.info_search.result_finder import find_result
from backend.to_honey.act_command import act_task
from backend.to_honey.system_status import system_status


while True:
    try:
        unwanted=r'\bHONEY\b|\bHANI\b'
        text=str(listening())
        sentence=re.sub(unwanted,'',text,flags=re.IGNORECASE)

        category=categorize_sentence(sentence)
        print(category)
        if category=="Personal Question":
            speaking(personal_ans(sentence))

        elif category=="Person Query":
            speaking(find_result(sentence))
        elif category=="Definition":
            speaking(find_result(sentence))
        elif category=="General Question":
            speaking(find_result(sentence))

        elif category=="Command":
            if any(word in sentence for word in ["OPEN", "CLOSE", "SEARCH"]):
                speaking(app_task(sentence))
            elif any(word in sentence for word in ["LAUGH", "CRY", "SING","JOKE"]):
                speaking(act_task(sentence))

        elif category=="Greeting":
            speaking(greet(sentence))

        elif category=="Opinion":
            speaking("instead of sharing an opinion , i can provide some factual information ")
            speaking(find_result(sentence))
        
        elif category=="System Status":
            speaking(system_status(sentence))

        elif sentence.strip() == "EXIT":
            speaking("okay... exiting .. bye ")
            break
        
        else:
            speaking("SORRY..I DONT KNOW ABOT THAT...")
        

    
    except Exception as e:
        print(f"something wrong :{e}")
        speaking("something wrong..")