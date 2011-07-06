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
import shutsubahyo_main_sql as sms
import shutsubahyo_base_sql as sbs
import shutsubahyo_ketto_sql as sks

# Model
class Model:
    def __init__(self):
        self.thisYear = str(dt.today().year)
        self.flagDict = { \
            "order" : "d", \
            "day" : False, \
            "ListItem" : False, \
            "raceCodePos" : False }
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
        if self.flagDict["order"] == "d":
            pub.sendMessage("FILE CHOSEN", self.shutsubahyoFileSentakuDesc(yearCode))
        elif self.flagDict["order"] == "a":
            pub.sendMessage("FILE CHOSEN", self.shutsubahyoFileSentakuAsc(yearCode))
        else:
            pass

    def shutsubahyoFileSentakuDesc(self, value):
        _data = sfsds.shutsubahyoFileSentakuDescSQL()
        return _data.getAllRows(year = value)
        
    def shutsubahyoFileSentakuAsc(self, value):
        _data = sfsas.shutsubahyoFileSentakuAscSQL()
        return _data.getAllRows(year = value)

    def shutsubahyoRaceSentaku(self, value):
        self.flagDict["day"] = value
        _data = srss.shutsubahyoRaceSentakuSQL()
        aList = _data.getAllRows(code = self.flagDict["day"] + "%")
        self.raceCodeList = [i[0] for i in aList]
        nameList = ["%s%sR %s" % (i[1], i[2], i[3]) for i in aList]
        self.titleDict = dict(zip(self.raceCodeList, nameList))
        pub.sendMessage("RACE CHOSEN", { \
            u"日時" : self.kaisaiNengappiDict[value],
            u"レースリスト" : aList} )

    def shutsubahyo(self, value):
        pub.sendMessage("RACE FORM CHOSEN", { \
            u"タイトル" : self.titleDict[value], \
            u"出馬表" : self.shutsubahyoMain(value), \
            u"基本" : self.shutsubahyoBase(value), \
            u"血統" : self.shutsubahyoKetto(value) })

    def shutsubahyoMain(self, value):
        _data = sms.shutsubahyoMainSQL()
        return _data.getAllRows(code = value)

    def shutsubahyoBase(self, value):
        _data = sbs.shutsubahyoBaseSQL()
        return _data.getAllRows(code = value)

    def shutsubahyoKetto(self, value):
        _data = sks.shutsubahyoKettoSQL()
        return _data.getAllRows(code = value)

# View
class View(mvc.yabusameFrame):
    def __init__(self, *args, **kwds):
        mvc.yabusameFrame.__init__(self, *args, **kwds)

class ShutsubahyoFileSentakuDlg(mvc.shutsubahyoFileSentakuDialog):
    def __init__(self, *args, **kwds):
        mvc.shutsubahyoFileSentakuDialog.__init__(self, *args, **kwds)

    def SetListCtrl(self, data):
        cs = [u'コード', u'日付↓', u'R数', u'D']
        [self.shutsubahyoFileSentakuView.InsertColumn(cs.index(heading), heading) for heading in cs]
        [self.shutsubahyoFileSentakuView.Append(i) for i in data]
        [self.shutsubahyoFileSentakuView.SetColumnWidth(i, wx.LIST_AUTOSIZE) for i in range (len(cs))]

    def RemoveListCtrl(self):
        self.shutsubahyoFileSentakuView.ClearAll()

class ShutsubahyoRaceSentakuDlg(mvc.shutsubahyoRaceSentakuDialog):
    def __init__(self, *args, **kwds):
        mvc.shutsubahyoRaceSentakuDialog.__init__(self, *args, **kwds)

    def SetListCtrl(self, data):
        cs = [u'コード', u'場所', u'R', u'レース', u'コース', u'頭', u'発走']
        [self.shutsubahyoRaceSentakuView.InsertColumn(cs.index(heading), heading) for heading in cs]
        [self.shutsubahyoRaceSentakuView.Append(i) for i in data]
        [self.shutsubahyoRaceSentakuView.SetColumnWidth(i, wx.LIST_AUTOSIZE) for i in range (len(cs))]

    def RemoveListCtrl(self):
        self.shutsubahyoRaceSentakuView.ClearAll()

