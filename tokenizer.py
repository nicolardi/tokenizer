import os
import sys
from pprint import pprint

text = ""
vocabolario = []
encoded = []

def merge_token(encoded_text, t1, t2):
    if t1 is None or t2 is None:
        return encoded_text

    # join text
    str1 = vocabolario[t1]
    str2 = vocabolario[t2]
    joined = str1+str2
    # create the new token
    vocabolario.append(joined)
    new_token = len(vocabolario)-1
    new_encoded = []

    i = 0
    encoded_text_len = len(encoded_text) -1

    while(i < encoded_text_len):
        current_t = encoded_text[i]
        next_t = encoded_text[i+1]
        if (current_t == t1 and next_t == t2):
            new_encoded.append(new_token)
            i += 2 
        else:
            new_encoded.append(current_t)
            i += 1
    if i < len(encoded_text):
       new_encoded.append(encoded_text[i])
    return new_encoded 

def get_best_mergeable_token(encoded_text):
     stats = {}
     (best_t1, best_t2) =  (None, None)  
     best_matches = 0 

     for i in range(len(encoded_text)-1 ) :
         t1, t2 = (encoded_text[i], encoded_text[i+1])
         joined_token = f"{t1}_{t2}"
         current = stats.get(joined_token, 0)
         stats[joined_token] = current + 1

         if stats[joined_token] > best_matches:
            best_t1 = t1
            best_t2 = t2
            best_matches = stats[joined_token]
     if best_matches < 2:
        return None
     
     return(best_t1,best_t2)

def reduce(encoded):
    t = get_best_mergeable_token(encoded)
    if t is None: 
        return None
    (t1,t2) = t
     
    return merge_token(encoded, t1, t2)

def main():
    global text
    global encoded
    with open("data.txt","r", encoding="utf-8") as f:
        while c := f.read(1):
            if c not in vocabolario:
                vocabolario.append(c)
            text += c
    for i in range(len(text)):
        c = text[i]
        index = vocabolario.index(c)   
        encoded.append(index) 

    while (t := get_best_mergeable_token(encoded)) is not None: 
        (t1,t2) = t
        encoded = merge_token(encoded, t1, t2)
    log("Vocabolario", vocabolario)

def log(title, el):
    print(f">> {title}")
    pprint(el, indent=4, width=60, compact=True)

if __name__ == "__main__":
        main()
        print("Performances");
        print(f"Testo originale: {len(text)}")
        print(f"Testo compresso: {len(encoded)}")
        sys.exit(0)
