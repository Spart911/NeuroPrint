import wx
import os
import wx.lib.scrolledpanel as scrolled
# from elevate import elevate



class PhotoFrame(wx.Frame):
    def __init__(self, parent, img_path):
        super(PhotoFrame, self).__init__(parent, title='Photo', size=(800, 600))

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(0, 0, 0))  # Set background color to black

        border_size = 10  # Border size in pixels
        border_color = wx.Colour(0, 0, 0)  # Border color (black)

        img = wx.Image(img_path, wx.BITMAP_TYPE_ANY)
        img = img.Scale(img.GetWidth() + 2 * border_size, img.GetHeight() + 2 * border_size)

        img_ctrl = wx.StaticBitmap(panel, -1, wx.Bitmap(img))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(img_ctrl, 1, wx.EXPAND | wx.ALL, border_size)  # Add border size to maintain spacing
        panel.SetSizer(hbox)
        self.Centre()
        self.Show()

        # Draw a border around the image
        dc = wx.ClientDC(img_ctrl)
        dc.SetPen(wx.Pen(border_color, border_size * 2))
        dc.SetBrush(wx.Brush(border_color, wx.TRANSPARENT))
        dc.DrawRectangle(0, 0, img_ctrl.GetSize().width, img_ctrl.GetSize().height)





class SliceModelFrame(wx.Frame):
    def __init__(self, parent, gcode_content):
        super(SliceModelFrame, self).__init__(parent, title='Sliced Model', size=(800, 600))

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        panel = scrolled.ScrolledPanel(self, -1)
        panel.SetBackgroundColour(wx.Colour(0, 0, 0))

        text = wx.TextCtrl(panel, -1, gcode_content, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, size=(780, 580), pos=(10, 10))
        text.SetForegroundColour(wx.Colour(255, 255, 255))
        text.SetBackgroundColour(wx.Colour(0, 0, 0))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(text, 1, wx.EXPAND | wx.ALL, 0)

        panel.SetSizer(vbox)
        panel.SetupScrolling(scroll_x=False)

        self.Centre()
        self.Show()


class JSON_Frame(wx.Frame):
    def __init__(self, parent, gcode_content):
        super(JSON_Frame, self).__init__(parent, title='JSON Printing Options', size=(800, 600))

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        panel = scrolled.ScrolledPanel(self, -1)
        panel.SetBackgroundColour(wx.Colour(0, 0, 0))

        text = wx.TextCtrl(panel, -1, gcode_content, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER, size=(780, 580), pos=(10, 10))
        text.SetForegroundColour(wx.Colour(255, 255, 255))
        text.SetBackgroundColour(wx.Colour(0, 0, 0))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(text, 1, wx.EXPAND | wx.ALL, 0)

        panel.SetSizer(vbox)
        panel.SetupScrolling(scroll_x=False)

        self.Centre()
        self.Show()



