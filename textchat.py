
import os
from twilio.rest import Client
from flask import Flask
import lxml.etree as E
import lxml.builder

# Initializing environmental  variables

#acount_sid= os.environ["twilio_account_sid"]
#auth_token = os.environ["twilio_auth_token"]
# Your Account SID from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]
# Initializing Twilio and Flask variables

client = Client(account_sid, auth_token)

app = Flask(__name__)


#Get text

#set text to textmessage

#Generate XML from text

def xml_gen(txtmsg):
    #TWXL categories
    RESPONSE = E.response
    #TWXL Fields
    SAY = E.say
    #Generate TWXL
    pagetwxl = RESPONSE(
                        SAY(txtmsg, voice = "Alice")
                        )
    return pagetwxl

#xmlfile = open(responsetwxl.xml,"w")
#xml_gen(textmessage).write(xmlfile)

@app.route("/xml", methods=['GET','POST'])
def xmlpage():
    return xml_gen("Hello there")

if __name__ == "__main__":
    app.run(debug=True)