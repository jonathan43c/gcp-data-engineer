SELECT name, COUNT(order_id) AS total_pedidos, SUM(price) AS total_gastado
FROM ecommerce_dataset.orders_with_users
GROUP BY name
ORDER BY total_gastado DESC;