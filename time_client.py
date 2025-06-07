import socket


SERVER_HOST = 'localhost'  
SERVER_PORT = 45000
CRLF = '\r\n'

def send_request(sock, message):
    sock.sendall((message + CRLF).encode('utf-8'))
    response = sock.recv(1024)
    return response.decode('utf-8')

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to time server.")

            while True:
                command = input("Command (TIME / QUIT): ").strip().upper()
                if command in ['TIME', 'QUIT']:
                    response = send_request(s, command)
                    print(f"Server: {response.strip()}")

                    if command == 'QUIT':
                        print("Disconnected.")
                        break
                else:
                    print("Invalid command. Use TIME or QUIT.")
    except ConnectionRefusedError:
        print("Unable to connect to server. Is it running?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
