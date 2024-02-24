SET @HOUR := -1;

SELECT @HOUR := @HOUR + 1, (SELECT COUNT(ANIMAL_ID)
                          FROM ANIMAL_OUTS
                          WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;