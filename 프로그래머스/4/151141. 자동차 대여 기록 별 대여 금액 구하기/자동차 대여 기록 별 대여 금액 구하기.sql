# -- 코드를 입력하세요
# SELECT DISTINCT HIS.HISTORY_ID, 
# CASE
#     WHEN (DATEDIFF(END_DATE, START_DATE) + 1) >= 7 THEN
#     ROUND(SUM((DATEDIFF(END_DATE, START_DATE) + 1) * CAR.DAILY_FEE * 0.95))
#     WHEN (DATEDIFF(END_DATE, START_DATE) + 1) >= 30 THEN
#     ROUND(SUM((DATEDIFF(END_DATE, START_DATE) + 1) * CAR.DAILY_FEE * 0.93))
#     WHEN (DATEDIFF(END_DATE, START_DATE) + 1) >= 90 THEN
#     ROUND(SUM((DATEDIFF(END_DATE, START_DATE) + 1) * CAR.DAILY_FEE * 0.9))
#     ELSE SUM((DATEDIFF(END_DATE, START_DATE) + 1) * CAR.DAILY_FEE)
# END AS FEE
# FROM CAR_RENTAL_COMPANY_CAR AS CAR
# JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS PLAN ON CAR.CAR_TYPE = PLAN.CAR_TYPE
# JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HIS ON CAR.CAR_ID = HIS.CAR_ID
# WHERE CAR.CAR_TYPE LIKE '트럭'
# GROUP BY HIS.HISTORY_ID
# ORDER BY 2 DESC, 1 DESC


SELECT HISTORY_ID, 
    round(DAILY_FEE * (DATEDIFF(h.END_DATE,h.START_DATE)+1)
    * (case 
    when DATEDIFF(END_DATE,START_DATE)+1 < 7 then 1
    when DATEDIFF(END_DATE,START_DATE)+1 < 30 then 0.95
    when DATEDIFF(END_DATE,START_DATE)+1 < 90 then 0.92
    else 0.85 end)) as "FEE"

from CAR_RENTAL_COMPANY_CAR as c 
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    on c.CAR_ID = h.CAR_ID
    join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
    on c.CAR_TYPE = p.CAR_TYPE

where c.car_type = "트럭"

group by HISTORY_ID

order by FEE desc , HISTORY_ID desc