from twilio.rest import Client 

account_sid = 'AC624b31ae15da0d25dee9e809a38e4e73'
auth_token = 'c8849af007dc3be78ec6b13e8434bbdc'
client = Client(account_sid, auth_token)

messsage = client.messages.create(
                                from_='+12545406571',
                                body= 'I can\'t believe this work',
                                to='+15857203057'
                            )

print(messsage.sid)