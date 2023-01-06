-- https://school.programmers.co.kr/learn/courses/30/lessons/77487


SELECT *
FROM places AS a
WHERE a.host_id in (SELECT host_id
                   FROM places
                   GROUP BY host_id
                   HAVING COUNT(host_id) >= 2
                    )
ORDER BY id ASC                    



-- GROUP BY를 사용하지 않을 경우

SELECT *
FROM places a
WHERE (SELECT COUNT(host_id) as host_id
       FROM places
       WHERE host_id = a.host_id) >= 2
ORDER BY id