from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
import time


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
app = Flask(__name__)
client = Client(account_sid, auth_token)

def call():


    client.calls.create(
                        url='http://57c2c0f3.ngrok.io/answer',
                        to='+447444072109',
                        from_='+441233800083')

def getmessage():
    messages = client.messages.list()

    for i in range(0, len(client.messages.list())):
        if messages[i].direction == "inbound":
            return (messages[i].body)
    return "Error"



@app.route("/msg", methods=['GET', 'POST'])
def message_answer():
    rsp = MessagingResponse()
    rsp.message("Calling you")
    call()
    return str(rsp)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    response = getmessage()
    time.sleep(3)
    resp = VoiceResponse()
    resp.say(response, voice='alice')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


