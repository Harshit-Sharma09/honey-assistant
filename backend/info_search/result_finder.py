import requests
import wikipedia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

#for error resolve
import nltk 

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")


# Function to search DuckDuckGo using its API
def search_duckduckgo(query):
    
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    
    # Send the request and get the response
    response = requests.get(url)
    
    # Convert the response to JSON (which is a format that's easy to handle)
    data = response.json()
    
    # Extract useful information from the response (like the 'AbstractText')
    ddg_result = data.get('AbstractText', ' ')
    
    # Return the result
    return ddg_result

def search_wikipedia(query):
    print("-----------------------------------")
    try:
        # Get the summary of the topic (first 2 sentences)
        wiki_result = wikipedia.summary(query, sentences=2)
        return wiki_result
    except wikipedia.exceptions.DisambiguationError as e:
        wiki_result=" "
        return f"Your query was too vague. Did you mean: {', '.join(e.options[:4])}?"
    except wikipedia.exceptions.PageError as e:
        wiki_result=" "
        return "I couldn't find anything for that."
    except Exception as e:
        wiki_result=" "
        return "something wrong"

def  summarize_text(text, sentence_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

# Example usage of the function
def find_result(query):
    ddg_result=search_duckduckgo(query)                                   
    wiki_result=search_wikipedia(query)

    combined_result=wiki_result + "\n" + ddg_result                          
    print("combined ------",combined_result)

    if combined_result.strip():
        summary = summarize_text(combined_result, sentence_count=2)
        print(" \n Summary:", summary)
        return summary
    else:
        return"No good content found."
    
# while True:
#     a=input("enter :")
#     a=a.upper()
#     find_result(a)