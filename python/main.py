from flask import Flask, jsonify
import serial
import threading
import keyboard

app = Flask(__name__)

# 全域變數，用於存儲最新讀取的數據
latest_data = ""
ser = None

def initialize_serial(port, baudrate):
    global ser
    if ser is None:
        print('Initializing serial port...')
        ser = serial.Serial(port, baudrate, timeout=1)
    else:
        print('Serial port already initialized.')


def keyboard_map(inp):

    [
        
    ]


def read_from_serial():
    global latest_data
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()


            latest_data = line
            #print(keyboard.is_pressed('ctrl'))        
            if(keyboard.is_pressed('ctrl')):
                if(line[19]=='1'):
                    print('全部選取')



@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({'data': latest_data})

if __name__ == '__main__':
    # 初始化序列埠
    port = 'COM5'  # 將 'COM5' 替換為你的序列埠名稱
    baudrate = 115200  # 波特率
    initialize_serial(port, baudrate)

    # 啟動一個獨立的線程來讀取序列埠數據
    thread = threading.Thread(target=read_from_serial)
    thread.daemon = True
    thread.start()

    # 啟動 Flask 伺服器
    app.run(debug=False, host='0.0.0.0', port=9003)
