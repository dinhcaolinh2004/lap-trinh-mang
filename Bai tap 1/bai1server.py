import socket

def handle_client(client_socket):
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode()
    # Tách hai số nguyên a và b
    a, b = map(int, data.split())
    
    # Tính tổng của a và b
    result = a + b
    
    # Gửi kết quả lại cho client
    client_socket.send(str(result).encode())
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    
    print("Server đang chạy và chờ kết nối...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Kết nối từ: {addr}")
        
        # Xử lý yêu cầu từ client
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
