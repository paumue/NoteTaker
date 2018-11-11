import os
from twilio.rest import Client
from flask import Flask
import xml.etree.ElementTree as ET
import requests
from twilio.rest import Client,TwilioRestClient

# Initializing environmental  variables

#acount_sid= os.environ["twilio_account_sid"]
#auth_token = os.environ["twilio_auth_token"]
# Your Account SID from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]


# Initializing Twilio and Flask variables

client = Client(account_sid, auth_token)

def getMessages():
    textmessage = ""
    #Retrieves messages
    message = client.messages.list()
    iteration = 0
    #Retrieves body of most recent inbound message
    while (message[iteration].direction != "inbound"):
        iteration = iteration + 1
    if (message[iteration].direction == "inbound"):
        textmessage = message[iteration].body
    return textmessage

def makecall():
    call = client.calls.create(
        to= os.environ["phone_number"],
        from_= os.environ["twilio number"],
        url = "https://b1aa8436.ngrok.io/outcall"
    )


app = Flask(__name__)

#textmessage = "This is an xml constructed call"

@app.route("/outcall", methods=['GET','POST'])
def vocalResponse():
    callsays = getMessages()
    resp = VoiceResponse()
    resp.say(callsays)
    return str(resp)
    #makecall1()

@app.route("/textin", methods=['GET','POST'])
def gettext():
    makecall()

@app.route("/voicerec", methods=['GET','POST'])
def voicerecord():
    resp = VoiceResponse()
    resp.record(timeout="10", transcribe="True")
    return resp()


if __name__ == "__main__":
    app.run()

