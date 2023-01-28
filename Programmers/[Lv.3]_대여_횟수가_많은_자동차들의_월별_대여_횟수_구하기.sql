-- https://school.programmers.co.kr/learn/courses/30/lessons/151139#

SELECT MONTH(start_date), car_id, COUNT(1) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id in ( 
    SELECT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE DATE_FORMAT(start_date, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    GROUP BY 1
    HAVING COUNT(1) >= 5) AND DATE_FORMAT(start_date, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
GROUP BY 1,2
ORDER BY 1 ASC, 2 DESC