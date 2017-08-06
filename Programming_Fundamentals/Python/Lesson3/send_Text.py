import twilio.rest as Rest;

def send_Msg():
    
    # Your Account SID from twilio.com/console
    account_sid = "[Account Id]"
    # Your Auth Token from twilio.com/console
    auth_token  = "[Token]"
    
    client = Rest.Client(account_sid, auth_token)

    message = client.messages.create(
        to="+16412260165", 
        from_="+16416385058",
        body="Hello from Python!")

    print(message.sid);

send_Msg();
