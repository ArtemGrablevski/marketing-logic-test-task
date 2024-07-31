## SQL запрос для выборки данных

### Код для создания таблицы в базе данных и заполнения ее начальными данными:
```sql
CREATE TABLE orders (
    date DATE,
    order_id SERIAL PRIMARY KEY,
    user_id INT,
    price NUMERIC
);

INSERT INTO orders (date, order_id, user_id, price) VALUES
    ('2024-01-01', 1, 1, 5),
    ('2024-01-01', 2, 1, 10),
    ('2024-01-01', 3, 2, 5),
    ('2024-01-01', 4, 3, 5),
    ('2024-01-01', 5, 1, 5),
    ('2024-01-02', 6, 1, 5),
    ('2024-01-02', 7, 2, 10),
    ('2024-01-02', 8, 3, 5),
    ('2024-01-03', 9, 3, 5),
    ('2024-01-03', 10, 3, 5);
```

### SQL запрос для получения необходимой выборки:
```sql
SELECT 
	TO_CHAR(date, 'DD.MM') AS date,
	COUNT(order_id) AS orders_amount,
	(
        SELECT COUNT(user_id) AS users_amount FROM 
        (SELECT user_id FROM orders o2 WHERE o1.date = o2.date GROUP BY user_id) subquery
    ),
	SUM(price) as orders_sum
FROM orders o1
GROUP BY date
ORDER BY date;
```