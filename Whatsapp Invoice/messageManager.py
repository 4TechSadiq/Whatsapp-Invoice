from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os


account_sid = 'AC33217cd1aa85c67a9a27467f2810a292' # account sid
auth_token = '37bc704ec20c50575466ad7a30a5023f' # twilio authentication token

from_number = 'whatsapp:+14155238886' #from number
to_number = 'whatsapp:+918714094884' #user number

client = Client(account_sid,auth_token)


def message(url,name, date): #url of the image, name, date of payment
    """To send the whatsapp message"""

    message = client.messages.create(
        from_= from_number,
        body=f'Dear {name}, your payment is due on {date}. Consider paying it', # message
        to= to_number,
        media_url = url # url of the image or link
    )
    print(message)
    
    # Deleted the invoice image from the root directory after message is delivered
    if message.status == 'queued':
        os.remove(f'{name}.png') 
