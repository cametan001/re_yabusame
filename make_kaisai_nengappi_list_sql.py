#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import db

class makeKaisaiNengappiList(db.DB):
    def __init__(self):
        db.DB.__init__(self)

    def SQLtemp(self):
        _str = """ \
SELECT DISTINCT
    strftime('%Y%m%d', RA.KAISAI_NENGAPPI)
    , strftime('%Y年 %m月%d日(', RA.KAISAI_NENGAPPI) || YC.CONTENT || ')'
FROM
    JVD_RACE_SHOSAI RA
    LEFT OUTER JOIN JVD_YOBI_CODE YC
    ON YC.CODE = RA.YOBI_CODE
WHERE 1 = 1
    AND RA.KAISAI_NENGAPPI >= JULIANDAY('1986-01-01')
    AND NOT (RA.DATA_KUBUN = 'A' OR RA.DATA_KUBUN = 'B')
ORDER BY
    RA.KAISAI_NENGAPPI DESC
    ;
        """
        return _str

if __name__ == '__main__':
    v = makeKaisaiNengappiList()
    for i in v.getAllRows():
        for j in i:
            print j.encode('utf_8'),
        print '\n'
            
