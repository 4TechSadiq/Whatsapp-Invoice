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

#### Configuration
```python
cloudinary.config(
    cloud_name = 'your_cloud_name', 
    api_key = 'your_api_key', 
    api_secret = 'your_api_secret', 
    secure = True
)
```

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
