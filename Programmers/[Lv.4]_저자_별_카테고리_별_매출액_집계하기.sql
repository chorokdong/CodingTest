-- https://school.programmers.co.kr/learn/courses/30/lessons/144856


SELECT book.author_id, author.author_name, book.category, 
        sum(book.price * book_sales.sales) AS total_sales
FROM book_sales 
LEFT JOIN book ON book_sales.book_id = book.book_id
LEFT JOIN author ON book.author_id = author.author_id 
WHERE DATE_FORMAT(book_sales.sales_date, '%Y-%m') = '2022-01'
GROUP BY 1,3
ORDER BY 1 ASC, 3 DESC