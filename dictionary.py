import json
from difflib import get_close_matches
from tkinter import Y

data=json.load(open("dictionary.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif(len(get_close_matches(w,data.keys())>0)):
        yn=(input("Did you mean %s instead? Press Y if yes, press N if no." % get_close_matches(w,data.keys())[0]))
        yn=yn.lower()
        if yn =="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return("The word does not exist.")
        else:
            return("We didnt understand.")
    else:
        return("the word does not exist")

word=input("Enter a word to search:")
output=translate(word)
if type (output) == list:
    for item in output:
        print(item)
else:
    print(output)
input("press ENTER to exit")