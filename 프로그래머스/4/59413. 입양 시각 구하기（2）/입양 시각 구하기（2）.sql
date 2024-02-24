WITH RECURSIVE HOURLIST AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1 
    FROM HOURLIST 
    WHERE HOUR < 23
)

SELECT HOURLIST.HOUR, COUNT(AO.ANIMAL_ID) AS COUNT
FROM HOURLIST
LEFT JOIN ANIMAL_OUTS AS AO ON HOURLIST.HOUR = HOUR(AO.DATETIME)
GROUP BY HOURLIST.HOUR
ORDER BY HOURLIST.HOUR;
