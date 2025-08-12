from datetime import datetime
def greet(sentance):
    if "HELLO" in sentance or"HI" in sentance or"HEY" in sentance :
        return "hello    ..  i am honey ,    how can i help you "
    
    elif "GOOD MORNING"in sentance or  "GOOD AFTERNOON"in sentance or  "GOOD EVENING"in sentance or  "GOOD NIGHT"in sentance :
        current_hour=datetime.now().hour

        if 4<=current_hour <12:
            return "GOOD MORNING"
        elif 12<= current_hour <17:
            return "GOOD AFTERNOON"
        elif 17<= current_hour < 22:
            return "GOOD EVENING"
        else:
            return "GOOD NIGHT"
        
    else:
        return"nothing"
