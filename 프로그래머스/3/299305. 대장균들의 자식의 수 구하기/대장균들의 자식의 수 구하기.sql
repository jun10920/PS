-- 코드를 작성해주세요
SELECT PARENT.ID, COUNT(CHILD.PARENT_ID) AS CHILD_COUNT
FROM ECOLI_DATA AS PARENT
LEFT JOIN ECOLI_DATA AS CHILD ON CHILD.PARENT_ID = PARENT.ID
GROUP BY PARENT.ID
ORDER BY PARENT.ID