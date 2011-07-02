#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sat Jul  2 02:27:59 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class yabusameFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: yabusameFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.panel_3 = wx.Panel(self.panel_1, -1)
        self.panel_2 = wx.Panel(self.panel_1, -1)
        
        # Menu Bar
        self.yabusameframe_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.yabusameframe_menubar.Append(wxglade_tmp_menu, u"メインメニュー")
        wxglade_tmp_menu = wx.Menu()
        self.yabusameframe_menubar.Append(wxglade_tmp_menu, u"ウィンドウ")
        wxglade_tmp_menu = wx.Menu()
        self.yabusameframe_menubar.Append(wxglade_tmp_menu, u"オプション")
        wxglade_tmp_menu = wx.Menu()
        self.yabusameframe_menubar.Append(wxglade_tmp_menu, u"ヘルプ")
        self.SetMenuBar(self.yabusameframe_menubar)
        # Menu Bar end
        self.yabusameframe_statusbar = self.CreateStatusBar(1, 0)
        
        # Tool Bar
        self.yabusameframe_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.yabusameframe_toolbar)
        self.yabusameframe_toolbar.AddLabelTool(wx.NewId(), u"終了", wx.Bitmap("/media/LOGITEC HD/yabusame2/icons/quit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.shutsubahyoBtn = wx.Button(self.panel_2, -1, u"出馬表")
        self.saishinShutsubahyoBtn = wx.Button(self.panel_2, -1, u"最新出馬表")
        self.seisekiBtn = wx.Button(self.panel_2, -1, u"成績")
        self.jushoSeisekiBtn = wx.Button(self.panel_2, -1, u"重賞成績")
        self.kishuBtn = wx.Button(self.panel_2, -1, u"騎手")
        self.kishuSenrekiBtn = wx.Button(self.panel_2, -1, u"騎手戦歴")
        self.chokyoshiBtn = wx.Button(self.panel_2, -1, u"調教師")
        self.chokyoshiSenrekiBtn = wx.Button(self.panel_2, -1, u"調教師戦歴")
        self.F1Btn = wx.Button(self.panel_3, wx.ID_HELP, "")
        self.F2Btn = wx.Button(self.panel_3, -1, "F2")
        self.F3Btn = wx.Button(self.panel_3, -1, "F3")
        self.F4Btn = wx.Button(self.panel_3, -1, "F4")
        self.F5Btn = wx.Button(self.panel_3, -1, "F5")
        self.F6Btn = wx.Button(self.panel_3, -1, "F6")
        self.F7Btn = wx.Button(self.panel_3, -1, "F7")
        self.F8Btn = wx.Button(self.panel_3, -1, "F8")
        self.F9Btn = wx.Button(self.panel_3, -1, "F9")
        self.F10Btn = wx.Button(self.panel_3, -1, "F10")
        self.F11Btn = wx.Button(self.panel_3, -1, "F11")
        self.F12Btn = wx.Button(self.panel_3, -1, "F12")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.onQuit, id=-1)
        self.Bind(wx.EVT_BUTTON, self.onShutsubahyoBtn, self.shutsubahyoBtn)
        self.Bind(wx.EVT_BUTTON, self.onSaishinShutsubahyoBtn, self.saishinShutsubahyoBtn)
        self.Bind(wx.EVT_BUTTON, self.onSeisekiBtn, self.seisekiBtn)
        self.Bind(wx.EVT_BUTTON, self.onJushoSeisekiBtn, self.jushoSeisekiBtn)
        self.Bind(wx.EVT_BUTTON, self.onKishuBtn, self.kishuBtn)
        self.Bind(wx.EVT_BUTTON, self.onKishuSenrekiBtn, self.kishuSenrekiBtn)
        self.Bind(wx.EVT_BUTTON, self.onChokyoshiBtn, self.chokyoshiBtn)
        self.Bind(wx.EVT_BUTTON, self.onChokyoshiSenrekiBtn, self.chokyoshiSenrekiBtn)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: yabusameFrame.__set_properties
        self.SetTitle(u"流鏑馬")
        self.yabusameframe_statusbar.SetStatusWidths([-1])
        # statusbar fields
        yabusameframe_statusbar_fields = ["yabusameframe_statusbar"]
        for i in range(len(yabusameframe_statusbar_fields)):
            self.yabusameframe_statusbar.SetStatusText(yabusameframe_statusbar_fields[i], i)
        self.yabusameframe_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: yabusameFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(3, 4, 0, 0)
        grid_sizer_1 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_1.Add(self.shutsubahyoBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.saishinShutsubahyoBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.seisekiBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.jushoSeisekiBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.kishuBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.kishuSenrekiBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.chokyoshiBtn, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.chokyoshiSenrekiBtn, 0, wx.EXPAND, 0)
        self.panel_2.SetSizer(grid_sizer_1)
        sizer_2.Add(self.panel_2, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.F1Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F2Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F3Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F4Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F5Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F6Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F7Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F8Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F9Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F10Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F11Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.F12Btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_3.SetSizer(grid_sizer_2)
        sizer_2.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def onQuit(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onQuit' not implemented!"
        event.Skip()

    def onShutsubahyoBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onShutsubahyoBtn' not implemented!"
        event.Skip()

    def onSaishinShutsubahyoBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onSaishinShutsubahyoBtn' not implemented!"
        event.Skip()

    def onSeisekiBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onSeisekiBtn' not implemented!"
        event.Skip()

    def onJushoSeisekiBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onJushoSeisekiBtn' not implemented!"
        event.Skip()

    def onKishuBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onKishuBtn' not implemented!"
        event.Skip()

    def onKishuSenrekiBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onKishuSenrekiBtn' not implemented!"
        event.Skip()

    def onChokyoshiBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onChokyoshiBtn' not implemented!"
        event.Skip()

    def onChokyoshiSenrekiBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        print "Event handler `onChokyoshiSenrekiBtn' not implemented!"
        event.Skip()

# end of class yabusameFrame


class shutsubahyoFileSentakuDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: shutsubahyoFileSentakuDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_6 = wx.Panel(self, -1)
        self.panel_5 = wx.Panel(self, -1)
        self.panel_4 = wx.Panel(self, -1)
        self.yearSelect = wx.ComboBox(self.panel_4, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.nenAndHyoji = wx.StaticText(self.panel_4, -1, u"年 表示順")
        self.hizukeKojunBtn = wx.Button(self.panel_4, -1, u"日付降順↓")
        self.hizukeShojunBtn = wx.Button(self.panel_4, -1, u"日付昇順↑")
        self.shutsubahyoFileSentakuView = wx.ListCtrl(self.panel_5, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.btnOK = wx.Button(self.panel_6, wx.ID_OK, "")
        self.btnCancel = wx.Button(self.panel_6, wx.ID_CANCEL, "")
        self.btnHelp = wx.Button(self.panel_6, wx.ID_HELP, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.onSelectYear, self.yearSelect)
        self.Bind(wx.EVT_BUTTON, self.onHizukeKojunBtn, self.hizukeKojunBtn)
        self.Bind(wx.EVT_BUTTON, self.onHizukeShojunBtn, self.hizukeShojunBtn)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.onListItemDeselected, self.shutsubahyoFileSentakuView)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onListItemSelected, self.shutsubahyoFileSentakuView)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onListItemActivated, self.shutsubahyoFileSentakuView)
        self.Bind(wx.EVT_BUTTON, self.onBtnOK, self.btnOK)
        self.Bind(wx.EVT_BUTTON, self.onBtnCancel, self.btnCancel)
        self.Bind(wx.EVT_BUTTON, self.onBtnHelp, self.btnHelp)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: shutsubahyoFileSentakuDialog.__set_properties
        self.SetTitle(u"出馬表ファイル選択")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: shutsubahyoFileSentakuDialog.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.yearSelect, 0, 0, 0)
        sizer_4.Add(self.nenAndHyoji, 0, 0, 0)
        sizer_4.Add(self.hizukeKojunBtn, 0, 0, 0)
        sizer_4.Add(self.hizukeShojunBtn, 0, 0, 0)
        self.panel_4.SetSizer(sizer_4)
        sizer_3.Add(self.panel_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.shutsubahyoFileSentakuView, 1, wx.EXPAND, 0)
        self.panel_5.SetSizer(sizer_5)
        sizer_3.Add(self.panel_5, 7, wx.EXPAND, 0)
        sizer_6.Add((150, 30), 0, 0, 0)
        sizer_6.Add(self.btnOK, 0, 0, 0)
        sizer_6.Add(self.btnCancel, 0, 0, 0)
        sizer_6.Add(self.btnHelp, 0, 0, 0)
        self.panel_6.SetSizer(sizer_6)
        sizer_3.Add(self.panel_6, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    def onSelectYear(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onSelectYear' not implemented!"
        event.Skip()

    def onHizukeKojunBtn(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onHizukeKojunBtn' not implemented!"
        event.Skip()

    def onHizukeShojunBtn(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onHizukeShojunBtn' not implemented!"
        event.Skip()

    def onListItemDeselected(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemDeselected' not implemented!"
        event.Skip()

    def onListItemSelected(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemSelected' not implemented!"
        event.Skip()

    def onListItemActivated(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemActivated' not implemented!"
        event.Skip()

    def onBtnOK(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnOK' not implemented!"
        event.Skip()

    def onBtnCancel(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnCancel' not implemented!"
        event.Skip()

    def onBtnHelp(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnHelp' not implemented!"
        event.Skip()

# end of class shutsubahyoFileSentakuDialog


class shutsubahyoRaceSentakuDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: shutsubahyoRaceSentakuDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_9 = wx.Panel(self, -1)
        self.panel_8 = wx.Panel(self, -1)
        self.panel_7 = wx.Panel(self, -1)
        self.taKaisaiBtn = wx.Button(self.panel_7, -1, u"他開催")
        self.zenKaisaiBtn = wx.Button(self.panel_7, wx.ID_BACKWARD, "")
        self.jiKaisaiBtn = wx.Button(self.panel_7, wx.ID_FORWARD, "")
        self.kaisaiNichijiLabel = wx.StaticText(self.panel_8, -1, "")
        self.shutsubahyoRaceSentakuView = wx.ListCtrl(self.panel_9, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onShutsubahyoBtn, self.taKaisaiBtn)
        self.Bind(wx.EVT_BUTTON, self.onZenKaisaiBtn, self.zenKaisaiBtn)
        self.Bind(wx.EVT_BUTTON, self.onJiKaisaiBtn, self.jiKaisaiBtn)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.onListItemDeselected, self.shutsubahyoRaceSentakuView)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onListItemSelected, self.shutsubahyoRaceSentakuView)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onListItemActivated, self.shutsubahyoRaceSentakuView)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: shutsubahyoRaceSentakuDialog.__set_properties
        self.SetTitle(u"出馬表レース選択")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: shutsubahyoRaceSentakuDialog.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8.Add(self.taKaisaiBtn, 0, 0, 0)
        sizer_8.Add(self.zenKaisaiBtn, 0, 0, 0)
        sizer_8.Add(self.jiKaisaiBtn, 0, 0, 0)
        self.panel_7.SetSizer(sizer_8)
        sizer_7.Add(self.panel_7, 1, wx.EXPAND, 0)
        sizer_9.Add(self.kaisaiNichijiLabel, 0, 0, 0)
        self.panel_8.SetSizer(sizer_9)
        sizer_7.Add(self.panel_8, 1, wx.EXPAND, 0)
        sizer_10.Add(self.shutsubahyoRaceSentakuView, 1, wx.EXPAND, 0)
        self.panel_9.SetSizer(sizer_10)
        sizer_7.Add(self.panel_9, 7, wx.EXPAND, 0)
        self.SetSizer(sizer_7)
        sizer_7.Fit(self)
        self.Layout()
        # end wxGlade

    def onShutsubahyoBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onShutsubahyoBtn' not implemented!"
        event.Skip()

    def onZenKaisaiBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onZenKaisaiBtn' not implemented!"
        event.Skip()

    def onJiKaisaiBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onJiKaisaiBtn' not implemented!"
        event.Skip()

    def onListItemDeselected(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onListItemDeselected' not implemented!"
        event.Skip()

    def onListItemSelected(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onListItemSelected' not implemented!"
        event.Skip()

    def onListItemActivated(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onListItemActivated' not implemented!"
        event.Skip()

# end of class shutsubahyoRaceSentakuDialog


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    yabusameframe = yabusameFrame(None, -1, "")
    app.SetTopWindow(yabusameframe)
    yabusameframe.Show()
    app.MainLoop()
