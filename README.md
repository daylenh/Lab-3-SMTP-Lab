Lab-3-SMTP-Lab
Simple Python SMTP Email Sender (Using Sockets)

This Python script demonstrates how to send an email using raw **SMTP protocol** commands over a socket connection. It manually performs the SMTP handshake and message transfer without using any high-level email libraries.

What It Does
The script connects to a public SMTP server, sends a plain-text email using basic SMTP commands (`HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, etc.), and then closes the connection.

Email Content
The email sent by this script contains:
From: youremail@example.com
To: dayven.lenh@sjsu.edu
Subject: Test Email from Python SMTP

How to Run
1. Requirements
- Python 3.x
- Internet connection (outbound access to port 25)

2. Usage
  1. Clone or download this script.
  2. Update the email addresses in the message and SMTP command lines:
      - `youremail@example.com` → your sender email
      - `dayven.lenh@sjsu.edu` → your recipient email
  3. Run the script:

```bash
python smtp_sender.py
