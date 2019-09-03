from twilio.rest import Client

def sms(message)

    account_sid = "AC145500ea4d5b5d136c9e7698e70e9ebd"
    auth_token  = "8cfb4d2457d31ffd140b0d027e1d389d"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+233578513659", 
        from_='+12562578652',
        body=message)
    
    if message:
        return 'Message sent!'
    else:
        return 'Message not sent'
    
    



