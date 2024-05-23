import tkinter as tk
from flask import Flask, jsonify
import serial
import threading
import keyboard
import time

app = Flask(__name__)

# 全域變數，用於存儲最新讀取的數據
latest_data = ""
ser = None

keyboard_map = [
    ['0', '14', '13', '12', '5', '25', '24', '38', '37', '36', '49', '48', '61', '60'],
    ['1', '17', '16', '15', '28', '27', '26', '41', '40', '39', '51', '50', '64', '63', '62'],
    ['2', '19', '18', '31', '30', '29', '44', '43', '42', '54', '53', '52', '66', '65'],
    ['3', '21', '20', '34', '33', '32', '47', '46', '45', '56', '55', '68', '67'],
    ['4', '23', '22', '35', '59', '58', '57', '71', '70', '69']
]

keyboard_key = [
    ['esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'back'],
    ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\', 'Del'],
    ['Capslock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';:', '\'', 'Enter', 'Pup'],
    ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',<', '.>', '/?', 'Shift', '上'],
    ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Fn', 'Ctrl', '左', '下', '右']
]

keyboard_cap_width = [
  ['1','1','1','1','1','1','1','1','1','1','1','1','1','2.1'],
  ['1.5','1','1','1','1','1','1','1','1','1','1','1','1','1.6','1.2'],
  ['1.7','1','1','1','1','1','1','1','1','1','1','1','2.5','1.2'],
  ['2.1','1','1','1','1','1','1','1','1','1','1','1.8','1'],
  ['1.3','1.3','1.3','6.1','1','1','1','1','1','1']
]

root = tk.Tk()
root.title("Keyboard Simulator")
root.wm_attributes("-toolwindow", True)
root.wm_attributes("-alpha", 0.9)
root.wm_attributes("-topmost", True)

root.geometry("330x102")
root.geometry("+600+0")

root.overrideredirect(True)

canvas = tk.Canvas(root, width=800, height=200)
canvas.pack()

def initialize_serial(port, baudrate):
    global ser
    if ser is None:
        print('Initializing serial port...')
        ser = serial.Serial(port, baudrate, timeout=1)
    else:
        print('Serial port already initialized.')

port = 'COM4'
baudrate = 115200  # 波特率
initialize_serial(port, baudrate)

def show_window():
    root.deiconify()
    root.lift()  # 將視窗提到頂層
    root.wm_attributes("-topmost", True)  # 強制置頂

def hide_window():
    root.withdraw()


keyboard_cap_touch_last = [
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0']
]




key_positions = {}

def init_keyboard():
    key_cap = 20
    row_height = key_cap

    # 初始化時創建所有按鍵的矩形
    for row_idx, row in enumerate(keyboard_map):
        row_cap_widths = list(map(float, keyboard_cap_width[row_idx]))

        for col_idx, key in enumerate(row):
            key_width = row_cap_widths[col_idx]
            x0 = sum(row_cap_widths[:col_idx]) * key_cap
            x1 = x0 + key_width * key_cap
            y0 = row_idx * row_height
            y1 = y0 + row_height
            
            # 取得按鍵對應的狀態
            key_state = keyboard_cap_touch_last[row_idx][col_idx]
            
            if key_state == '1':
                fill_color = "red"
            else:
                fill_color = "gray"
            # 創建矩形並保存其標示符
            rect_id = canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color)
            key_positions[key] = rect_id

            # 繪製按鍵的文字
            canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=keyboard_key[row_idx][col_idx], fill="white")

    return key_positions


init_keyboard()

def update_keyboard_color(data):
    # 更新按鍵的顏色
    for row_idx, row in enumerate(keyboard_map):
        for col_idx, key in enumerate(row):
            key_state = data[int(keyboard_map[row_idx][col_idx])]
            rect_id = key_positions[(key)]
            if key_state == '1':
                canvas.itemconfig(rect_id, fill="red")
            else:
                if key_state == '0':
                    fill_color = "gray"
                else:
                    fill_color = "red"
                canvas.itemconfig(rect_id, fill=fill_color)



def read_serial():
    global latest_data
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            latest_data = line

            print(line)
            if int(line) > 1:
                root.wm_attributes("-alpha", 0.9)
                update_keyboard_color(line)
            else:
                root.wm_attributes("-alpha", 0.0)



threading.Thread(target=read_serial, daemon=True).start()

root.mainloop()
