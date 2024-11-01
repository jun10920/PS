WITH RECURSIVE gen(id, parent_id, generation) AS (
    SELECT id, parent_id, 1
    FROM ecoli_data
    WHERE parent_id IS NULL

    UNION ALL

    SELECT C.id, C.parent_id, generation + 1
    FROM ecoli_data C
    JOIN gen P ON P.id = C.parent_id
)

SELECT COUNT(*) count, generation
FROM gen 
WHERE NOT EXISTS (SELECT 1 FROM gen B WHERE gen.id = B.parent_id)
GROUP BY generation
ORDER BY generation;