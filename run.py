# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python

from flask import Flask, request, redirect
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    # be careful: resp = Response() not working in python3, use MessagingResponse() instead
    resp = MessagingResponse()

    # Add a message
    resp.message("Hey Jay")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)