


from software.pywifi import connection


server=connection('localhost', 12345, "TCP", bufferSize=1024, local=True) # create local server

server.startServerConnection()

