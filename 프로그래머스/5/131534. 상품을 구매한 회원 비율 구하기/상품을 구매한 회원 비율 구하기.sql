SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, 
       COUNT(DISTINCT USER_ID) AS PUCHASED_USERS, 
       ROUND(COUNT(DISTINCT USER_ID)/(SELECT COUNT(USER_ID) 
                                      FROM USER_INFO 
                                      WHERE YEAR(JOINED) = 2021), 1) AS PUCHASED_RATIO
FROM USER_INFO JOIN ONLINE_SALE USING(USER_ID)
WHERE YEAR(JOINED)=2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH