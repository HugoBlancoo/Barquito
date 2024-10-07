import socket

def obtener_respuesta(peticion_cliente):
    if peticion_cliente == "camara":
        return "datos_camara"
    elif peticion_cliente == "imu":
        return "datos_imu"
    elif peticion_cliente == "ultra":
        return "datos_ultra"
    elif peticion_cliente == "todos":
        return "datos_todos"
    else:
        return "MAL"


server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('localhost',4444)
server_socket.bind(server_address)
# "Asocio" el socket con dirección y puerto => "Le digo donde escuchar"

while 1:
        print("Esperando por peticiones...\n")
        peticion, direccion_cliente = server_socket.recvfrom(4096)
        # Recibo petición del cliente

        print(f"El cliente solicitó {peticion.decode()}\n")

        respuesta = obtener_respuesta(peticion.decode())
        # Parseo la petición y obtengo respuesta

        server_socket.sendto(respuesta.encode(),direccion_cliente)
        #Envío respuesta
        print("Respuesta enviada\n"
              "--------------\n")
