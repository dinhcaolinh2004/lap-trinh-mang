import socket

def start_server():
    # Thiết lập socket cho server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server đang lắng nghe tại cổng 12345...")

    while True:
        # Chấp nhận kết nối từ client
        client_socket, addr = server_socket.accept()
        print(f"Kết nối từ {addr}")

        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode()
        print(f"Dữ liệu nhận được từ client: {data}")

        # Chuyển đổi chuỗi thành danh sách các số thực
        try:
            numbers = list(map(float, data.split()))
            numbers.sort()  # Sắp xếp danh sách số theo thứ tự tăng dần

            # Gửi lại chuỗi số đã sắp xếp cho client
            sorted_numbers_str = ' '.join(map(str, numbers))
            client_socket.send(sorted_numbers_str.encode())
            print(f"Gửi lại chuỗi số đã sắp xếp cho client: {sorted_numbers_str}")

        except ValueError:
            # Xử lý khi dữ liệu không hợp lệ
            error_message = "Dữ liệu không hợp lệ! Vui lòng gửi một chuỗi các số thực."
            client_socket.send(error_message.encode())
            print(error_message)

        # Đóng kết nối với client sau khi xử lý xong
        client_socket.close()

if __name__ == "__main__":
    start_server()
