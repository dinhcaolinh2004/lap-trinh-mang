import socket

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    # Tạo socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Gán địa chỉ và cổng
    server_socket.listen(1)  # Lắng nghe kết nối từ client
    print("Server đang lắng nghe...")

    while True:
        # Chấp nhận kết nối từ client
        client_socket, addr = server_socket.accept()
        print(f"Kết nối từ {addr}")

        try:
            # Nhận số nguyên từ client
            data = client_socket.recv(1024).decode()
            if data:
                number = int(data)
                total = sum_of_digits(number)
                # Gửi tổng về cho client
                client_socket.send(str(total).encode())
        except ValueError:
            print("Đã xảy ra lỗi khi chuyển đổi dữ liệu.")
        finally:
            client_socket.close()  # Đóng kết nối với client

if __name__ == "__main__":
    main()
