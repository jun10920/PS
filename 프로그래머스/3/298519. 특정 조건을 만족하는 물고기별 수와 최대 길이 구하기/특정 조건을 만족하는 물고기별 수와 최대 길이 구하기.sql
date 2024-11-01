SELECT 
    COUNT(ID) AS FISH_COUNT,
    MAX(LENGTH) AS MAX_LENGTH,
    FISH_TYPE
        
FROM 
    FISH_INFO
WHERE 
    FISH_TYPE IN (
        SELECT 
            FISH_TYPE
        FROM 
            FISH_INFO
        GROUP BY 
            FISH_TYPE
        HAVING 
            AVG(COALESCE(LENGTH, 10)) >= 33
    )
GROUP BY 
    FISH_TYPE
ORDER BY 
    FISH_TYPE;
