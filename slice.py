import os
import subprocess
import sys
import math
import datetime
import re
import ctypes
import psutil

def run_as_admin(command, params=None):
    # Получаем handle текущего процесса
    hinstance = ctypes.windll.shell32.ShellExecuteW(None, "runas", command, params, None, 1)
    if hinstance <= 32:
        return False
    return True

def __slice(model_file, definition_files, settings=None):
    if settings is None:
        settings = {}

    cura_engine_path = "Cura 2.7\\CuraEngine.exe"  # Замените на ваш путь
    cmd = [cura_engine_path, "slice"]

    for definition in definition_files:
        cmd.append("-j")
        cmd.append(definition)

    for key, val in settings.items():
        cmd.append("-s")
        cmd.append(str(key)+"="+str(val))

    cmd.append("-l")
    cmd.append(model_file)

    cmd.append("-v")

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err_output = process.communicate()
        process.wait()
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Command:", e.cmd)
        print("Output:", e.output)
        print("Return code:", e.returncode)
        return None, None

    return output, err_output

def slicer(model_file, definition_files, settings=None, verbose=False):
    output, err_output = __slice(model_file, definition_files, settings)
    output_filename = "output.gcode"  # Имя файла для сохранения Gcode

    if verbose:
        print(err_output)

    # Записываем Gcode в файл
    with open(output_filename, "wb") as gcode_file:
        gcode_file.write(output)

# Вызов функции и сохранение Gcode в файл



def estimate(model_file, definition_files, settings=None, verbose=False):
    output, err_output = __slice(model_file, definition_files, settings)

    if verbose:
        print(err_output)

    record = False

    output_lines = err_output.decode("utf8").split(os.linesep)
    header = []

    for line in output_lines:
        if line.startswith("Gcode header after slicing:"):
            record = True

        if record:
            header.append(line)

    if verbose:
        print("Header:", header)

    time = -1
    filament = -1

    for line in header:
        if line.startswith(";TIME:"):
            time = int(line.split(":")[-1])
        if line.startswith(";Filament used: "):
            filament = float(line.split(" ")[-1].replace("m",""))

    return {"time": time, "filament": filament}
def Dslice():
    model_file = "xyzCalibration_cube.stl"
    definition_files = ["Cura 2.7\\resources\\definitions\\fdmprinter.def.json","Cura 2.7\\resources\\definitions\\fdmextruder.def.json"]
    settings = None
    slicer(model_file, definition_files, settings)
    print(f"Gcode сохранен ")