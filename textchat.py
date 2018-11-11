#Python version 3
from distutils.core import setup
import requests
import os
from twilio.rest import Client,TwilioRestClient
from flask import Flask
import lxml
import xml.etree.ElementTree as ET
from twilio.twiml.voice_response import VoiceResponse

# Initializing environmental  variables

account_sid= os.environ["twilio_account_sid"]
auth_token = os.environ["twilio_auth_token"]

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
        to= "+447539002953",
        from_= "+442033221378",
        url = "https://b1aa8436.ngrok.io/outcall"
        )
def makecall1():
    call = client.calls.create(
        to= "+447539002953",
        from_= "+442033221378",
        url = "https://b1aa8436.ngrok.io/voicerec"
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
