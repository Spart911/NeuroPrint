import ctypes
import sys
import psutil


# ЭКСПОРТ ПАРАМЕТРА
filepath = r"C:\Program Files\Cura 2.7\resources\definitions\fdmprinter.def.json"  # Путь файла 
P="material_flow" # Параметр

from JSON import initial_flow

import parametr




# from JSON import change_parametr


# a=777 #Значение параметра

# def main():
#     change_parametr(filepath, P, a)


# if ctypes.windll.shell32.IsUserAnAdmin():
#     main()
# else:
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)