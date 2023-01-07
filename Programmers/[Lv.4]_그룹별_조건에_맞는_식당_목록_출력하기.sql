-- https://school.programmers.co.kr/learn/courses/30/lessons/131124


SELECT a.member_name, b.review_text, DATE_FORMAT(b.review_date, '%Y-%m-%d') AS review_date
FROM member_profile a
LEFT JOIN rest_review b ON a.member_id = b.member_id
WHERE b.member_id = (SELECT member_id	
                     FROM rest_review
                     GROUP BY 1
                     ORDER BY COUNT(*) DESC 
                     LIMIT 1)
ORDER BY 3 ASC, 2 ASC