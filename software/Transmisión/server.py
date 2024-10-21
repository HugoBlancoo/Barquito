import cv2
import socket
import pickle
import struct

# Inicializar la captura desde la webcam
cap = cv2.VideoCapture(0)

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y puerto
server_socket.bind(('0.0.0.0', 8485))  # IP y puerto donde escuchará el servidor
server_socket.listen(5)  # Número máximo de conexiones en cola
print("Esperando conexiones...")

conn, addr = server_socket.accept()  # Aceptar una conexión
print(f"Conectado con: {addr}")

try:
    # Comenzar a capturar frames
    while cap.isOpened():
        ret, frame = cap.read()  # Leer los frames de la webcam
        if ret:
            # Redimensionar el frame a 640x480
            frame = cv2.resize(frame, (640, 480))

            # Serializar el frame utilizando pickle
            data = pickle.dumps(frame)

            # Empaquetar el tamaño del frame antes de enviarlo
            message_size = struct.pack("Q", len(data))

            # Enviar el tamaño del frame y luego el frame
            conn.sendall(message_size + data)
        else:
            break
finally:
    # Liberar recursos
    cap.release()
    conn.close()
    server_socket.close()

    print("Grabación finalizada y guardada en 'output.avi'")
