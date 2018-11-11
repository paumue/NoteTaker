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
               "punctuate asterisk": "*",
               "punctuate bullet":"\n -"}

with open("data.txt") as textfile:
    data_file = textfile.read()
    print(data_file)
for key in punctuation:
    data_file = data_file.replace(key, punctuation[key])
f = open("data.txt","w")
f.write(data_file)