class AnalysisFrame(wx.Frame):
    def __init__(self, parent, defect, confidence_score):
        super(AnalysisFrame, self).__init__(parent, title='Результат анализа', size=(400, 150))

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)


        font_path = os.path.join('fonts', 'Rostov.ttf')

        # Load the custom font
        custom_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        custom_font.SetFaceName("Rostov")



        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(0, 0, 0))

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Создаем панели с фоновым цветом
        defect_panel = wx.Panel(panel)
        defect_panel.SetBackgroundColour(wx.Colour(0, 0, 0))
        accuracy_panel = wx.Panel(panel)
        accuracy_panel.SetBackgroundColour(wx.Colour(0, 0, 0))

        # Текст "ДЕФЕКТ"
        defect_label = wx.StaticText(defect_panel, -1, "ДЕФЕКТ:")
        defect_label.SetForegroundColour(wx.Colour(255, 255, 255))

        # Текст "КОЭФФИЦИЕНТ ТОЧНОСТИ"
        accuracy_label = wx.StaticText(accuracy_panel, -1, "КОЭФФИЦИЕНТ ТОЧНОСТИ:")
        accuracy_label.SetForegroundColour(wx.Colour(255, 255, 255))

        # Значение "ДЕФЕКТ"
        defect_value = wx.StaticText(defect_panel, -1, defect)
        defect_value.SetForegroundColour(wx.Colour(255, 255, 255))

        # Значение "КОЭФФИЦИЕНТ ТОЧНОСТИ"
        accuracy_value = wx.StaticText(accuracy_panel, -1, str(confidence_score))
        accuracy_value.SetForegroundColour(wx.Colour(255, 255, 255))

        # Располагаем элементы внутри панелей
        defect_sizer = wx.BoxSizer(wx.HORIZONTAL)
        defect_sizer.Add(defect_label, 0, wx.EXPAND | wx.ALL, 5)
        defect_sizer.Add(defect_value, 0, wx.EXPAND | wx.ALL, 5)
        defect_panel.SetSizer(defect_sizer)

        accuracy_sizer = wx.BoxSizer(wx.HORIZONTAL)
        accuracy_sizer.Add(accuracy_label, 0, wx.EXPAND | wx.ALL, 5)
        accuracy_sizer.Add(accuracy_value, 0, wx.EXPAND | wx.ALL, 5)
        accuracy_panel.SetSizer(accuracy_sizer)

        # Располагаем панели в общем вертикальном бокссайзере
        vbox.Add(defect_panel, 0, wx.EXPAND)
        vbox.Add(accuracy_panel, 0, wx.EXPAND)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()




class ParameterInputDialog(wx.Dialog):
    def __init__(self, parent, title, custom_font):
        super(ParameterInputDialog, self).__init__(parent, title=title, size=(300, 150))

        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.param_label = wx.StaticText(self.panel, -1, "ВВЕДИТЕ ПАРАМЕТР:")
        self.param_label.SetFont(custom_font)
        self.param_label.SetForegroundColour(wx.WHITE)  # Set text color to white
        self.param_label.SetBackgroundColour(wx.BLACK)  # Set background color to black
        vbox.Add(self.param_label, 0, wx.EXPAND | wx.ALL, 10)

        self.param_text = wx.TextCtrl(self.panel, -1, "", style=wx.TE_PROCESS_ENTER)
        self.param_text.SetFont(custom_font)
        self.param_text.SetForegroundColour(wx.WHITE)  # Set text color to white
        self.param_text.SetBackgroundColour(wx.BLACK)  # Set background color to black
        vbox.Add(self.param_text, 0, wx.EXPAND | wx.ALL, 10)

        self.ok_button = wx.Button(self.panel, wx.ID_OK, "OK")
        self.ok_button.SetForegroundColour(wx.WHITE)  # Set text color to white
        self.ok_button.SetBackgroundColour(wx.BLACK)  # Set background color to black
        vbox.Add(self.ok_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.panel.SetBackgroundColour(wx.BLACK)  # Set panel background color to black
        self.panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.OnOK, id=wx.ID_OK)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnter, self.param_text)
        self.param_value = None

    def OnOK(self, event):
        self.param_value = self.param_text.GetValue()
        event.Skip()
        self.Destroy()

    def OnEnter(self, event):
        self.param_value = self.param_text.GetValue()
        self.EndModal(wx.ID_OK)
        self.Destroy()





