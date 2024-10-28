import socket

def start_client():
    host = '192.168.1.100'  # Địa chỉ IP của máy Server
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        # Nhập từ từ người dùng
        word = input("Nhập một từ để tra từ điển: ")
        # Gửi từ đó đến server
        client_socket.sendall(word.encode())
        # Nhận định nghĩa từ server
        response = client_socket.recv(1024).decode()
        print(f"Định nghĩa của '{word}' là: {response}")
    
if __name__ == "__main__":
    start_client()