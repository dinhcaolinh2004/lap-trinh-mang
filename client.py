import requests
from PIL import Image
from io import BytesIO

def generate_qr(text):
    url = "http://localhost:5000/generate_qr"
    headers = {"Content-Type": "application/json"}
    data = {"text": text}

    # Gửi yêu cầu POST đến server
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        # Nhận mã QR dưới dạng ảnh PNG
        img = Image.open(BytesIO(response.content))
        img.show()  # Hiển thị mã QR
        # img.save("qr_code.png")  # Lưu mã QR nếu muốn
    else:
        print("Failed to generate QR code:", response.text)

if __name__ == "__main__":
    text = input("Enter text or URL to generate QR: ")
    generate_qr(text)
