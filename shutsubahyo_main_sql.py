#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import db

class shutsubahyoMainSQL(db.DB):
    def __init__(self):
        db.DB.__init__(self)

    def SQLtemp(self):
        _str = """ \
SELECT
    strftime('%Y年 %m月%d日(', RA.KAISAI_NENGAPPI) || YC.CONTENT || ')' AS KAISAI_NENGAPPI
    , ' ' || RA.KAISAI_KAIJI || '回' || KC.CONTENT || RA.KAISAI_NICHIJI || '日目 ' AS KAISAI_KAIJI
    , CASE
    WHEN RA.DATA_KUBUN BETWEEN '1' AND '2' THEN RA.TOROKU_TOSU
    ELSE RA.SHUSSO_TOSU
    END ||
    '頭' AS TOSU
    , strftime('%H:%M発走', RA.HASSO_JIKOKU) AS HASSO_TIME
    , TC.CONTENT AS TENKO
    , RA.RACE_BANGO || 'R' AS RACE_BANGO
    , CASE RA.JUSHO_KAIJI WHEN 0 THEN ''
    ELSE '第' || RA.JUSHO_KAIJI || '回'
    END ||
    RA.KYOSOMEI_HONDAI AS HONDAI
    , KSC.CONTENT || '・' ||
    CASE
    WHEN RA.KYOSO_JOKEN_CODE_SAIJAKUNEN BETWEEN '001' AND '099' THEN KJC.CONTENT || '下'
    ELSE KJC.CONTENT
    END ||
    CASE
    WHEN RA.GRADE_CODE = ' ' OR RA.GRADE_CODE = 'D' OR RA.GRADE_CODE = 'E' THEN ''
    ELSE '・' || GC.CONTENT
    END ||
    '(' || JSC.CONTENT || ')' ||  KKC.CONTENT AS JOKEN
    , CASE
    WHEN RA.TRACK_CODE BETWEEN '10' AND '22' THEN '芝'
    WHEN RA.TRACK_CODE BETWEEN '23' AND '29' THEN 'ダート'
    WHEN RA.TRACK_CODE BETWEEN '51' AND '59' THEN '障害'
    ELSE ''
    END ||
    RA.KYORI || 'm' ||
    CASE RA.COURSE_KUBUN
    WHEN '  ' THEN ''
    ELSE '(' || rtrim(RA.COURSE_KUBUN) || ')'
    END AS KYORI
    , CASE
    WHEN RA.DATA_KUBUN BETWEEN '3' AND '7' THEN TBC.CONTENT
    ELSE ''
    END ||
    CASE
    WHEN RA.DATA_KUBUN BETWEEN '3' AND '7' THEN DBC.CONTENT
    ELSE ''
    END AS BABA_JOTAI
    , '本賞金[1着]' || (RA.HONSHOKIN1 / 100) || '万[2着]' || (RA.HONSHOKIN2 / 100) ||
    '万[3着]' || (RA.HONSHOKIN3 / 100) || '万[4着]' || (RA.HONSHOKIN4 / 100) ||
    '万[5着]' || (RA.HONSHOKIN5 / 100) || '万' AS HONSHOKIN
    , '付加賞[1着]' || (1.0 * RA.FUKASHOKIN1 / 100) || '万[2着]' || (1.0 * RA.FUKASHOKIN2 / 100) ||
    '万[3着]' || (1.0 * RA.FUKASHOKIN3 / 100) || '万' AS FUKASHOKIN
FROM
    JVD_RACE_SHOSAI RA
    LEFT OUTER JOIN JVD_YOBI_CODE YC
    ON YC.CODE = RA.YOBI_CODE
    LEFT OUTER JOIN JVD_KEIBAJO_CODE KC
    ON KC.CODE = RA.KEIBAJO_CODE
    LEFT OUTER JOIN JVD_TENKO_CODE TC
    ON TC.CODE = RA.TENKO_CODE
    LEFT OUTER JOIN JVD_KYOSO_SHUBETSU_CODE KSC
    ON KSC.CODE = RA.KYOSO_SHUBETSU_CODE
    LEFT OUTER JOIN JVD_KYOSO_JOKEN_CODE KJC
    ON KJC.CODE = RA.KYOSO_JOKEN_CODE_SAIJAKUNEN
    LEFT OUTER JOIN JVD_GRADE_CODE GC
    ON GC.CODE = RA.GRADE_CODE
    LEFT OUTER JOIN JVD_JURYO_SHUBETSU_CODE JSC
    ON JSC.CODE = RA.JURYO_SHUBETSU_CODE
    LEFT OUTER JOIN JVD_KYOSO_KIGO_CODE KKC
    ON KKC.CODE = RA.KYOSO_KIGO_CODE
    LEFT OUTER JOIN JVD_BABAJOTAI_CODE TBC
    ON TBC.CODE = RA.SHIBA_BABAJOTAI_CODE
    LEFT OUTER JOIN JVD_BABAJOTAI_CODE DBC
    ON DBC.CODE = RA.DIRT_BABAJOTAI_CODE
WHERE 1 = 1
    AND RA.RACE_CODE = :code
    ;
        """
        return _str

if __name__ == '__main__':
    v = shutsubahyoMainSQL()
    for i in v.getAllRows(code = '2011062609040411'):
        for j in i:
            print j.encode('utf_8'),
        print '\n'
