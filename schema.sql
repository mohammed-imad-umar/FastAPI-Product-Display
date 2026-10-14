CREATE DATABASE IF NOT EXISTS product_store;
USE product_store;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO products (name, price)
SELECT 'Laptop', 70000.00
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'Laptop');

INSERT INTO products (name, price)
SELECT 'iPhone', 87000.00
WHERE NOT EXISTS (SELECT 1 FROM products WHERE name = 'iPhone');
