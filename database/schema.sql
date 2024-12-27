CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    brand TEXT,
    specifications JSONB
);

CREATE TABLE deals (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    price DECIMAL NOT NULL,
    retailer TEXT NOT NULL,
    url TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
