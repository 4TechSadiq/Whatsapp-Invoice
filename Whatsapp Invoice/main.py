#Assemble all modules.
from invoiceManager import invoice
from urlGen import get_url
from messageManager import message

#Invoice Generation
image = invoice('invoice.docx', 'demo', 'image.png', 'July 8, 2019', '1234', 'company address', 'invoice to address', '1000.00')

#Invoice image to url
url = get_url(image)
#Send Invoice
message(url=url,name='demo',date="25/06/2024")
