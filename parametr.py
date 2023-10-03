import ctypes
import sys
import psutil
from photo import Dphoto
from remove_bg import Dremove_bg
from image_editor import Dimage_editor
from JSON import change_parametr
from Underextrusion import DEF_Underextrusion
filepath = r"Cura 2.7\resources\definitions\fdmprinter.def.json"  # Путь файла 
P="material_flow" # Параметр
Dremove_bg()
Dimage_editor()

from JSON import initial_flow
min_flow = 80
max_flow = 120




def check_defect(flow):
    Dphoto()
    Dremove_bg()
    Dimage_editor()
    # Здесь должен быть код, который проверяет наличие дефектов недоэкструзии и переэкструзии.
    # Вам нужно вставить свой код проверки дефектов в эту функцию.

    defect_nedoekstruzii = DUnderextrusion()
    print("Наличие дефекта недоэкструзия:",defect_nedoekstruzii)
    print("Впишите наличие дефекта переэкструзия")
    defect_pereekstruzii = int(input())
    print("Наличие дефекта переэкструзия:",defect_pereekstruzii)


    
    # Пример проверки дефекта недоэкструзии:
    if flow < 80:
        defect_nedoekstruzii = 1

    # Пример проверки дефекта переэкструзии:
    if flow > 120:
        defect_pereekstruzii = 1

    return defect_nedoekstruzii, defect_pereekstruzii


def optimize_flow(initial_flow, min_flow, max_flow):
    # print("Поток равен:",initial_flow)
    defect_nedoekstruzii =1
    defect_pereekstruzii =1
    while (defect_nedoekstruzii+defect_pereekstruzii)!=0 :
        print("Поток равен:",initial_flow)
        defect_nedoekstruzii, defect_pereekstruzii = check_defect(initial_flow)
        if (defect_nedoekstruzii+defect_pereekstruzii)==0:
            print("Оптимальное значение потока:", initial_flow)
            change_parametr(filepath, P, initial_flow)
            break
        elif defect_pereekstruzii==1:
            initial_flow=initial_flow-(initial_flow-min_flow)/3  # Наличие дефекта переэкструзия
            # 
            #КОД ПЕЧАТИ(НАРЕЗКА МОДЕЛИ С ИЗМЕНЕННЫМ ПАРАМЕТРОМ И ЭКСПОРТ GCODE)
            from slice import Dslice
            from Gcode_send import Dgcode_send
            # 

        
        elif defect_nedoekstruzii==1:
            initial_flow=initial_flow+(max_flow-initial_flow)/3 # Наличие дефекта недоэкструзия
            # 
            #КОД ПЕЧАТИ(НАРЕЗКА МОДЕЛИ С ИЗМЕНЕННЫМ ПАРАМЕТРОМ И ЭКСПОРТ GCODE)
            from slice import Dslice
            from Gcode_send import Dgcode_send
            # 

    # Если не удалось найти оптимальное значение, возвращаем исходное значение
    
    print("Оптимальное значение потока:",initial_flow)
    change_parametr(filepath, P, initial_flow)
    return 0





if ctypes.windll.shell32.IsUserAnAdmin():
    optimize_flow(initial_flow, min_flow, max_flow)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)