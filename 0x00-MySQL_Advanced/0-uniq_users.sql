-- Task: Create a 'users' table with specific attributes
-- This table will store user information including id, email, and name.
-- The 'id' is a primary key and auto-incremented, while 'email' is unique and cannot be null.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- Auto-incremented unique ID
    email VARCHAR(255) NOT NULL UNIQUE,         -- Email, unique and not null
    name VARCHAR(255)                           -- Name, can be null
);
