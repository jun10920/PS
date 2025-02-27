SELECT HRE.EMP_NO, HRE.EMP_NAME, 
    CASE
        WHEN AVG(HRG.SCORE) >= 96 THEN 'S'
        WHEN AVG(HRG.SCORE) >= 90 THEN 'A'
        WHEN AVG(HRG.SCORE) >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN AVG(HRG.SCORE) >= 96 THEN SAL * 0.2
        WHEN AVG(HRG.SCORE) >= 90 THEN SAL * 0.15
        WHEN AVG(HRG.SCORE) >= 80 THEN SAL * 0.1
        ELSE 0
    END AS BONUS
FROM HR_DEPARTMENT AS HRD
JOIN HR_EMPLOYEES AS HRE ON HRD.DEPT_ID = HRE.DEPT_ID
JOIN HR_GRADE AS HRG ON HRE.EMP_NO = HRG.EMP_NO
GROUP BY 1, 2, HRE.SAL
ORDER BY 1
