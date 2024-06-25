# Invoice Automation System

## Overview

The Invoice Automation System is designed to automate the process of generating, uploading, and sending invoices via WhatsApp. This project utilizes several tools and libraries including PIL for image handling, Cloudinary for image uploading, Twilio for messaging, and docxtpl for document generation and manipulation.

## Project Structure

The project consists of three main modules:

1. **Invoice Manager**: Handles the creation and formatting of invoices.
2. **URL Generator**: Uploads the invoice images to Cloudinary and retrieves the URL.
3. **Message Manager**: Sends the invoice URL to clients via WhatsApp using Twilio.

## Modules

### 1. Invoice Manager

This module generates an invoice in `.docx` format, converts it to `.pdf`, and finally converts the `.pdf` to an image (`.png`).

#### Dependencies

- `docxtpl`
- `docx2pdf`
- `fitz`
- `os`

#### Function

```python
def invoice(template, name, logo, date, invoice_number, company_address, invoice_to, amount):
    # Implementation details here
    pass
```

### 2. URL Generator 
This module uploads the generated invoice image to Cloudinary and retrieves the secure URL of the uploaded image.

#### Dependencies
- `cloudinary`
- `os`

#### Function

```python
def get_url(image):
    # Function implementation here
    pass
```

### 3. Message Manager
This module sends a WhatsApp message to the client with the invoice URL using Twilio.

#### Dependencies
- `twilio`
- `os`

#### Function
```python
def message(url, name, date):
    # Function implementation here
    pass
```

## Configuration
#### Cloudinary Configuration
Set up your Cloudinary credentials in the cloudinary.config:


```python
cloudinary.config(
    cloud_name = 'your_cloud_name', 
    api_key = 'your_api_key', 
    api_secret = 'your_api_secret', 
    secure = True
)
```

#### Twilio Configuration
```python
account_sid = 'your_account_sid' 
auth_token = 'your_auth_token'

from_number = 'whatsapp:your_twilio_number_here' 
to_number = 'whatsapp:client_number_here'
```
## Usage
### Main Script
The main script integrates all modules to generate the invoice, upload it to Cloudinary, and send it via WhatsApp

#### Dependencies

- `invoiceManager`
- `urlGenerator`
- `messageManager`

```python
from invoiceManager import invoice
from urlGen import get_url
from messageManager import message

# Invoice Generation
#Example Data
image = invoice('invoice.docx', 'demo', 'image.png', 'July 8, 2019', '1234', 'company address', 'invoice to address', '1000.00')

# Invoice image to URL
url = get_url(image)

# Send Invoice
message(url=url, name='demo', date='July 8, 2019')
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```
2. **Install the required packages:**
   Ensure you have Python and pip installed. Then, install the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, install them individually:
   ```bash
   pip install pillow cloudinary twilio docxtpl docx2pdf pymupdf
   ```
   Replace https://github.com/your_username/your_repository.git with the actual URL of your Git repository. If you have a requirements.txt file listing all dependencies, use pip install -r requirements.txt to install them in one go. If not, install each package individually as shown.


## Demo Image
## Repository Structure
- **./Whatsapp invoice/Whatsapp.png**: The main demo image file.
