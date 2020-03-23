from twilio.rest import Client

# Account SID from twilio.com/console
account_sid = ""

# Auth Token from twilio.com/console
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
        to="",
        from_="",
        body="Hello from Python!")

print(message.sid)
