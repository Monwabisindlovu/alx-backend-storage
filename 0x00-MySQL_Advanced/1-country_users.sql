-- Create table users with specified attributes, including an enumeration for 'country'
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- id, integer, never null, auto increment and primary key
    email VARCHAR(255) NOT NULL UNIQUE,     -- email, string (255 characters), never null and unique
    name VARCHAR(255),                      -- name, string (255 characters)
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'  -- country, enumeration of countries: US, CO, and TN, never null
);

