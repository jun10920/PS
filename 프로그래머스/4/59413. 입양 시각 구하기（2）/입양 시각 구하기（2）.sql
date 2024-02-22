WITH RECURSIVE HourSeries AS (
    SELECT 0 AS Hour
    UNION ALL
    SELECT Hour + 1 FROM HourSeries WHERE Hour < 23
)
SELECT hs.Hour, COUNT(ao.Animal_ID) AS AdoptionCount
FROM HourSeries hs
LEFT JOIN (SELECT *, HOUR(DATETIME) AS Hour FROM ANIMAL_OUTS) ao ON hs.Hour = ao.Hour
GROUP BY hs.Hour
ORDER BY hs.Hour;
