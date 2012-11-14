# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACd4f90f2571958e3ac3f697dabb9b45dc"
auth_token = "24cdd8f1cae6c984a78839b7faa15c6d"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(to="+12014463242", from_="+12015469573",
                                               body="Hello there!")
