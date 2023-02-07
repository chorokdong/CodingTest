-- https://school.programmers.co.kr/learn/courses/30/lessons/151137

SELECT car_type, COUNT(1) AS CARS
FROM car_rental_company_car
WHERE options REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY 1
ORDER BY 1


# SELECT car_type, COUNT(1) AS CARS
# FROM car_rental_company_car
# WHERE options like '%통풍시트%' OR
#       options like '%열선시트%' OR
#       options like '%가죽시트%'
# GROUP BY 1
# ORDER BY 1
