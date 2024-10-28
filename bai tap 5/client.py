import socket

def main():
    # Tạo socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Kết nối đến server

    # Gửi số nguyên cho server
    number = input("Nhập một số nguyên: ")
    client_socket.send(number.encode())

    # Nhận tổng từ server
    total = client_socket.recv(1024).decode()
    print(f"Tổng các chữ số của số {number} là: {total}")

    client_socket.close()  # Đóng kết nối

if __name__ == "__main__":
    main()
