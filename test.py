def formattingstring(transcription):
    punctuation = {"exclamation mark": "!",
                   "question mark": "?",
                   "comma": ",",
                   "apostrophe": "'",
                   "colon": ";",
                   "semi colon": ":",
                   "open parenthesis": "(",
                   "closed parenthesis": ")",
                   "open brackets": "[",
                   "close brackets": "]",
                   "pound sign": "£",
                   "dollar sign": "$",
                   "asterisk": "*",
                   "bullet": "\n -"}
    for key in punctuation:
        print(key)
        transcription = transcription.replace(key, punctuation[key])
    return transcription


print(formattingstring("Can't trade summation mug punctuate questions punctuate comma punctuated apostrophe function column puncturing them a column punctured. Punctured clothes BRACA punctured po"))
