import cv2
import socket
import pickle
import struct

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor (cambiar la IP)
client_socket.connect(('172.20.10.8', 8485))

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)  # Recibir datos en paquetes
        if not packet: break
        data += packet

    # Extraer el tamaño del frame
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4*1024)

    # Extraer el frame
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Deserializar el frame
    frame = pickle.loads(frame_data)

    # Mostrar el frame en la pantalla
    cv2.imshow('Transmisión de Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
client_socket.close()
cv2.destroyAllWindows()
