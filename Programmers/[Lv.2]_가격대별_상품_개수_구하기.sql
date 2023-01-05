---- https://school.programmers.co.kr/learn/courses/30/lessons/131530
---- 가격대별 상품 개수 구하기

SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, COUNT(PRODUCT_ID)
FROM product
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP