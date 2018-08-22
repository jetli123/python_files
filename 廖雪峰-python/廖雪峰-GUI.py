# -*- coding: utf-8 -*-
# 创建并显示一个框架
import wx


def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()
app = wx.App()
# 创建标签和标题
# 增加标题大小
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
bkg = wx.Panel(win)
# 创建按钮
loadButton = wx.Button(win, label='Open',
                       pos=(225, 5), size=(80, 25))
loadButton.Bind(wx.EVT_BUTTON, load)
saveButton = wx.Button(win, label='Save',
                       pos=(315, 5), size=(80, 25))
saveButton.Bind(wx.EVT_BUTTON, save)
# 增加文本框,
filename = wx.TextCtrl(bkg, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(bkg, pos=(5, 35), size=(390, 260),
                       style=wx.HSCROLL)   # wx.HSCROLL 水平滚动条

# 使用尺寸器
hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT , border=5)
bkg.SetSizer(vbox)
# 在框架上增加按钮
# 只要使用 win 做为父进程参数实例化 wx.Button 即可
"""btn = wx.Button(win) # 增加按钮"""
win.Show()
app.MainLoop()
