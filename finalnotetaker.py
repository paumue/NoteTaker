from twilio.rest import Client
import os
from flask import Flask
from twilio.twiml.voice_response import Record, VoiceResponse
import time
from twilio.twiml.messaging_response import MessagingResponse
from pbwrap import Pastebin as pb
from difflib import SequenceMatcher

pastebin = pb("223aa89e0b48c8e3547ac1087ba5df6d")
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
app = Flask(__name__)
client = Client(account_sid, auth_token)

app = Flask(__name__)

def formatting():
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
                   "bullet": "\n -"}
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

    pburl = pastebin.create_paste(api_paste_code=newdata, api_paste_private=0, api_paste_name=None, api_paste_expire_date=None, api_paste_format=None)

    with open('out.txt', "w") as f:
        f.write(newdata)
    return pburl

def formattingstring(transcription):
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
                   "bullet": "\n -"}

    word_set = transcription.split(" ")
    for key in punctuation:
        for word in word_set:
            seq = SequenceMatcher(None, key, word)
            if (seq.quick_ratio() > .8):
                word_set[word_set.index(word)] = punctuation.get(key)
    newdata = ""
    for element in word_set:
        newdata = newdata + element + " "
    return newdata


def gettranscription():
    transcriptions = client.transcriptions.list()
    text = transcriptions[0].transcription_text
    return text


def getmessage():
    messages = client.messages.list()

    for i in range(0, len(client.messages.list())):
        if messages[i].direction == "inbound":
            return (messages[i].body)
    return "Error"


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("I am the notetaker I will help you to take notes. Tell me what I should write down", voice='alice')
    resp.record(timeout="60", transcribe="True")
    return str(resp)


@app.route("/msg", methods=['GET', 'POST'])
def message_answer():
    rsp = MessagingResponse()
    if getmessage() == "Print":
        time.sleep(5)
        rsp.message(str((formattingstring(gettranscription()))))
    elif getmessage() == "Print File":
        file = open("data.txt", "w")
        file.write(str(gettranscription()))
        file.close()
        url = formatting()


        rsp.message("Check it out: " + url)


    else:
        rsp.message("If you want to print your notes, write: Print")
    return str(rsp)


if __name__ == "__main__":
    app.run(debug=True)