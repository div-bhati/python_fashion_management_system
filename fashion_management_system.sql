create database fashion_management_system;

use fashion_management_system;

CREATE TABLE IF NOT EXISTS Clothing (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    clothing_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (clothing_id) REFERENCES Clothing(id)
);



INSERT INTO Clothing (name, category, price, stock_quantity) VALUES
('T-Shirt', 'Apparel', 19.99, 50),
('Jeans', 'Apparel', 39.99, 30),
('Sneakers', 'Footwear', 49.99, 20),
('Dress', 'Apparel', 59.99, 15),
('Jacket', 'Outerwear', 79.99, 25),
('Cap', 'Accessories', 15.99, 100),
('Scarf', 'Accessories', 12.99, 80),
('Belt', 'Accessories', 22.99, 60);

INSERT INTO Customers (name, email, phone) VALUES
('Alice Johnson', 'alice.johnson@example.com', '555-1234'),
('Bob Smith', 'bob.smith@example.com', '555-5678'),
('Charlie Brown', 'charlie.brown@example.com', '555-8765'),
('Diana Prince', 'diana.prince@example.com', '555-4321'),
('Ethan Hunt', 'ethan.hunt@example.com', '555-9876');

INSERT INTO Orders (customer_id, clothing_id, quantity, order_date) VALUES
(1, 2, 1, '2024-10-01 10:00:00'),
(2, 1, 2, '2024-10-02 11:30:00'),
(3, 3, 1, '2024-10-03 12:45:00'),
(4, 4, 1, '2024-10-04 14:20:00'),
(5, 5, 1, '2024-10-05 16:15:00');
