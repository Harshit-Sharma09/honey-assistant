import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

def categorize_sentence(sentence):
    sentence = sentence.strip()
    doc = nlp(sentence)
    print("final sentance-", sentence )
    
 # Keyword lists
    question_words = ["WHO", "WHAT", "HOW", "WHERE", "WHY", "WHEN","DEFINE"]
    greeting_words = ["HI", "HELLO", "HEY","GOOD MORNING","GOODMORNING","GOOD AFTERNOON","GOODAFTERNOON","GOOD EVENING","GOODEVENING","GOOD NIGHT","GOODNIGHT"]
    opinion_words = ["THINK", "OPINION", "FEEL", "BELIVE","SUGGEST"]
    command_verbs = [ "PLAY", "STOP","SEARCH","OPEN", "CLOSE", "WEATHER","LAUGH","CRY","SING","JOKE"]
    system_status = ["BATTERY", "MEMORY" ,"STORAGE" , " RAM ","SYSTEM STATUS"]

    person_mentioned = any(ent.label_ == "PERSON" for ent in doc.ents)

    
    # Command
    if any(token.lemma_.upper() in command_verbs for token in doc):
        return "Command"
    
    # Opinions
    if any(opinion in sentence for opinion in opinion_words):
        return "Opinion"
    
    #yourself command :
    if " YOU" in sentence or " YOUR" in sentence:
        return "Personal Question"

    
    
    if "TELL" in sentence:                       #"TELL ME ABOUT"
        if "TELL ME ABOUT YOURSELF" in sentence or "TELL ME ABOUT YOU" in sentence:
            return "Personal Question"
        
        if any(status in sentence for status in system_status):
            return "System Status"
        
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return "Person Query"
            elif ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART", "EVENT", "LANGUAGE"]:
                return "Definition"
        return "Definition"  # fallback if no entity found


    if any(q in sentence for q in question_words):
        if "WHO" in sentence or person_mentioned:
            return "Person Query"
        elif "HOW ARE YOU" in sentence or "HOW R U" in sentence:
            return "Personal Question"
        elif "WHAT" in sentence or "DEFINE" in sentence:
            return "Definition"
        else:
            return "General Question"
    
   

     # Greetings
    if any(greet in sentence for greet in greeting_words):
        return "Greeting"
    
    #SYSTEM STATUS 
    if any(status in sentence for status in system_status):
        return "System Status"
    
# while True:
#     a=str(input("enter sentence :"))
#     print(str(categorize_sentence(a)))