class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.custom_font = self.load_custom_font()
        self.InitUI()
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap('icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

    def load_custom_font(self):
        font_path = os.path.join('fonts', 'Rostov.ttf')
        custom_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        custom_font.SetFaceName("Rostov")
        custom_font.SetPointSize(14)
        return custom_font

    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.SetBackgroundColour(wx.Colour(0, 0, 0))  # Black background

        font_path = os.path.join('fonts', 'Rostov.ttf')

        # Load the custom font
        custom_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        custom_font.SetFaceName("Rostov")

        buttons = [
            "Сделать фото",
            "Удалить фон",
            "Обработать фото",
            "Нарезать модель",
            "Провести анализ фото на наличие дефекта",
            "Изменить параметр",
            "Запустить печать"
        ]

        vbox = wx.BoxSizer(wx.VERTICAL)

        for label in buttons:
            button = wx.Button(pnl, label=label, size=(-1, 40))
            button.SetForegroundColour(wx.Colour(255, 255, 255))
            button.SetBackgroundColour(wx.Colour(52, 73, 94))  # Dark blue buttons
            button.SetFont(custom_font)  # Apply custom font
            vbox.Add(button, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
            vbox.AddSpacer(5)

            self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)

        pnl.SetSizer(vbox)

        self.SetMinSize((450, 420))  # Adjusted minimum size for the window
        self.SetTitle('NeuroPrint')
        self.Centre()

    def OnButtonClick(self, event):
        label = event.GetEventObject().GetLabel()
        if label == "Сделать фото":
            from photo import Dphoto  # Подставьте правильный импорт для функции Dphoto
            # Вызываем Dphoto только при нажатии кнопки "Сделать фото"
            Dphoto(camera_index=0)
            Dphoto(camera_index=1)
            # Отображаем окно с фото после вызова Dphoto
            img_path = os.path.join('img_test', 'photo1.png')
            photo_frame = PhotoFrame(self, img_path)


        if label == "Удалить фон":
            #from remove_bg import Dremove_bg  # Подставьте правильный импорт для функции Dphoto
            # Вызываем Dphoto только при нажатии кнопки "Сделать фото"
            #Dremove_bg()
            # Отображаем окно с фото после вызова Dphoto
            img_path = os.path.join('CHB', 'photo1.png.png')
            photo_frame = PhotoFrame(self, img_path)


        if label == "Обработать фото":
            from image_editor import Dimage_editor  # Подставьте правильный импорт для функции Dphoto
            Dimage_editor()
            img_path = os.path.join('res', 'photo1.png.png')
            photo_frame = PhotoFrame(self, img_path)


        if label == "Нарезать модель":
            from slice import Dslice
            Dslice()
            gcode_file_path = 'output.gcode'
            
            try:
                with open(gcode_file_path, 'r', encoding='utf-8') as gcode_file:
                    gcode_content = gcode_file.read()

            # Создаем новое окно для отображения содержимого G-code
                    slice_model_frame = SliceModelFrame(self, gcode_content)
            except IOError:
                wx.MessageBox('Не удалось прочитать файл G-code.', 'Ошибка', wx.OK | wx.ICON_ERROR)

        if label == "Провести анализ фото на наличие дефекта":
            from Underextrusion import DEF_Underextrusion
            class_name = (DEF_Underextrusion())[0]
            confidence_score = (DEF_Underextrusion())[1]
            # Учитываем различные префиксы в class_name
            if class_name.startswith("T "):
                defect = class_name[2:]
            else:
                defect = class_name

            analysis_frame = AnalysisFrame(self, defect, confidence_score)

        if label == "Изменить параметр":
            filepath = r"Cura 2.7\\resources\\definitions\\fdmprinter.def.json"
            dialog = ParameterInputDialog(self, "Изменение параметра", self.custom_font)
            dialog.CenterOnScreen()
            result = dialog.ShowModal()
            if result == wx.ID_OK:
                znac_parametr = dialog.param_value
                print("The entered parameter is:", znac_parametr)  # You can replace this with your desired functionality
            dialog.Destroy()
            from JSON import change_parametr
            change_parametr(filepath,"material_flow",znac_parametr)

            try:
                with open(filepath, 'r', encoding='utf-8') as json_file:
                    json_content = json_file.read()

                    # Создаем новое окно для отображения содержимого json
                    json_frame = JSON_Frame(self, json_content)
            except IOError:
                wx.MessageBox('Не удалось прочитать файл G-code.', 'Ошибка', wx.OK | wx.ICON_ERROR)

        if label == "Запустить печать":
            from Gcode_send import Dgcode_send
            Dgcode_send()


        

if __name__ == '__main__':
    # elevate()
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