class ShutsubahyoDlg(mvc.shutsubahyoDialog):
    def __init__(self, *args, **kwds):
        mvc.shutsubahyoDialog.__init__(self, *args, **kwds)

    def SetLabels(self, data):
        labelList = [self.kaisaiNengappiLabel, self.kaisaiKaijiLabel, \
                     self.tosuLabel, self.hassoLabel, self.tenkoLabel, \
                     self.raceBangoLabel, self.raceHondaiLabel, \
                     self.jokenLabel, self.courseLabel, self.babaJotaiLabel, \
                     self.honshokinLabel, self.fukashokinLabel]
        [i[0].SetLabel(i[1].encode('utf_8')) for i in zip(labelList, data[0])]

    def SetKihonView(self, data):
        cs = [u'枠', u'番', u'馬名', u'性齢', u'騎手', u'斤量', u'単勝', \
              u'馬体重', u'調教師', u'馬記号', u'馬主', u'生産者', u'毛色', u'誕生']
        [self.kihonView.InsertColumn(cs.index(heading), heading) for heading in cs]
        [self.kihonView.Append(i) for i in data]
        [self.kihonView.SetColumnWidth(i, wx.LIST_AUTOSIZE) for i in range (len(cs))]

    def SetKettoView(self, data):
        cs = [u'枠', u'番', u'馬名', u'性齢', u'騎手', u'斤量', \
              u'単勝', u'馬体重', u'父', u'母', u'母父', u'母の母']
        [self.kettoView.InsertColumn(cs.index(heading), heading) for heading in cs]
        [self.kettoView.Append(i) for i in data]
        [self.kettoView.SetColumnWidth(i, wx.LIST_AUTOSIZE) for i in range (len(cs))]

    def RemoveListCtrl(self):
        viewList = [self.kihonView, self.kettoView]
        [i.ClearAll() for i in viewList]

