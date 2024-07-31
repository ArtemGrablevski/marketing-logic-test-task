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
