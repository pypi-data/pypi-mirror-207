from datetime import datetime

import wx
from time import sleep
import pandas as pd

from lightweight_charts import Chart, WxChart


def on_click(x):
    print('yeayea')
    print(x)


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None)
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        self.SetSize((1000, 500))

        self.chart = WxChart(panel, 1000, 500)

        webview = self.chart.get_webview()

        sizer.Add(webview, wx.EXPAND | wx.ALL)
        self.Fit()
        self.Show()


def start_wx_app():
    app = wx.App()
    frame = Frame()

    df = pd.read_csv('../examples/1_setting_data/ohlcv.csv')
    frame.chart.set(df)
    app.MainLoop()


if __name__ == '__main__':

    chart = Chart(width=1000, debug=True)

    df = pd.read_csv('../examples/1_setting_data/ohlcv.csv')

    chart.set(df)
    chart.legend(True)
    chart.subscribe_click(on_click)

    marker = chart.marker(datetime(year=2023, month=2, day=17))

    line = chart.create_line()
    print(line)

    chart.show(block=False)

    while 1:
        sleep(2)
