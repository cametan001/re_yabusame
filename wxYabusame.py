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
                
        self.dlgDict = {}
        
        pub.subscribe(self.ShowListCtrl, "LIST CTRL SHOWN")
        
        self.view.Show()

    def makeShutsubahyoFileSentakuDlg(self):
        #set up the first dialog which allows the user to modify the Model's value
        self.dlgDict[u"出馬表ファイル選択"] = ShutsubahyoFileSentakuDlg(None)
        self.dlgDict[u"出馬表ファイル選択"].SetListCtrl( \
            self.model.shutsubahyoFileSentakuDesc( \
                self.model.thisYear + "%"))
        [self.dlgDict[u"出馬表ファイル選択"].yearSelect.Append(item) for item in self.model.yearList]
        self.dlgDict[u"出馬表ファイル選択"].yearSelect.SetValue(self.model.thisYear)
        # self.dlgDict[u"出馬表ファイル選択"].SetListCtrl(self.model.showShutsubahyoFileSentaku())
        self.dlgDict[u"出馬表ファイル選択"].Bind( \
            wx.EVT_COMBOBOX, \
            self.onSelectYear, \
            self.dlgDict[u"出馬表ファイル選択"].yearSelect)
        self.dlgDict[u"出馬表ファイル選択"].Bind( \
            wx.EVT_LIST_ITEM_DESELECTED, \
            self.onListItemDeselected, \
            self.dlgDict[u"出馬表ファイル選択"].shutsubahyoFileSentakuView)
        self.dlgDict[u"出馬表ファイル選択"].Bind( \
            wx.EVT_LIST_ITEM_SELECTED, \
            self.onListItemSelected, \
            self.dlgDict[u"出馬表ファイル選択"].shutsubahyoFileSentakuView)
        self.dlgDict[u"出馬表ファイル選択"].Bind( \
            wx.EVT_LIST_ITEM_ACTIVATED, \
            self.onListItemActivated, \
            self.dlgDict[u"出馬表ファイル選択"].shutsubahyoFileSentakuView)
        shutsubahyo_file_sentaku_btn_dic = \
                                         { self.onHizukeKojunBtn: \
                                           self.dlgDict[u"出馬表ファイル選択"].hizukeKojunBtn, \
                                           self.onHizukeShojunBtn: \
                                           self.dlgDict[u"出馬表ファイル選択"].hizukeShojunBtn, \
                                           self.onBtnOK: \
                                           self.dlgDict[u"出馬表ファイル選択"].btnOK, \
                                           self.onBtnCancel: \
                                           self.dlgDict[u"出馬表ファイル選択"].btnCancel, \
                                           self.onBtnHelp: \
                                           self.dlgDict[u"出馬表ファイル選択"].btnHelp }
        [self.dlgDict[u"出馬表ファイル選択"].Bind( \
            wx.EVT_BUTTON, \
            k, \
            shutsubahyo_file_sentaku_btn_dic[k]) \
         for k in shutsubahyo_file_sentaku_btn_dic.keys()]

    def makeShutsubahyoRaceSentakuDlg(self):
        self.dlgDict[u"出馬表レース選択"] = ShutsubahyoRaceSentakuDlg(None)
        self.shutsubahyo_race_sentaku_btn_dic = \
                                              { self.onShutsubahyoBtn : \
                                                self.dlgDict[u"出馬表レース選択"].taKaisaiBtn, \
                                                self.onZenKaisaiBtn : \
                                                self.dlgDict[u"出馬表レース選択"].zenKaisaiBtn, \
                                                self.onJiKaisaiBtn : \
                                                self.dlgDict[u"出馬表レース選択"].jiKaisaiBtn }
        [self.dlgDict[u"出馬表レース選択"].Bind( \
            wx.EVT_BUTTON, \
            k, \
            self.shutsubahyo_race_sentaku_btn_dic[k])
         for k in self.shutsubahyo_race_sentaku_btn_dic.keys()]
        
    def onQuit(self, event): # wxGlade: yabusameFrame.<event_handler>
        # print "Event handler `onQuit' not implemented!"
        # event.Skip()
        self.view.Close()

    def onShutsubahyoBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        # print "Event handler `onShutsubahyoBtn' not implemented!"
        # event.Skip()
        self.makeShutsubahyoFileSentakuDlg()
        self.dlgDict[u"出馬表ファイル選択"].ShowModal()
        self.dlgDict[u"出馬表ファイル選択"].Destroy()

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
        if self.dlgDict[u"出馬表ファイル選択"]:
            self.dlgDict[u"出馬表ファイル選択"].RemoveListCtrl()
            self.dlgDict[u"出馬表ファイル選択"].SetListCtrl(message.data)
        elif self.dlgDict[u"出馬表レース選択"]:
            self.dlgDict[u"出馬表レース選択"].RemoveListCtrl()
            self.dlgDict[u"出馬表レース選択"].SetListCtrl(message.data)
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
        if self.dlgDict[u"出馬表ファイル選択"]:
            self.makeShutsubahyoRaceSentakuDlg()
            self.model.shutsubahyoRaceSentaku( \
                self.dlgDict[u"出馬表ファイル選択"].shutsubahyoFileSentakuView.GetItemText( \
                    self.currentItem)[:8] + '%')
            self.dlgDict[u"出馬表ファイル選択"].Destroy()
            self.dlgDict[u"出馬表レース選択"].ShowModal()
            self.dlgDict[u"出馬表レース選択"].Destroy()

    def onBtnOK(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnOK' not implemented!"
        event.Skip()

    def onBtnCancel(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onBtnCancel' not implemented!"
        # event.Skip()
        self.dlgDict[u"出馬表ファイル選択"].Destroy()

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
