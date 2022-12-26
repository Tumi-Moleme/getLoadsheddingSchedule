from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)
from_whatsapp_number = "YOUR_TWILIO_PHONE_NUMBER"
to_whatsapp_number = "RECIPIENT_PHONE_NUMBER"


message = client.messages.create(
    body="There is a powercut in your area. Please be prepared.",
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(message.sid)
