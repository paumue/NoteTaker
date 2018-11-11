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

app = flask(__name__)

@app.route("/stt",method = ["POST","GET"])
def speachToText():
    resp = VoiceResponse()
    resp.record(timeout="60", transcribe="True")
    return resp()
