import socket
import threading
import time
import logging
from datetime import datetime

PORT = 45000
HOST = '0.0.0.0'
BUFFER_SIZE = 1024
CRLF = b'\r\n'

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.running = True

    def run(self):
        logging.warning(f"Handling client {self.address}")
        buffer = b''
        try:
            while self.running:
                data = self.connection.recv(BUFFER_SIZE)
                if not data:
                    break
                buffer += data

                while CRLF in buffer:
                    line, buffer = buffer.split(CRLF, 1)
                    line_str = line.decode('utf-8').strip()

                    if line_str.upper() == 'TIME':
                        current_time = time.strftime("%d %m %Y %H:%M:%S")
                        response = f"{current_time}\r\n"
                        self.connection.sendall(response.encode('utf-8'))

                    elif line_str.upper() == 'QUIT':
                        self.running = False
                        break

        except Exception as e:
            logging.warning(f"Error with {self.address}: {e}")
        finally:
            logging.warning(f"Closing connection {self.address}")
            self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.the_clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        logging.warning(f"Time server started on port {PORT}...")

        try:
            while True:
                client_conn, client_addr = self.server_socket.accept()
                client_thread = ProcessTheClient(client_conn, client_addr)
                client_thread.start()
                self.the_clients.append(client_thread)
        except KeyboardInterrupt:
            logging.warning("Server shutting down...")
        finally:
            self.server_socket.close()


def main():
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(message)s')
    server = Server()
    server.start()
    server.join()

if __name__ == "__main__":
    main()