# Controller
class Controller:
    def __init__(self, app):
        self.model = Model()

        #set up the frame which displays the current Model value
        self.view = View(None)
        # Quitボタン設定
        self.view.Bind(wx.EVT_TOOL, self.onQuit, id=-1)
        # ボタン設定
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
        
        pub.subscribe(self.ChooseFile, "FILE CHOSEN")
        pub.subscribe(self.ChooseRace, "RACE CHOSEN")
        pub.subscribe(self.ChooseRaceForm, "RACE FORM CHOSEN")
        
        self.view.Show()

    def makeShutsubahyoFileSentakuDlg(self):
        #set up the first dialog which allows the user to modify the Model's value
        self.dlgDict[u"ファイル選択"] = ShutsubahyoFileSentakuDlg(None)
        # 初期表示
        self.dlgDict[u"ファイル選択"].SetListCtrl( \
            self.model.shutsubahyoFileSentakuDesc( \
                self.model.thisYear + "%"))
        [self.dlgDict[u"ファイル選択"].yearSelect.Append(item) for item in self.model.yearList]
        self.dlgDict[u"ファイル選択"].yearSelect.SetValue(self.model.thisYear)
        # コンボボックス設定
        self.dlgDict[u"ファイル選択"].Bind( \
            wx.EVT_COMBOBOX, \
            self.onSelectYear, \
            self.dlgDict[u"ファイル選択"].yearSelect)
        # ビュー設定
        self.dlgDict[u"ファイル選択"].Bind( \
            wx.EVT_LIST_ITEM_DESELECTED, \
            self.onListItemDeselected, \
            self.dlgDict[u"ファイル選択"].shutsubahyoFileSentakuView)
        self.dlgDict[u"ファイル選択"].Bind( \
            wx.EVT_LIST_ITEM_SELECTED, \
            self.onListItemSelected, \
            self.dlgDict[u"ファイル選択"].shutsubahyoFileSentakuView)
        self.dlgDict[u"ファイル選択"].Bind( \
            wx.EVT_LIST_ITEM_ACTIVATED, \
            self.onListItemActivated, \
            self.dlgDict[u"ファイル選択"].shutsubahyoFileSentakuView)
        # ボタン設定
        shutsubahyo_file_sentaku_btn_dic = \
                                         { self.onHizukeKojunBtn: \
                                           self.dlgDict[u"ファイル選択"].hizukeKojunBtn, \
                                           self.onHizukeShojunBtn: \
                                           self.dlgDict[u"ファイル選択"].hizukeShojunBtn, \
                                           self.onBtnOK: \
                                           self.dlgDict[u"ファイル選択"].btnOK, \
                                           self.onBtnCancel: \
                                           self.dlgDict[u"ファイル選択"].btnCancel, \
                                           self.onBtnHelp: \
                                           self.dlgDict[u"ファイル選択"].btnHelp }
        [self.dlgDict[u"ファイル選択"].Bind( \
            wx.EVT_BUTTON, \
            k, \
            shutsubahyo_file_sentaku_btn_dic[k]) \
         for k in shutsubahyo_file_sentaku_btn_dic.keys()]

    def makeShutsubahyoRaceSentakuDlg(self):
        self.dlgDict[u"レース選択"] = ShutsubahyoRaceSentakuDlg(None)
        # ボタン設定
        shutsubahyo_race_sentaku_btn_dic = \
                                         { self.onShutsubahyoBtn : \
                                           self.dlgDict[u"レース選択"].taKaisaiBtn, \
                                           self.onZenKaisaiBtn : \
                                           self.dlgDict[u"レース選択"].zenKaisaiBtn, \
                                           self.onJiKaisaiBtn : \
                                           self.dlgDict[u"レース選択"].jiKaisaiBtn }
        [self.dlgDict[u"レース選択"].Bind( \
            wx.EVT_BUTTON, \
            k, \
            shutsubahyo_race_sentaku_btn_dic[k])
         for k in shutsubahyo_race_sentaku_btn_dic.keys()]
        # ビュー設定
        self.dlgDict[u"レース選択"].Bind( \
            wx.EVT_LIST_ITEM_DESELECTED, \
            self.onListItemDeselected, \
            self.dlgDict[u"レース選択"].shutsubahyoRaceSentakuView)
        self.dlgDict[u"レース選択"].Bind( \
            wx.EVT_LIST_ITEM_SELECTED, \
            self.onListItemSelected, \
            self.dlgDict[u"レース選択"].shutsubahyoRaceSentakuView)
        self.dlgDict[u"レース選択"].Bind( \
            wx.EVT_LIST_ITEM_ACTIVATED, \
            self.onListItemActivated, \
            self.dlgDict[u"レース選択"].shutsubahyoRaceSentakuView)

    def makeShutsubahyoDlg(self):
        #set up the third dialog which allows the user to modify the Model's value
        self.dlgDict[u"出馬表"] = ShutsubahyoDlg(None)

        # ボタン設定
        shutsubahyo_btn_dic = \
                            { self.onTaRaceBtn : \
                              self.dlgDict[u"出馬表"].taRaceBtn, \
                              self.onAnotherButton : \
                              self.dlgDict[u"出馬表"].anotherBtn, \
                              self.onTheOtherBtn : \
                              self.dlgDict[u"出馬表"].theOtherBtn, \
                              self.onTaisenBtn : \
                              self.dlgDict[u"出馬表"].taisenBtn, \
                              self.onKaisaiBunsekiBtn : \
                              self.dlgDict[u"出馬表"].kaisaiBunsekiBtn, \
                              self.onHanroChokoBtn : \
                              self.dlgDict[u"出馬表"].hanroChokyoBtn, \
                              self.onKettohyoBtn : \
                              self.dlgDict[u"出馬表"].kettohyoBtn, \
                              self.onOddsBtn : \
                              self.dlgDict[u"出馬表"].oddsBtn, \
                              self.onZenRaceBtn : \
                              self.dlgDict[u"出馬表"].zenRaceBtn, \
                              self.onJiRaceBtn : \
                              self.dlgDict[u"出馬表"].jiRaceBtn, \
                              self.onBtn1 : \
                              self.dlgDict[u"出馬表"].button_1, \
                              self.onBtn2 : \
                              self.dlgDict[u"出馬表"].button_2, \
                              self.onBtn3 : \
                              self.dlgDict[u"出馬表"].button_3 }
        [self.dlgDict[u"出馬表"].Bind( \
            wx.EVT_BUTTON, \
            k, \
            shutsubahyo_btn_dic[k])
         for k in shutsubahyo_btn_dic.keys()]
        
    def onQuit(self, event): # wxGlade: yabusameFrame.<event_handler>
        # print "Event handler `onQuit' not implemented!"
        # event.Skip()
        self.view.Close()

    def onShutsubahyoBtn(self, event): # wxGlade: yabusameFrame.<event_handler>
        # print "Event handler `onShutsubahyoBtn' not implemented!"
        # event.Skip()
        self.makeShutsubahyoFileSentakuDlg()
        self.model.flagDict["ListItem"] = "shutsubahyoFileSentakuDlg"
        self.dlgDict[u"ファイル選択"].ShowModal()
        self.dlgDict[u"ファイル選択"].Destroy()

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
        self.model.flagDict["order"] = "d"
        self.model.showShutsubahyoFileSentaku()

    def onHizukeShojunBtn(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onHizureShojunBtn' not implemented!"
        # event.Skip()
        self.model.flagDict["order"] = "a"
        self.model.showShutsubahyoFileSentaku()

    def ChooseFile(self, message):
        # print "Event handler `OederChanged' not implemented!"
        # event.Skip()
        self.dlgDict[u"ファイル選択"].RemoveListCtrl()
        self.dlgDict[u"ファイル選択"].SetListCtrl(message.data)

    def ChooseRace(self, message):
        # print "Event handler `OederChanged' not implemented!"
        # event.Skip()
        self.dlgDict[u"レース選択"].kaisaiNichijiLabel.SetLabel(message.data[u"日時"])
        self.dlgDict[u"レース選択"].RemoveListCtrl()
        self.dlgDict[u"レース選択"].SetListCtrl(message.data[u"レースリスト"])

    def ChooseRaceForm(self, message):
        # print "Event handler `OederChanged' not implemented!"
        # event.Skip()
        self.dlgDict[u"出馬表"].SetTitle(u"出馬表・%s" % message.data[u"タイトル"])
        self.dlgDict[u"出馬表"].SetLabels(message.data[u"出馬表"])
        self.dlgDict[u"出馬表"].RemoveListCtrl()
        self.dlgDict[u"出馬表"].SetKihonView(message.data[u"基本"])
        self.dlgDict[u"出馬表"].SetKettoView(message.data[u"血統"])
    
    def onListItemDeselected(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemDeselected' not implemented!"
        event.Skip()

    def onListItemSelected(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onListItemSelected' not implemented!"
        event.Skip()

    def onListItemActivated(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        # print "Event handler `onListItemActivated' not implemented!"
        # event.Skip()
        currentItem = event.m_itemIndex
        if self.model.flagDict["ListItem"] == "shutsubahyoFileSentakuDlg":
            self.makeShutsubahyoRaceSentakuDlg()
            self.model.flagDict["ListItem"] = "shutsubahyoRaceSentakuDlg"
            code= \
                  self.dlgDict[u"ファイル選択"].shutsubahyoFileSentakuView.GetItemText(currentItem)[:8]
            self.model.shutsubahyoRaceSentaku(code)
            self.dlgDict[u"レース選択"].ShowModal()
            self.dlgDict[u"レース選択"].Destroy()
        elif self.model.flagDict["ListItem"] == "shutsubahyoRaceSentakuDlg":
            self.makeShutsubahyoDlg()
            self.model.flagDict["ListItem"] = "shutsubahyoDlg"
            code= \
                  self.dlgDict[u"レース選択"].shutsubahyoRaceSentakuView.GetItemText(currentItem)
            self.model.flagDict["raceCodePos"] = self.model.raceCodeList.index(code)
            self.model.shutsubahyo(code)
            self.dlgDict[u"出馬表"].ShowModal()
            self.dlgDict[u"出馬表"].Destroy()
        else:
            pass

    def onBtnOK(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnOK' not implemented!"
        event.Skip()

    def onBtnCancel(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnCancel' not implemented!"
        event.Skip()

    def onBtnHelp(self, event): # wxGlade: shutsubahyoFileSentakuDialog.<event_handler>
        print "Event handler `onBtnHelp' not implemented!"
        event.Skip()

    def onZenKaisaiBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        # print "Event handler `onZenKaisaiBtn' not implemented!"
        # event.Skip()
        id = self.model.kaisaiNengappiKeyList.index(self.model.day) + 1
        code = self.model.kaisaiNengappiKeyList[id]
        self.model.shutsubahyoRaceSentaku(code)

    def onJiKaisaiBtn(self, event): # wxGlade: shutsubahyoRaceSentakuDialog.<event_handler>
        # print "Event handler `onJiKaisaiBtn' not implemented!"
        # event.Skip()
        id = self.model.kaisaiNengappiKeyList.index(self.model.day) - 1
        code = self.model.kaisaiNengappiKeyList[id]
        self.model.shutsubahyoRaceSentaku(code)

    # 出馬表関連
    def onTaRaceBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onTaRaceBtn' not implemented!"
        event.Skip()

    def onAnotherButton(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onAnotherButton' not implemented!"
        event.Skip()

    def onTheOtherBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onTheOtherBtn' not implemented!"
        event.Skip()

    def onTaisenBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onTaisenBtn' not implemented!"
        event.Skip()

    def onKaisaiBunsekiBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onKaisaiBunsekiBtn' not implemented!"
        event.Skip()

    def onHanroChokoBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onHanroChokoBtn' not implemented!"
        event.Skip()

    def onKettohyoBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onKettohyoBtn' not implemented!"
        event.Skip()

    def onOddsBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onOddsBtn' not implemented!"
        event.Skip()

    def onZenRaceBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        # print "Event handler `onZenRaceBtn' not implemented!"
        # event.Skip()
        idx = self.model.flagDict["raceCodePos"] - 1
        self.model.flagDict["raceCodePos"] = idx
        code = self.model.raceCodeList[idx]
        self.model.shutsubahyo(code)

    def onJiRaceBtn(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        # print "Event handler `onJiRaceBtn' not implemented!"
        # event.Skip()
        idx = self.model.flagDict["raceCodePos"] + 1
        self.model.flagDict["raceCodePos"] = idx
        code = self.model.raceCodeList[idx]
        self.model.shutsubahyo(code)

    def onBtn1(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onBtn1' not implemented!"
        event.Skip()

    def onBtn2(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onBtn2' not implemented!"
        event.Skip()

    def onBtn3(self, event): # wxGlade: shutsubahyoDialog.<event_handler>
        print "Event handler `onBtn3' not implemented!"
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()
