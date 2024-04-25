-- Task: Create a table 'users' with attributes 'id', 'email', and 'name'
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(id)
);

