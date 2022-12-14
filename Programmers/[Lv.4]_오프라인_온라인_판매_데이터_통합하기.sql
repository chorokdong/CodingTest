-- https://school.programmers.co.kr/learn/courses/30/lessons/131537


SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID,USER_ID, SALES_AMOUNT 
from ONLINE_SALE
where SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
union all
select DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
from OFFLINE_SALE
where SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc