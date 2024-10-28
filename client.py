import socket

def start_client():
    host = '127.0.0.1'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        num1 = input("Nhập số thứ nhất: ")
        num2 = input("Nhập số thứ hai: ")
        client_socket.sendall(f"{num1} {num2}".encode())
        result = client_socket.recv(1024).decode()
        print(f"Tổng là: {result}")
        
if __name__ == "__main__":
    start_client()
