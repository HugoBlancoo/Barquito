

import socket
from pydantic import BaseModel, ValidationError
from pydantic.networks import IPvAnyAddress

class ConnectionConfig(BaseModel):
    host: IPvAnyAddress
    port: int

class connection:
    def __init__(self, host, port, sockTYPE="TCP", bufferSize=1024, local=False):
        """
        ## connection macro-class

        #### Needs arguments:

        - host                  Host direction (if it is **localhost** tun `local=True`)
        - port                  Port of the connection (recommended up from 10000)
        - sockTYPE              Socket type, either TCP or UDP
        - bufferSize            The size in bytes of the reception of response buffer
        - local                 Forces local connection for debugging/server type connection binding 
        

        """

        if not local: # local permite forzar una conexión y usar "localhost"
            try:
                ConnectionConfig(host=host, port=port)
            except ValidationError as e:
                print("Validation error: ", e)
                return
        self.host = host
        self.port = port
        self.bufferSize=bufferSize
        self.sockTYPE = socket.SOCK_STREAM if sockTYPE=="TCP" else socket.SOCK_DGRAM
        self.sock=socket.socket(socket.AF_INET, self.sockTYPE)


    def startServerConnection(self):
        try:
            self.sock.bind(('localhost', self.port))
            self.sock.listen(1)
            while True:
                client_conn, client_address = self.sock.accept()
                while True:
                    data = client_conn.recv(self.bufferSize)
                    client_message=data.decode("utf-8")
                    print(f"{client_conn}:{client_address}: {client_message}")
                    
                    # TODO: Command and control 
                    m=input(">RESPONSE?: ")
                    
                    
                    
                    client_conn.send(m.encode("utf-8"))
        except Exception as e:
            print(f"There was an exception: {e}")

    def startClientConnection(self):
        try:
            self.sock.connect((self.host, self.port))
        except Exception as e:
            print(f"There was an exception: {e}")

    def send(self, message):
        self.sock.send(message)
        # Receive data from the server
        response = self.sock.recv(self.bufferSize)
        return response.decode("utf-8")


    def stopConnection(self, seq=None):
        # TODO: seq es una forma de mandar al otro extremo de la comunicacion una despedida

        self.sock.close()





