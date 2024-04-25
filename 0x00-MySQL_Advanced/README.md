# 0x00. MySQL advanced

## Description
This repository contains MySQL advanced projects for the ALX Software Engineering program. Each task is a MySQL script file that fulfills specific requirements related to database management and optimization.

## Resources
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-procedures.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## Tasks

### 0. We are all unique!
Write a SQL script that creates a table `users` with specific attributes. If the table already exists, the script should not fail.

### 1. In and not out
Write a SQL script that creates a table `users` with specific attributes, including an enumeration of countries. If the table already exists, the script should not fail.

### 2. Best band ever!
Write a SQL script that ranks country origins of bands based on the number of fans.

### 3. Old school band
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.

### 4. Buy buy buy
Write a SQL script that creates a trigger to decrease the quantity of an item after adding a new order.

### 5. Email validation to sent
Write a SQL script that creates a trigger to reset the attribute `valid_email` only when the email has been changed.

### 6. Add bonus
Write a SQL script that creates a stored procedure `AddBonus` to add a new correction for a student.

### 7. Average score
Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student.

### 8. Optimize simple search
Write a SQL script that creates an index on the first letter of names for a table `names`.

### 9. Optimize search and score
Write a SQL script that creates an index on the first letter of names and scores for a table `names`.

### 10. Safe divide
Write a SQL script that creates a function `SafeDiv` to divide two numbers safely.

### 11. No table for a meeting
Write a SQL script that creates a view `need_meeting` to list students with a score under 80 and no last meeting or more than 1 month.

## Author
Created by [ALX](https://github.com/alx-backend-storage)


