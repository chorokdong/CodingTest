-- https://school.programmers.co.kr/learn/courses/30/lessons/131534

SELECT YEAR(sales_date) AS YEAR, 
       MONTH(sales_date) AS MONTH,  
       COUNT(DISTINCT(os.user_id)) AS PUCHASED_USERS, 
       ROUND(COUNT(DISTINCT(os.user_id)) / (SELECT COUNT(*)
                                            FROM user_info
                                            WHERE YEAR(joined) = 2021),1) AS PUCHASED_RATIO
FROM online_sale AS os
INNER JOIN user_info AS ui ON ui.user_id = os.user_id
WHERE YEAR(joined) = 2021
GROUP BY 1,2
ORDER BY 1 ASC, 2 ASC