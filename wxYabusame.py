#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx
import MVCtemp as mvc
from wx.lib.pubsub import Publisher as pub
from datetime import date as dt
import make_kaisai_nengappi_list_sql as mknls
import shutsubahyo_file_sentaku_asc_sql as sfsas
import shutsubahyo_file_sentaku_desc_sql as sfsds
import shutsubahyo_race_sentaku_sql as srss

# Model
class Model:
    def __init__(self):
        self.thisYear = str(dt.today().year)
        self.flag = "d"
        self.yearList = [str(i) for i in range(dt.today().year, 1985, -1)]
        self.kaisaiNengappiDict = dict(mknls.makeKaisaiNengappiList().getAllRows())
        self.kaisaiNengappiKeyList = self.kaisaiNengappiDict.keys()
        self.kaisaiNengappiKeyList.sort()
        self.kaisaiNengappiKeyList.reverse()

    def changeYear(self, value):
        self.thisYear = self.yearList[value]
        self.showShutsubahyoFileSentaku()
        
    def showShutsubahyoFileSentaku(self):
        yearCode = self.thisYear + "%"
        if self.flag == "d":
            pub.sendMessage("LIST CTRL SHOWN", self.shutsubahyoFileSentakuDesc(yearCode))
        elif self.flag == "a":
            pub.sendMessage("LIST CTRL SHOWN", self.shutsubahyoFileSentakuAsc(yearCode))
        else:
            pass

    def shutsubahyoFileSentakuDesc(self, value):
        _data = sfsds.shutsubahyoFileSentakuDescSQL()
        return _data.getAllRows(year = value)
        
    def shutsubahyoFileSentakuAsc(self, value):
        _data = sfsas.shutsubahyoFileSentakuAscSQL()
        return _data.getAllRows(year = value)

    def shutsubahyoRaceSentaku(self, value):
        _data = srss.shutsubahyoRaceSentakuSQL()
        pub.sendMessage("LIST CTRL SHOWN", _data.getAllRows(code = value))

# View
class View(mvc.yabusameFrame):
    def __init__(self, *args, **kwds):
        mvc.yabusameFrame.__init__(self, *args, **kwds)

class ShutsubahyoFileSentakuDlg(mvc.shutsubahyoFileSentakuDialog):
    def __init__(self, *args, **kwds):
        mvc.shutsubahyoFileSentakuDialog.__init__(self, *args, **kwds)

    def SetListCtrl(self, data):
        cs = ['コード', '日付↓', 'R数', 'D']
        [self.shutsubahyoFileSentakuView.InsertColumn(cs.index(heading), heading) for heading in cs]
        [self.shutsubahyoFileSentakuView.Append(i) for i in data]
        [self.shutsubahyoFileSentakuView.SetColumnWidth(i, wx.LIST_AUTOSIZE) for i in range (len(cs))]

    def RemoveListCtrl(self):
        self.shutsubahyoFileSentakuView.ClearAll()

class ShutsubahyoRaceSentakuDlg(mvc.shutsubahyoRaceSentakuDialog):
    def __init__(self, *args, **kwds):
        mvc.shutsubahyoRaceSentakuDialog.__init__(self, *args, **kwds)

    def SetListCtrl(self, data):
        cs = ['コード', '場所', 'R', 'レース', 'コース', '頭', '発走']
        [self.shutsubahyoRaceSentakuView.InsertColumn(cs.index(heading), heading) for heading in cs]
        [self.shutsubahyoRaceSentakuView.Append(i) for i in data]
        [self.shutsubahyoRaceSentakuView.SetColumnWidth(i, wx.LIST_AUTOSIZE) for i in range (len(cs))]

    def RemoveListCtrl(self):
        self.shutsubahyoRaceSentakuView.ClearAll()

# Controller
class Controller:
    def __init__(self, app):
        self.model = Model()

        #set up the frame which displays the current Model value
        self.view = View(None)
        self.view.Bind(wx.EVT_TOOL, self.onQuit, id=-1)
        view_dic = { self.onShutsubahyoBtn : self.view.shutsubahyoBtn, \
                     self.onSaishinShutsubahyoBtn : self.view.saishinShutsubahyoBtn, \
                     self.onSeisekiBtn : self.view.seisekiBtn, \
                     self.onJushoSeisekiBtn : self.view.jushoSeisekiBtn, \
                     self.onKishuBtn : self.view.kishuBtn, \
                     self.onKishuSenrekiBtn : self.view.kishuSenrekiBtn, \
                     self.onChokyoshiBtn : self.view.chokyoshiBtn, \
                     self.onChokyoshiSenrekiBtn : self.view.chokyoshiSenrekiBtn }
        [self.view.Bind(wx.EVT_BUTTON, k, view_dic[k]) for k in view_dic.keys()]
        
        #set up the first dialog which allows the user to modify the Model's value
        # self.shutsubahyo_file_sentaku_dlg = ShutsubahyoFileSentakuDlg(None)
        # self.shutsubahyo_file_sentaku_dlg.SetListCtrl( \
        #     self.model.shutsubahyoFileSentakuDesc( \
        #         self.model.thisYear + "%"))
        # [self.shutsubahyo_file_sentaku_dlg.yearSelect.Append(item) for item in self.model.yearList]
        # self.shutsubahyo_file_sentaku_dlg.yearSelect.SetValue(self.model.thisYear)
        # self.shutsubahyo_file_sentaku_dlg.SetListCtrl(self.model.showShutsubahyoFileSentaku())
        self.shutsubahyo_file_sentaku_dlg.Bind( \
            wx.EVT_COMBOBOX, \
            self.onSelectYear, \
            self.shutsubahyo_file_sentaku_dlg.yearSelect)
        self.shutsubahyo_file_sentaku_dlg.Bind( \
            wx.EVT_LIST_ITEM_DESELECTED, \
            self.onListItemDeselected, \
            self.shutsubahyo_file_sentaku_dlg.shutsubahyoFileSentakuView)
        self.shutsubahyo_file_sentaku_dlg.Bind( \
            wx.EVT_LIST_ITEM_SELECTED, \
            self.onListItemSelected, \
            self.shutsubahyo_file_sentaku_dlg.shutsubahyoFileSentakuView)
        self.shutsubahyo_file_sentaku_dlg.Bind( \
            wx.EVT_LIST_ITEM_ACTIVATED, \
            self.onListItemActivated, \
            self.shutsubahyo_file_sentaku_dlg.shutsubahyoFileSentakuView)
        shutsubahyo_file_sentaku_btn_dic = \
                                         { self.onHizukeKojunBtn: \
                                           self.shutsubahyo_file_sentaku_dlg.hizukeKojunBtn, \
                                           self.onHizukeShojunBtn: \
                                           self.shutsubahyo_file_sentaku_dlg.hizukeShojunBtn, \
                                           self.onBtnOK: \
                                           self.shutsubahyo_file_sentaku_dlg.btnOK, \
                                           self.onBtnCancel: \
                                           self.shutsubahyo_file_sentaku_dlg.btnCancel, \
                                           self.onBtnHelp: \
                                           self.shutsubahyo_file_sentaku_dlg.btnHelp }
        [self.shutsubahyo_file_sentaku_dlg.Bind( \
            wx.EVT_BUTTON, \
            k, \
            shutsubahyo_file_sentaku_btn_dic[k]) \
         for k in shutsubahyo_file_sentaku_btn_dic.keys()]
        # pub.subscribe(self.ShowListCtrl, "LIST CTRL SHOWN")

        #set up the second dialog which allows the user to modify the Model's value
        self.shutsubahyo_race_sentaku_dlg = ShutsubahyoRaceSentakuDlg(None)
        self.shutsubahyo_race_sentaku_btn_dic = \
                                              { self.onShutsubahyoBtn : \
                                                self.shutsubahyo_race_sentaku_dlg.taKaisaiBtn, \
                                                self.onZenKaisaiBtn : \
                                                self.shutsubahyo_race_sentaku_dlg.zenKaisaiBtn, \
                                                self.onJiKaisaiBtn : \
                                                self.shutsubahyo_race_sentaku_dlg.jiKaisaiBtn }
        [self.shutsubahyo_race_sentaku_dlg.Bind( \
            wx.EVT_BUTTON, \
            k, \
            self.shutsubahyo_race_sentaku_btn_dic[k])
         for k in self.shutsubahyo_race_sentaku_btn_dic.keys()]
        
        pub.subscribe(self.ShowListCtrl, "LIST CTRL SHOWN")
        
        self.view.Show()

    def makeShutsubahyoFileSentakuDlg(self):
        #set up the first dialog which allows the user to modify the Model's value
        dlg = ShutsubahyoFileSentakuDlg(None)
        dlg.SetListCtrl( \
            self.model.shutsubahyoFileSentakuDesc( \
                self.model.thisYear + "%"))
        [dlg.yearSelect.Append(item) for item in self.model.yearList]
        dlg.yearSelect.SetValue(self.model.thisYear)
        
    def onQuit(self, event): # wxGlade: yabusameFrame.<event_handler>
        # print "Event handler `onQuit' not implemented!"
        # event.Skip()
        self.shutsubahyo_race_sentaku_dlg.Destroy()
        self.shutsubahyo_file_sentaku_dlg.Destroy()
        self.view.Close()

    def onShutsubahyoBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        # print "Event handler `onShutsubahyoBtn' not implemented!"
        # event.Skip()
        self.shutsubahyo_file_sentaku_dlg.ShowModal()
        # self.shutsubahyo_file_sentaku_dlg.Destroy()

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

    def onSelectYear(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onSelectYear' not implemented!"
        # event.Skip()
        item = event.GetSelection()
        self.model.changeYear(item)

    def onHizukeKojunBtn(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onHizukeKojunBtn' not implemented!"
        # event.Skip()
        self.model.flag = "d"
        self.model.showShutsubahyoFileSentaku()

    def onHizukeShojunBtn(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onHizureShojunBtn' not implemented!"
        # event.Skip()
        self.model.flag = "a"
        self.model.showShutsubahyoFileSentaku()

    def ShowListCtrl(self, message):
        # print "Event handler `OederChanged' not implemented!"
        # event.Skip()
        if self.shutsubahyo_file_sentaku_dlg:
            self.shutsubahyo_file_sentaku_dlg.RemoveListCtrl()
            self.shutsubahyo_file_sentaku_dlg.SetListCtrl(message.data)
        elif self.shutsubahyo_race_sentaku_dlg:
            self.shutsubahyo_race_sentaku_dlg.RemoveListCtrl()
            self.shutsubahyo_race_sentaku_dlg.SetListCtrl(message.data)
        else:
            print "Event handler `OederChanged' not implemented!"
            event.Skip()
    
    def onListItemDeselected(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemDeselected' not implemented!"
        event.Skip()

    def onListItemSelected(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemSelected' not implemented!"
        event.Skip()

    def onListItemActivated(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onListItemActivated' not implemented!"
        # event.Skip()
        self.currentItem = event.m_itemIndex
        if self.shutsubahyo_file_sentaku_dlg:
            self.model.shutsubahyoRaceSentaku( \
                self.shutsubahyo_file_sentaku_dlg.shutsubahyoFileSentakuView.GetItemText( \
                    self.currentItem)[:8] + '%')
            self.shutsubahyo_file_sentaku_dlg.Destroy()
        self.shutsubahyo_race_sentaku_dlg.ShowModal()
        # self.shutsubahyo_race_sentaku_dlg.Destroy()

    def onBtnOK(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnOK' not implemented!"
        event.Skip()

    def onBtnCancel(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onBtnCancel' not implemented!"
        # event.Skip()
        self.shutsubahyo_file_sentaku_dlg.Close()

    def onBtnHelp(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnHelp' not implemented!"
        event.Skip()

    def onZenKaisaiBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onZenKaisaiBtn' not implemented!"
        event.Skip()

    def onJiKaisaiBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        print "Event handler `onJiKaisaiBtn' not implemented!"
        event.Skip()


if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()
