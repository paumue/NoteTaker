#give us number
# we send them a sms
# wait for response
# parse the response to a voice message
# voice message to call
# keep call open

import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447444072109",
    from_="+441233800083",
    body="Hello from Python!")
print(message.sid)
