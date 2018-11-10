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

message = client.messages.list()
print(message[1].direction)
print(message[1].body)
iteration = 0
while (message[iteration].direction != "inbound"):
    iteration = iteration + 1
    textmessage = message[iteration]

def makecall():
    call = client.calls.create(
        to= "+447539002953",
        from_= "+442033221378",
        url = "https://b1aa8436.ngrok.io/outcall"
        )



app = Flask(__name__)

#textmessage = "This is an xml constructed call"

@app.route("/outcall", methods=['GET','POST'])
def vocalResponse():
    resp = VoiceResponse()
    resp.say(textmessage)
    return(str(resp))

@app.route("/textin", methods=['GET','POST'])
def gettext():
    makecall()
if __name__ == "__main__":
    app.run()
