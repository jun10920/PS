-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, COUNT(DISTINCT USER_ID) AS PURCHASED_USERS, ROUND(COUNT(DISTINCT USER_ID) / (SELECT COUNT(USER_ID)
                                    FROM USER_INFO
                                    WHERE YEAR(JOINED) = 2021                                                                                     ), 1) AS PURCHASED_RATIO
FROM USER_INFO
JOIN ONLINE_SALE USING (USER_ID)
WHERE YEAR(JOINED) = 2021
GROUP BY 1, 2
ORDER BY 1, 2