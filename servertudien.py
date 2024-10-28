import socket
import requests
from bs4 import BeautifulSoup

def get_definition_from_soha(word):
    url = f"http://tratu.soha.vn/dict/vn_en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Tìm kiếm định nghĩa trong phần nội dung của trang
        definition_section = soup.find("div", {"class": "section-h2"})
        if definition_section:
            return definition_section.text.strip()
        else:
            return "Không tìm thấy định nghĩa cho từ này."
    else:
        return "Không thể kết nối đến từ điển."

def start_server():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"SERVER đang lắng nghe tại {host}:{port}")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Kết nối từ {addr}")
            data = conn.recv(1024).decode()  # Nhận từ từ client
            if data:
                # Tra cứu từ trên tratu.soha.vn
                definition = get_definition_from_soha(data.lower())
                # Gửi định nghĩa về cho client
                conn.sendall(definition.encode())

if __name__ == "__main__":
    start_server()