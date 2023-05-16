from twilio.rest import Client 

account_sid = 'AC624b31ae15da0d25dee9e809a38e4e73'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

messsage = client.messages.create(
                                from_='+12545406571',
                                body= 'HELLLOOOOO',
                                to='+15856905070'
                            )

print(messsage.sid)