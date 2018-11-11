from difflib import SequenceMatcher
punctuation = {"exclamation": "!",
               "question": "?",
               "comma": ",",
               "period": ".",
               "apostrophe": "'",
               "colon": ";",
               "semi-colon": ":",
               "open": "(",
               "closed": ")",
               "pound": "£",
               "dollar": "$",
               "asterisk": "*",
               "bullet":"\n -"}

with open("data.txt") as textfile:
    data_file = textfile.read()
    word_set = data_file.split(" ")
for key in punctuation:
    for word in word_set:
        seq = SequenceMatcher(None, key, word)
        if (seq.quick_ratio() > .8):
            word_set[word_set.index(word)] = punctuation.get(key)
newdata = ""
for element in word_set:
    newdata = newdata + element + " "
file = open("finaldata.txt","w")
file.write(newdata)
