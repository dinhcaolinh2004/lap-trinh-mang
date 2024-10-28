import socket
def send_stock_symbol(symbol, host='localhost', port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Connecting to {host} on port {port}...")
            s.connect((host, port))
            print(f"Sending stock symbol: {symbol}")
            s.sendall(symbol.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")  
    except ConnectionRefusedError:
        print(f"Error: Unable to connect to the server at {host}:{port}")
    except socket.error as e:
        print(f"Socket error: {e}")
if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    send_stock_symbol(symbol)