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

```python```
def invoice(template, name, logo, date, invoice_number, company_address, invoice_to, amount):

### 2. URL Generator 
This module uploads the generated invoice image to Cloudinary and retrieves the secure URL of the uploaded image.

#### Dependencies
- `cloudinary`
- `os`

