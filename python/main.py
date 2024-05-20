from flask import Flask, jsonify
from threading import Thread
import serial

app = Flask(__name__)

# 配置串口
serial_port = serial.Serial('/dev/cu.usbserial-110', 115200, timeout=1)

def read_serial_data():
    while True:
        # 讀取一行數據
        serial_data = serial_port.readline().decode().strip()
        app.serial_data = serial_data  # 將數據存儲在 Flask 應用的全局變量中

@app.route('/get_serial_data', methods=['GET'])
def get_serial_data():
    return jsonify({'data': app.serial_data})

if __name__ == '__main__':
    # 開始串口讀取線程
    serial_thread = Thread(target=read_serial_data)
    serial_thread.daemon = True
    serial_thread.start()

    # 啟動 Flask 應用
    app.run(debug=True)
