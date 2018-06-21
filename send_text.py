from twilio.rest import TwilioRestClient

account_sid = "AC5ce6613b3852eec8f3872416a93d3cd7" # Your Account SID from www.twilio.com/console
auth_token  = "741f40a25d51321412e0be69e1d33497"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="I'm leaving, meet at longyang square",
    to=   "+15618739065",    # Replace with your phone number
    from_="+12018624387") # Replace with your Twilio number

print(message.sid)
