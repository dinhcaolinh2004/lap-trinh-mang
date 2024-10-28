import socket

# Hàm kiểm tra tổng các chữ số của một số có bằng 15 hay không
def sum_of_digits_is_15(number):
    return sum(int(digit) for digit in str(number)) == 15

# Hàm xử lý yêu cầu từ client
def handle_client(client_socket):
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode()
    a, b = map(int, data.split())

    # Tìm các số trong khoảng a -> b có tổng các chữ số bằng 15
    result = [str(num) for num in range(a, b + 1) if sum_of_digits_is_15(num)]
    result_str = " ".join(result) if result else "Không có số nào thỏa mãn"

    # Gửi kết quả lại cho client
    client_socket.send(result_str.encode())
    client_socket.close()

# Hàm khởi động server
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
