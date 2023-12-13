from elevate import elevate
import wx
import os
import wx.lib.scrolledpanel as scrolled
class Frame(wx.Frame):
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

            button = [
                "Запустить"
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


if __name__ == '__main__':
    elevate()
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()