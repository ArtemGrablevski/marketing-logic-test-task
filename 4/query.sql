SELECT 
	TO_CHAR(date, 'DD.MM') AS date,
	COUNT(order_id) AS orders_amount,
	(SELECT COUNT(user_id) AS users_amount FROM (SELECT user_id FROM orders o2 WHERE o1.date = o2.date GROUP BY user_id) subquery),
	SUM(price) as orders_sum
FROM orders o1
GROUP BY date
ORDER BY date;
