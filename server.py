from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get("text")
    if not data:
        return {"error": "No text provided"}, 400

    # Tạo mã QR
    qr = qrcode.make(data)
    
    # Lưu mã QR vào máy dưới dạng file PNG
    qr.save("qr_code.png")
    print("Mã QR đã được lưu với tên 'qr_code.png'")

    # Lưu ảnh QR vào bộ nhớ tạm để gửi cho client
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    # Trả về ảnh QR dưới dạng ảnh PNG cho client
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
