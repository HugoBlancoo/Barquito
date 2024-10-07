import socket

# Esta función es más por legibilidad que por utilidad, podriamos enviar numeros y ya
def obtener_mensaje(opcion):
    if opcion == 1:
        return "camara"
    elif opcion == 2:
        return "imu"
    elif opcion == 3:
        return "ultra"
    elif opcion == 4:
        return "todos"
    else:
        return "MAL"


client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# creo el socket del cliente

server_address = ('localhost',4444)
# indico la direccion y puerto del servidor

while(1):
    print("Seleccione que mensaje enviar \n"
          "\n"
          "1. Obtener datos de camara\n"
          "2. Obtener datos de IMU\n"
          "3. Obtener datos de sensor de ultrasonidos\n"
          "4. Obtener datos de todos los sensores\n"
          "\n")

    eleccion = int(input("$>"))
    # parseo la eleccion del usuario a un entero para poder hacer las comparaciones

    if eleccion not in range (1, 5):
        print("La opcion marcada está fuera del rango (1-4)")
    else:
        mensaje = obtener_mensaje(eleccion)
        # Obtengo el mensaje que voy a enviar

        client_socket.sendto(mensaje.encode(),server_address)
        # Envío el mensaje al server

        respuesta, direccion_respuesta = client_socket.recvfrom(4096)
        # Espero la respuesta del server

        print(f"Datos obtenidos = {respuesta.decode()} enviados por {direccion_respuesta}")
        # Printeo los valores recibidos