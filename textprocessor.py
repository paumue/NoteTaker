punctuation = {"punctuate exclamation mark": "!",
               "punctuate question mark": "?",
               "punctuate comma": ",",
               "punctuate apostrophe": "'",
               "punctuate colon": ";",
               "punctuate semi colon": ":",
               "punctuate open parenthesis": "(",
               "punctuate closed parenthesis": ")",
               "punctuate open brackets": "[",
               "punctuate close brackets": "]",
               "punctuate pound sign": "£",
               "punctuate dollar sign": "$",
               "punctuate asterisk": "*"}

F=open("data.txt", "w").read()
for key in punctuation:
    while(F.find(key) != -1):
        x = key.replage(key, punctuation[key])