import socket

def client_send(a, b):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    
    # Gửi dữ liệu (a và b) đến server
    message = f"{a} {b}"
    client_socket.send(message.encode())
    
    # Nhận kết quả từ server
    result = client_socket.recv(1024).decode()
    print(f"Kết quả nhận từ server: {result}")
    
    client_socket.close()

if __name__ == "__main__":
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b (a < b): "))
    client_send(a, b)
