import socket

def start_client():
    # Thiết lập socket cho client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Nhập chuỗi các số thực từ người dùng
    numbers_str = input("Nhập chuỗi các số thực, cách nhau bởi dấu cách: ")

    # Gửi chuỗi số cho server
    client_socket.send(numbers_str.encode())

    # Nhận chuỗi số đã sắp xếp từ server
    sorted_numbers = client_socket.recv(1024).decode()
    print(f"Chuỗi số đã sắp xếp từ server: {sorted_numbers}")

    # Đóng kết nối
    client_socket.close()

if __name__ == "__main__":
    start_client()
