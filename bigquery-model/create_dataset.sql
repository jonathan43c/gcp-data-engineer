-- Datos normalizados → más usado en bases de datos OLTP
-- Ejemplo: sistemas transaccionales como ventas, clientes, pedidos, pagos.

-- Datos desnormalizados → más usado en OLAP / analítica, como BigQuery
-- Ejemplo: tablas grandes para reportes, dashboards, KPIs, modelos estrella.

-- La idea simple:

-- Normalizado = menos duplicación, más tablas, más joins.
-- Bueno para registrar operaciones sin inconsistencias.

-- Desnormalizado = más duplicación controlada, menos joins, consultas más rápidas.
-- Bueno para análisis masivo en BigQuery.


CREATE SCHEMA ecommerce_dataset OPTIONS(locations="US");