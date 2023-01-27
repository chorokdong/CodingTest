-- https://school.programmers.co.kr/learn/courses/30/lessons/59413

WITH RECURSIVE tmp1 AS(
    SELECT 0 AS HOUR
    UNION ALL
        SELECT HOUR + 1 
        FROM tmp1
        WHERE HOUR < 23)
    

SELECT tmp1.HOUR, IFNULL(US.count,0)
FROM tmp1
LEFT JOIN (SELECT HOUR(datetime) AS hour, count(DISTINCT(animal_id)) as count
            FROM animal_outs
            GROUP BY 1) AS US ON tmp1.HOUR = US.hour