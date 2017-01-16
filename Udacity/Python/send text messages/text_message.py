from twilio.rest import TwilioRestClient

account_sid = "AC4dfd66caf13f03100778369bc70aeeb9" # Your Account SID from www.twilio.com/console
auth_token  = "6cc37ba561847f961e057f03052287c8"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Luke, I am your father",
    to="+12142645015",    # Replace with your phone number
    from_="14697893092") # Replace with your Twilio number

print(message.sid)
