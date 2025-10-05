from socket import *

# Message content setup
# This is the actual email content including headers.
msg = (
    "From: youremail@example.com\r\n"
    "To: dayven.lenh@sjsu.edu\r\n"
    "Subject: Test Email from Python SMTP\r\n"
    "\r\n"
    "I love computer networks!"
)

# Mail server information
# Using a free SMTP testing server on port 25 (no authentication).
mailserver = ('smtp.freesmtpservers.com', 25)

# Create socket and connect to mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

# Receive and print initial response from server
recv = clientSocket.recv(1024).decode()
print("Server:", recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print response
heloCommand = 'HELO alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("HELO response:", recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command
mailFrom = 'MAIL FROM:<dayven.lenh@sjsu.edu>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("MAIL FROM response:", recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command
rcptTo = 'RCPT TO:<dayven.lenh@sjsu.edu>\r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("RCPT TO response:", recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("DATA response:", recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message content
clientSocket.send(msg.encode())
clientSocket.send(b'\r\n.\r\n')  

# Receive server response
recv5 = clientSocket.recv(1024).decode()
print("Message response:", recv5)
if recv5[:3] != '250':
    print('250 reply not received after message.')

# Send QUIT command
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print("QUIT response:", recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')

# Close the socket
clientSocket.close()
