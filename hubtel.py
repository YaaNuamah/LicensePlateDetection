from pyhubtel_sms import SMS, Message

def sms(telephone, message):
	sms = SMS(client_id='#', client_secret='#')
	message = Message(
			sender='COMPSSA',
			content=message,
			recipient=telephone,
			registered_delivery=True,
	)
	sms.send(message)


