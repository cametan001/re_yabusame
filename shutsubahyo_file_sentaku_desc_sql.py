#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import db

class shutsubahyoFileSentakuDescSQL(db.DB):
    def __init__(self):
        db.DB.__init__(self)

    def SQLtemp(self):
        _str = """ \
SELECT
    RA.RACE_CODE AS CODE
    , strftime('%m月%d日(', RA.KAISAI_NENGAPPI) || YC.CONTENT || ')' AS HIZUKE
    , COUNT(*) AS RSU
    , CASE RA.DATA_KUBUN
    WHEN 1 OR 2 THEN 'D'
    ELSE 'S'
    END AS D
FROM
    JVD_RACE_SHOSAI RA
    OUTER LEFT JOIN JVD_YOBI_CODE YC
    ON YC.CODE = RA.YOBI_CODE
    OUTER LEFT JOIN JVD_KEIBAJO_CODE KC
    ON KC.CODE = RA.KEIBAJO_CODE
    OUTER LEFT JOIN JVD_GRADE_CODE GC
    ON GC.CODE = RA.GRADE_CODE
WHERE 1 = 1
    AND RA.RACE_CODE LIKE :year
    AND NOT (RA.DATA_KUBUN = 'A' OR RA.DATA_KUBUN = 'B')
GROUP BY
    RA.KAISAI_NENGAPPI
ORDER BY
    RA.KAISAI_NENGAPPI DESC
    ;
        """
        return _str

if __name__ == '__main__':
    v = shutsubahyoFileSentakuDescSQL()
    u = v.getAllRows(year = '2011%')
    print u
    print u.reverse()
