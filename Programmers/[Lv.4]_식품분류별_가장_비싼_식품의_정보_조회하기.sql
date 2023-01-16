-- https://school.programmers.co.kr/learn/courses/30/lessons/131116

SELECT category, price, product_name
FROM food_product
WHERE (category,price) in 
        (SELECT category, max(price)
         FROM food_product
         WHERE category in ('과자','국','김치','식용유')
         GROUP BY 1)
ORDER BY 2 DESC

-- [Rank() OVER 함수 사용]
-- SELECT RANK( ) OVER ( PARTITION BY 그룹핑할 칼럼 ORDER BY 정렬할 칼럼 )
-- FROM 테이블명

SELECT category, price, product_name
FROM (
      SELECT *, RANK() OVER(PARTITION BY category
                            ORDER BY price desc) AS pr
      FROM food_product
      WHERE category in ('과자','국','김치','식용유')
     ) AS product
WHERE product.pr = 1
ORDER BY 2 DESC
