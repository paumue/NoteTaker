from twilio.rest import Client
import os
from flask import Flask


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
app = Flask(__name__)
client = Client(account_sid, auth_token)


def gettranscription():
    transcriptions = client.transcriptions.list()
    text = transcriptions[0].transcription_text
    return text


print(gettranscription())