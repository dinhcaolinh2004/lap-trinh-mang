import socket
import requests
import threading
API_KEY = "your_alpha_vantage_api_key"
def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        data = response.json()
        if "Time Series (1min)" in data:
            time_series = data["Time Series (1min)"]
            latest_time = list(time_series.keys())[0]
            stock_price = time_series[latest_time]["1. open"]
            return f"Giá hiện tại của {symbol} là {stock_price}"
        else:
            return "Không tìm thấy thông tin cho mã chứng khoán này."
    except requests.exceptions.HTTPError as http_err:
        return f"Lỗi HTTP: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Không thể kết nối tới API. Kiểm tra kết nối mạng."
    except requests.exceptions.Timeout:
        return "Yêu cầu API bị hết thời gian chờ."
    except requests.exceptions.RequestException as e:
        return f"Lỗi khác: {str(e)}"
def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            stock_symbol = data.decode()
            print(f"Nhận mã chứng khoán: {stock_symbol}")
            stock_price = get_stock_price(stock_symbol)
            conn.sendall(stock_price.encode())
def start_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server đang chạy trên {host}:{port}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
if __name__ == "__main__":
    start_server()