-- Insertar datos en la tabla users
INSERT INTO ecommerce_dataset.users (user_id, name, email)
VALUES
    (1, 'Alice Johnson', 'alice.johnson@example.com'),
    (2, 'Bob Smith', 'bob.smith@example.com'),
    (3, 'Charlie Brown', 'charlie.brown@example.com');

-- Insertar datos en la tabla orders
INSERT INTO ecommerce_dataset.orders (order_id, user_id, product, price)
VALUES
    (101, 1, 'Laptop', 1200.50),
    (102, 1, 'Mouse', 25.75),
    (103, 2, 'Keyboard', 45.00),
    (104, 3, 'Monitor', 300.00),
    (105, 2, 'USB Cable', 10.00);