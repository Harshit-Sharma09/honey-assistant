#this deside category of sentance 

import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

def categorize_sentence(sentence):
    sentence = sentence.lower().strip()  # make lowercase and clean spaces
    doc = nlp(sentence)  # let spaCy understand it

    # Rule 1: "tell me about" → Person or Definition
    if "tell about" in sentence:
        if "tell about yourself" in sentence or "tell about you" in sentence:
            return "i am Honey, your personal assistant "
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return "Person Query"
            elif ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART", "EVENT", "LANGUAGE"]:
                return "Definition"
        return "Definition"  # fallback if no entity found

    # Rule 2: Look for person names in sentence
    person_mentioned = any(ent.label_ == "PERSON" for ent in doc.ents)

    # Keyword lists
    question_words = ["who", "what", "how", "where", "why", "when","define"]
    greeting_words = ["hi", "hello", "hey"]
    opinion_words = ["think", "opinion", "feel", "believe"]
    command_verbs = ["turn", "play", "stop", "open", "close", "show", "tell","laugh","cry"]

    # Rule 3: Is it a question?
    if "?" in sentence or any(q in sentence for q in question_words):
        if "who" in sentence or person_mentioned:
            return "Person Query"
        elif "how are you" in sentence:
            return "Personal Question"
        elif "what" in sentence or "define" in sentence:
            return "Definition"
        else:
            return "General Question"

    # Rule 4: Greetings
    if any(greet in sentence for greet in greeting_words):
        return "Greeting"

    # Rule 5: Opinions
    if any(opinion in sentence for opinion in opinion_words):
        return "Opinion"

    # Rule 6: Command
    if any(token.lemma_ in command_verbs for token in doc):
        return "Command"

    # Rule 7: Fallback
    return "Unknown"

# Run in loop until user types 'exit'
while True:
    user_input = input("Enter a sentence (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    category = categorize_sentence(user_input)
    print("→ Category:", category)
