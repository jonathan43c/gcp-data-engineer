CREATE OR REPLACE VIEW ecommerce_dataset.orders_with_users AS
SELECT
    o.user_id,
    o.order_id,
    o.product,
    o.price,
    u.name,
    u.email
FROM ecommerce_dataset.orders o
JOIN ecommerce_dataset.users u
ON o.user_id = u.user_id;