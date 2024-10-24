SELECT E1.ID
FROM ECOLI_DATA AS E1
INNER JOIN ECOLI_DATA AS E2 ON E1.PARENT_ID = E2.ID
INNER JOIN ECOLI_DATA AS E3 ON E2.PARENT_ID = E3.ID
WHERE E3.PARENT_ID IS NULL
ORDER BY E1.ID ASC;
