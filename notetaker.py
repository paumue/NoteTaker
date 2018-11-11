
from twilio.rest import Client
import os
from flask import Flask
from twilio.twiml.voice_response import Record, VoiceResponse
import time
from twilio.twiml.messaging_response import MessagingResponse


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
app = Flask(__name__)
client = Client(account_sid, auth_token)




app = Flask(__name__)

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
        rsp.message(str(gettranscription()))
    elif getmessage() == "Print File":
        file = open("data.txt", "w" )
        file.write(str(gettranscription()))
    else:
        rsp.message("If you want to print your notes, write: Print")
    return str(rsp)

if __name__ == "__main__":
    app.run(debug=True)
    print(gettranscription())

