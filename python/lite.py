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
    ['1', '17', '16', '15', '28', '27', '26', '41', '42', '39', '51', '50', '64', '63', '62'],
    ['2', '19', '18', '31', '30', '29', '44', '43', '40', '54', '53', '52', '66', '65'],
    ['3', '21', '20', '34', '33', '32', '47', '46', '45', '56', '55', '68', '67'],
    ['4', '23', '22', '35', '59', '58', '57', '71', '70', '69']
]

keyboard_key = [
    ['esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'back'],
    ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\', '|', 'Del'],
    ['Capslock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', ':', '\'', 'Enter', 'Pup'],
    ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '<', '.', '>', '/', '?', 'Shift', '上'],
    ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Fn', 'Ctrl', '左', '下', '右']
]

root = tk.Tk()
root.title("Keyboard Simulator")
root.wm_attributes("-toolwindow", True)
root.wm_attributes("-alpha", 0.9) 
root.wm_attributes("-topmost", True)

root.geometry("200x35")
root.geometry("+1720+800")

root.overrideredirect(True)

text_box = tk.Text(root, width=20, height=10,font=("Helvetica", 20))
text_box.pack()

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

def read_serial():
    global latest_data
    last_key = ''
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            latest_data = line
            text_box.see(tk.END)
            text_box.delete(1.0, tk.END)

            if keyboard.is_pressed('ctrl'):
                root.wm_attributes("-alpha", 0.9)
                if line[19] == '1':
                    text_box.insert(tk.END, '全部選取\n')
                elif line[34] == '1':
                    text_box.insert(tk.END, '複製\n')
                elif line[33] == '1':
                    text_box.insert(tk.END, '貼上\n')
                elif line[18] == '1':
                    text_box.insert(tk.END, '儲存\n')
                elif line[21] == '1':
                    text_box.insert(tk.END, '還原\n')
                root.wm_attributes("-alpha", 0.8)

            elif keyboard.is_pressed('alt'):
                root.wm_attributes("-alpha", 0.9)
                if line[1] == '1':
                    text_box.insert(tk.END, '切換視窗\n')
            else:
                root.wm_attributes("-alpha", 0)

            

threading.Thread(target=read_serial, daemon=True).start()

root.mainloop()