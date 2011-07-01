#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sqlite3
import os.path

class DB:
    def __init__(self):
        db = os.path.join(os.path.dirname(__file__), "../Pckeiba/PC-KEIBA Database/Database/pckeiba.db")
        conn = sqlite3.connect(db)
        # Unicodeを利用するのに必要
        # conn.text_factory = sqlite3.OptimizedUnicode
        self.con = conn

    def SQLtemp(self):
        pass

    def getAllRows(self, **kwargs):
        # すべてのRowを取得する
        _cur = self.con.cursor()
        _cur.execute(self.SQLtemp(), kwargs)
        _data = _cur.fetchall()
        self.con.close()
        return _data
    
# if __name__ == '__main__':
