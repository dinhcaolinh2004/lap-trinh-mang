import socket
import threading

def handle_client(client_socket):
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode()
    print(f"Dữ liệu nhận được từ client: {data}")

    # Chuyển chuỗi thành danh sách các số thực và tìm số lớn nhất
    try:
        numbers = list(map(float, data.split()))
        max_number = max(numbers)

        # Gửi lại số lớn nhất cho client
        client_socket.send(str(max_number).encode())
        print(f"Gửi lại số lớn nhất cho client: {max_number}")

    except ValueError:
        # Xử lý khi dữ liệu không hợp lệ
        error_message = "Dữ liệu không hợp lệ! Vui lòng gửi một chuỗi các số thực."
        client_socket.send(error_message.encode())
        print(error_message)

    # Đóng kết nối với client sau khi xử lý xong
    client_socket.close()

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

        # Tạo một luồng mới để xử lý client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
