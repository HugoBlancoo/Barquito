



from pywifi import connection


client=connection('localhost', 12345, "TCP", bufferSize=1024, local=True) # force local client

client.startClientConnection()


message = b'Hello, server!'
print("Rsponse from the server: ", client.send(message))

