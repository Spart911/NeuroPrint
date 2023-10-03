import json

def write(data, filename):
    data=json.dumps(data)
    data=json.loads(str(data))
    with open(filename, 'w',encoding='utf-8') as openfile:
        json.dump(data, openfile, indent=5)


def read(filename):
    with open(filename, 'r') as openfile:
        data = json.load(openfile)
    return data

filepath = r"Cura 2.7\\resources\\definitions\\fdmprinter.def.json"
json_object=read(filepath)   
initial_flow = json_object['settings']['material']['children']['material_flow']['default_value']

def change_parametr(filepath, Parametr,znach):
    json_object=read(filepath)   
    json_object['settings']['material']['children'][Parametr]['default_value'] = znach
    print(json_object['settings']['material']['children'][Parametr]['default_value'])
    write(json_object, filepath)
    # for app in psutil.process_iter(['pid', 'name']):
    #     sys_app = app.info.get('name').split('.')[0].lower()
    #     if 'powershell' in sys_app or 'cmd' in sys_app:
    #         try:
    #             psutil.Process(app.info.get('pid')).terminate()
    #             break
    #         except:
    #             continue
    # input()