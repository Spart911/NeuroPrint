import serial
import sys
import ctypes
import time
from elevate import elevate
import os



def sendGCodeToPrinter(gcode_file, serial_port):
    # Установка соединения по USB
    try:
        ser = serial.Serial(serial_port, 115200, timeout=2)
        print("Установлено соединение с портом", serial_port)
        time.sleep(100)
    except serial.SerialException as e:
        print("Ошибка при подключении к порту:", e)
        time.sleep(100)
        return

    # Открытие файла с G-кодом
    try:
        with open(gcode_file, 'r') as file:
            gcode_lines = file.readlines()
    except FileNotFoundError:
        while 1>0:
            print("Файл", gcode_file, "не найден.")
        return

    # Отправка G-кодов на печать
    for line in gcode_lines:
        line = line.strip()
        if line and not line.startswith(';'):  # Пропуск пустых строк и комментариев
            ser.write((line + '\n').encode())
            response = ser.readline().decode().strip()
            print("Отправлено:", line)
            print("Ответ принтера:", response)
            time.sleep(0.1)  # Задержка между отправкой строк G-кода

    ser.close()
    print("Печать завершена.")

# Пример использования
def Dgcode_send():
    gcode_file = "output.gcode"
    serial_port = "COM5"
    # print("ghjghgj")
    elevate()



    if ctypes.windll.shell32.IsUserAnAdmin():
        sendGCodeToPrinter(gcode_file, serial_port)
        # print("ghjghgj")
    else:
        print("НЕТ ПРАВ АДМИНИСТРАТОРА")
        time.sleep(100)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
Dgcode_send()