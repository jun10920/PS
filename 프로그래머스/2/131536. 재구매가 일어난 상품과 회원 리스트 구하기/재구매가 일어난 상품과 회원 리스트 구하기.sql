-- 코드를 입력하세요
SELECT DISTINCT OS1.USER_ID, OS1.PRODUCT_ID
FROM ONLINE_SALE AS OS1
JOIN ONLINE_SALE AS OS2 ON OS1.USER_ID = OS2.USER_ID
WHERE OS1.PRODUCT_ID = OS2.PRODUCT_ID AND OS1.ONLINE_SALE_ID != OS2.ONLINE_SALE_ID
ORDER BY USER_ID ASC, PRODUCT_ID DESC;