import socket

host = "google.com"
port = 80
request = bytes("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host), 'utf8')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send(request)

response = client.recv(4096)
print(response)
