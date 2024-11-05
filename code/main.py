import os
from twilio.rest import Client

os.environ['TWILIO_ACCOUNT_SID'] = ''
os.environ['TWILIO_AUTH_TOKEN'] = ''

client = Client()
call = client.calls.create(
    from_='+1716621-2424',
    to='+886917780800',
    url='https://handler.twilio.com/twiml/EH62539d87bcf85d6e932d305ffd417d6a'
)

print(call.sid)