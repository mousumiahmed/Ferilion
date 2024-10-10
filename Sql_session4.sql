-- Create the 'sales' table
use B1213;
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    sale_date DATE,
    customer_name VARCHAR(100)
);

-- Insert sample data into the 'sales' table
INSERT INTO sales (product_id, quantity, price, sale_date, customer_name) VALUES
(1, 10, 19.99, '2024-01-01', 'John Doe'),
(2, 5, 49.99, '2024-01-02', 'Jane Smith'),
(3, 2, 99.99, '2024-01-03', 'Emily Johnson'),
(1, 1, 19.99, '2024-01-04', 'Chris Lee'),
(2, 3, 49.99, '2024-01-05', 'Michael Brown');

-- Arithmetic Operators

-- Addition
-- Add 10 to the quantity of all sales
SELECT sale_id, quantity + 10 AS new_quantity
FROM sales;

select sale_id, quantity from sales;
select 2+3;

-- Subtraction
-- Subtract 5 from the quantity of all sales
SELECT sale_id, quantity - 5 AS new_quantity
FROM sales;

use demo;
select * from emp;
select *, round((sal*110)/100)from emp;

-- Multiplication
-- Multiply the price by 2
SELECT sale_id, price * 2 AS new_price
FROM sales;

-- Division
-- Divide the price by 2
SELECT sale_id, round(price / 2) AS new_price
FROM sales;

-- Modulus
-- Find the remainder when quantity is divided by 2
SELECT sale_id, quantity % 2 AS remainder
FROM sales;

-- Comparison Operators

-- Equal to
-- Find sales where the quantity is exactly 10
SELECT * FROM sales WHERE quantity = 10;

-- Not equal to
-- Find sales where the quantity is not 10
SELECT * FROM sales WHERE quantity <> 10;

-- Greater than
-- Find sales where the price is greater than 20
SELECT * FROM sales WHERE price > 20;

-- Less than
-- Find sales where the price is less than 50
SELECT * FROM sales WHERE price < 50;

-- Greater than or equal to
-- Find sales where the quantity is greater than or equal to 5
SELECT * FROM sales WHERE quantity >= 5;

-- Less than or equal to
-- Find sales where the quantity is less than or equal to 3
SELECT * FROM sales WHERE quantity <= 3;

-- BETWEEN
-- Find sales made between '2024-01-01' and '2024-01-03'
SELECT * FROM sales WHERE sale_date not BETWEEN '2024-01-01' AND '2024-01-03';

-- Not Between

-- IN
-- Find sales made to customers named 'John Doe' or 'Jane Smith'
SELECT * FROM sales WHERE customer_name IN ('John Doe', 'Jane Smith');

-- Like 
select * from sales
where customer_name like '_o%';

select * from sales
where customer_name not like 'J%';
-- Logical Operators

-- AND
-- Find sales where the quantity is greater than 2 and the price is less than 50
SELECT * FROM sales WHERE quantity > 2 AND price < 50;

-- OR
-- Find sales where the quantity is greater than 5 or the price is greater than 50
SELECT * FROM sales WHERE quantity > 5 OR price > 50;

-- NOT
-- Find sales where the customer name is not 'John Doe'
SELECT * FROM sales WHERE NOT customer_name = 'John Doe';

-- Bitwise Operators

-- Bitwise AND
-- Perform a bitwise AND between the quantity and 1
SELECT  quantity,sale_id, quantity & 1 AS bitwise_and
FROM sales;

select 10 & 1;
-- Bitwise OR
-- Perform a bitwise OR between the quantity and 1
SELECT sale_id, quantity | 1 AS bitwise_or
FROM sales;

-- Bitwise XOR
-- Perform a bitwise XOR between the quantity and 1
SELECT sale_id, quantity ^ 1 AS bitwise_xor
FROM sales;

-- Bitwise NOT
-- Perform a bitwise NOT on the quantity
SELECT sale_id, ~quantity AS bitwise_not
FROM sales;

select ~5;
-- Bitwise Shift Left
-- Shift the quantity to the left by 1 bit
SELECT sale_id, quantity << 1 AS shift_left
FROM sales;

-- Bitwise Shift Right
-- Shift the quantity to the right by 1 bit
SELECT sale_id, quantity >> 1 AS shift_right
FROM sales;

-- String Operators

-- Concatenation
-- Concatenate 'Sale: ' with the sale_id
SELECT CONCAT(customer_name, sale_id) AS sale_identifier
FROM sales; 

select concat_ws('-',15,7,2024);
group_concat(col1,col2) - > Aggregate functions

-- LIKE
-- Find sales where the customer name starts with 'J'
SELECT * FROM sales WHERE customer_name LIKE 'J%';

-- NOT LIKE
-- Find sales where the customer name does not start with 'J'
SELECT * FROM sales WHERE customer_name NOT LIKE 'J%';

-- Miscellaneous Operators

-- CASE
-- Categorize sales based on quantity
SELECT sale_id,
       CASE
           WHEN quantity >= 10 THEN 'Large Order'
           WHEN quantity >= 5 THEN 'Medium Order'
           ELSE 'Small Order'
       END case_sate
FROM sales;

-- Subquery Example
-- Find sales where the price is greater than the average price
SELECT * FROM sales
WHERE price > (
    SELECT AVG(price) FROM sales
);

-- Explanation:
-- Arithmetic Operators: Used for basic mathematical operations.
-- Comparison Operators: Used to compare two values.
-- Logical Operators: Used to combine multiple conditions.
-- Bitwise Operators: Used to perform bit-level operations.
-- String Operators: Used to manipulate string values.
-- Miscellaneous Operators: Various other operators like CASE for conditional logic.
-- Subquery Example: Uses a subquery to compare the price with the average price.


use demo;
select * from emp;

select * from emp
where sal >(select max(sal) from emp
where deptno = 20);

select * from emp
where sal>(select min(sal) from emp
where deptno = 20);

