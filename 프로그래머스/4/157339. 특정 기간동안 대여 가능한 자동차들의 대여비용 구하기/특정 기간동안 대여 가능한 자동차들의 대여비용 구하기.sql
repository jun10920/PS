-- 코드를 입력하세요
SELECT CAR.CAR_ID, CAR.CAR_TYPE, ROUND((100 - PLAN.DISCOUNT_RATE)/100 * CAR.DAILY_FEE * 30) AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HIS
JOIN CAR_RENTAL_COMPANY_CAR AS CAR ON HIS.CAR_ID = CAR.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS PLAN ON CAR.CAR_TYPE = PLAN.CAR_TYPE
WHERE CAR.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-12-01') 
AND PLAN.DURATION_TYPE LIKE '30%'
GROUP BY CAR.CAR_ID 
HAVING CAR.CAR_TYPE IN ('세단', 'SUV') AND (FEE >= 500000 AND FEE < 2000000) 
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC