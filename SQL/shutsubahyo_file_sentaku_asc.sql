SELECT
    strftime('%m月%d日(', RA.KAISAI_NENGAPPI) || YC.CONTENT || ')' AS HIZUKE
    , COUNT(*) AS RSU
    , CASE RA.DATA_KUBUN
    WHEN 1 OR 2 THEN 'D'
    ELSE 'S'
    END AS D
    , RA.RACE_CODE AS CODE
FROM
    JVD_RACE_SHOSAI RA
    OUTER LEFT JOIN JVD_YOBI_CODE YC
    ON YC.CODE = RA.YOBI_CODE
    OUTER LEFT JOIN JVD_KEIBAJO_CODE KC
    ON KC.CODE = RA.KEIBAJO_CODE
    OUTER LEFT JOIN JVD_GRADE_CODE GC
    ON GC.CODE = RA.GRADE_CODE
WHERE 1 = 1
    AND RA.RACE_CODE LIKE '2011%'
    AND NOT (RA.DATA_KUBUN = 'A' OR RA.DATA_KUBUN = 'B')
GROUP BY
    RA.KAISAI_NENGAPPI
ORDER BY
    RA.KAISAI_NENGAPPI ASC
    ;