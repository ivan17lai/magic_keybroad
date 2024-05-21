from flask import Flask, jsonify
import serial
import threading
import keyboard

app = Flask(__name__)

# 全域變數，用於存儲最新讀取的數據
latest_data = ""
ser = None


keyboard_map = [
  ['0','14','13','12','5','25','24','38','37','36','49','48','61','60'],
  ['1','17','16','15','28','27','26','41','42','39','51','50','64','63','62'],
  ['2','19','18','31','30','29','44','43','40','54','53','52','66','65'],
  ['3','21','20','34','33','32','47','46','45','56','55','68','67'],
  ['4','23','22','35','59','58','57','71','70','69']
];

keyboard_key = [
  ['esc','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','back'],
  ['Tab','Q','W','E','R','T','Y','U','I','O','P','[{',']}','\\|','Del'],
  ['Capslock','A','S','D','F','G','H','J','K','L',';:','\'','Enter','Pup'],
  ['Shift','Z','X','C','V','B','N','M',',<','.>','\/？','Shift','上'],
  ['Ctrl','Win','Alt','Space','Alt','Fn','Ctrl','左','下','右']
];


def initialize_serial(port, baudrate):
    global ser
    if ser is None:
        print('Initializing serial port...')
        ser = serial.Serial(port, baudrate, timeout=1)
    else:
        print('Serial port already initialized.')


port = '/dev/cu.usbserial-10'
baudrate = 115200  # 波特率
initialize_serial(port, baudrate)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()


        latest_data = line
        # i = 0
        # for c in line:
        #     print(i,end=':')
        #     print(c,end='/')
        #     i = i+1

        # print()  

        if(line[4]=='1'):
            if(line[19]=='1'):
                print('全部選取')
            elif(line[34]=='1'):
                print('複製')
            elif(line[33]=='1'):
                print('貼上')
            elif(line[18]=='1'):
                print('儲存')
            elif(line[21]=='1'):
                print('還原')
   