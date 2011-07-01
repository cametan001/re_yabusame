#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import db

class shutsubahyoRaceSentakuSQL(db.DB):
    def __init__(self):
        db.DB.__init__(self)

    def SQLtemp(self):
        _str = """ \
SELECT
    RA.RACE_CODE AS CODE
    , KC.CONTENT AS KEIBAJO
    , RA.RACE_BANGO AS RACE_BANGO
    , RA.KYOSOMEI_RYAKUSHO_6 ||
    CASE RA.JURYO_SHUBETSU_CODE
    WHEN '1' THEN 'H'
    ELSE ''
    END ||
    CASE 
    WHEN RA.GRADE_CODE = ' ' OR RA.GRADE_CODE = 'D' OR RA.GRADE_CODE = 'E' THEN KJC.CONTENT
    ELSE GC.CONTENT
    END ||
    CASE 
    WHEN RA.KYOSO_KIGO_CODE = '002' OR RA.KYOSO_KIGO_CODE = 'A02' THEN '・若'
    WHEN RA.KYOSO_KIGO_CODE BETWEEN '020' AND '025' THEN '・牝'
    WHEN RA.KYOSO_KIGO_CODE BETWEEN 'A20' AND 'A24' THEN '・牝'
    WHEN RA.KYOSO_KIGO_CODE BETWEEN 'N20' AND 'N24' THEN '・牝'
    ELSE ''
    END ||
    CASE
    WHEN RA.KYOSO_SHUBETSU_CODE = 11 AND RA.KYOSO_JOKEN_CODE_2SAI BETWEEN '004' AND '005' THEN '*'
    WHEN RA.KYOSO_SHUBETSU_CODE = 11 AND RA.KYOSO_JOKEN_CODE_2SAI BETWEEN '702' AND '703' THEN '*'
    WHEN RA.KYOSO_SHUBETSU_CODE = 12 AND RA.KYOSO_JOKEN_CODE_3SAI BETWEEN '004' AND '005' THEN '*'
    ELSE ''
    END AS RACEMEI
    , CASE 
    WHEN RA.TRACK_CODE = '00' THEN ''
    WHEN RA.TRACK_CODE BETWEEN '27' AND '28' THEN 'サ'
    WHEN RA.TRACK_CODE BETWEEN '23' AND '29' THEN 'ダ'
    WHEN RA.TRACK_CODE = '52' THEN 'ダ'
    ELSE '芝'
    END || RA.KYORI AS COURSE
    , CASE RA.DATA_KUBUN
    WHEN '1' THEN RA.TOROKU_TOSU
    WHEN '2' THEN RA.TOROKU_TOSU
    WHEN '9' THEN RA.TOROKU_TOSU
    ELSE RA.SHUSSO_TOSU
    END AS TOSU
    , strftime('%H:%M', RA.HASSO_JIKOKU) AS HASSO
FROM
    JVD_RACE_SHOSAI RA
    LEFT OUTER JOIN JVD_KEIBAJO_CODE KC
    ON KC.CODE = RA.KEIBAJO_CODE
    LEFT OUTER JOIN JVD_GRADE_CODE GC
    ON GC.CODE = RA.GRADE_CODE
    LEFT OUTER JOIN JVD_KYOSO_JOKEN_CODE KJC
    ON KJC.CODE = RA.KYOSO_JOKEN_CODE_SAIJAKUNEN
    LEFT OUTER JOIN JVD_KYOSO_KIGO_CODE KKC
    ON KKC.CODE = RA.KYOSO_KIGO_CODE
WHERE 1 = 1
    AND RA.RACE_CODE LIKE :code
    AND NOT (RA.DATA_KUBUN = 'A' OR RA.DATA_KUBUN = 'B')
ORDER BY
    RA.KEIBAJO_CODE
    , RA.RACE_BANGO
    ;
        """
        return _str

if __name__ == '__main__':
    v = shutsubahyoRaceSentakuSQL()
    u = v.getAllRows(code = '20110612%')
    for i in u:
        print i