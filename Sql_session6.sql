-- Aggregate Functions in MySQL

-- Introduction
-- Aggregate functions in MySQL perform a calculation on a set of values and return a single value.
-- Common aggregate functions include COUNT, SUM, AVG, MAX, and MIN, group_concat etc

-- Syntax
-- The basic syntax of aggregate functions is:

/*
SELECT aggregate_function(column)
FROM table_name
[WHERE condition];
*/

-- Example 1: Using COUNT to Count Rows

-- Tables:
-- employees: id, name, salary, department_id

-- Query: Count the total number of employees.
SELECT COUNT(*) AS total_employees
FROM employees;

-- Explanation:
-- 1. Uses the COUNT(*) function to count all rows in the employees table.
-- 2. Returns the total number of employees.

-- Example 2: Using SUM to Calculate Total Values

-- Query: Calculate the total salary of all employees.
SELECT SUM(salary) AS total_salary
FROM employees;

-- Explanation:
-- 1. Uses the SUM(salary) function to calculate the sum of all salaries in the employees table.
-- 2. Returns the total salary of all employees.

-- Example 3: Using AVG to Calculate Average Values

-- Query: Calculate the average salary of all employees.
SELECT AVG(salary) AS average_salary
FROM employees;

-- Explanation:
-- 1. Uses the AVG(salary) function to calculate the average salary in the employees table.
-- 2. Returns the average salary of all employees.

-- Example 4: Using MAX to Find the Maximum Value

-- Query: Find the highest salary among all employees.
SELECT MAX(salary) AS highest_salary
FROM employees;

-- Explanation:
-- 1. Uses the MAX(salary) function to find the highest salary in the employees table.
-- 2. Returns the highest salary.

-- Example 5: Using MIN to Find the Minimum Value

-- Query: Find the lowest salary among all employees.
SELECT MIN(salary) AS lowest_salary
FROM employees;

-- Explanation:
-- 1. Uses the MIN(salary) function to find the lowest salary in the employees table.
-- 2. Returns the lowest salary.

-- Example 6: Using Aggregate Functions with GROUP BY

-- Query: Calculate the total salary for each department.
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id;

-- Explanation:
-- 1. Selects department_id and the sum of salaries from the employees table.
-- 2. Groups the result by department_id, so the total salary is calculated for each department.

-- Example 7: Combining Aggregate Functions and HAVING

-- Query: Calculate the total salary for each department and show only departments with a total salary greater than 100,000.
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
HAVING total_salary > 100000;

-- Explanation:
-- 1. Selects department_id and the sum of salaries from the employees table.
-- 2. Groups the result by department_id.
-- 3. Filters the groups to include only those with a total_salary greater than 100,000.

-- Example 8: Using COUNT with DISTINCT

-- Query: Count the number of distinct departments.
SELECT COUNT(DISTINCT department_id) AS total_departments
FROM employees;

-- Explanation:
-- 1. Uses the COUNT(DISTINCT department_id) function to count the number of unique department_ids in the employees table.
-- 2. Returns the total number of distinct departments.

-- Summary
-- Aggregate functions such as COUNT, SUM, AVG, MAX, and MIN are used to perform calculations on sets of values and return single values.
-- They can be used with GROUP BY to aggregate data based on specific columns, and with HAVING to filter aggregated results.
-- By understanding and using aggregate functions, you can effectively summarize and analyze your data in MySQL.

/*
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    permissions INT
);

INSERT INTO users (id, name, permissions) VALUES
(1, 'Alice', 3), -- Read and Write (0011)
(2, 'Bob', 5),   -- Read and Execute (0101)
(3, 'Charlie', 7); -- Read, Write, and Execute (0111)

SELECT BIT_AND(permissions) & 1 FROM users;
-- Result: 1 (indicating all users have read permission)

SELECT BIT_OR(permissions) FROM users;
-- Result: 7 (indicating at least one user has Read, Write, and Execute permissions)

*/


-- Comparison Functions in MySQL

-- Introduction
-- Comparison functions in MySQL are used to perform operations on values and return specific results based on the comparison.
-- Common comparison functions include COALESCE, GREATEST, LEAST, and ISNULL.

-- COALESCE Function
-- The COALESCE function returns the first non-NULL value in a list of arguments.

-- Syntax
-- COALESCE(value1, value2, ..., value_n)

-- Example 1: Using COALESCE

-- Tables:
-- employees: id, name, salary, commission

-- Query: Select the name and compensation (salary + commission), using 0 if commission is NULL.
SELECT name, salary + COALESCE(commission, 0) AS compensation
FROM employees;

-- Explanation:
-- 1. Uses the COALESCE function to return the commission if it is not NULL.
-- 2. If the commission is NULL, it returns 0.
-- 3. Adds the salary to the result of COALESCE to calculate the total compensation.

-- GREATEST Function
-- The GREATEST function returns the greatest value from a list of arguments.

-- Syntax
-- GREATEST(value1, value2, ..., value_n)

-- Example 2: Using GREATEST

-- Tables:
-- products: id, price1, price2, price3

-- Query: Select the product ID and the highest price among three price columns.
SELECT id, GREATEST(price1, price2, price3) AS highest_price
FROM products;

-- Explanation:
-- 1. Uses the GREATEST function to return the highest value among price1, price2, and price3.
-- 2. Returns the product ID and the highest price for each product.

-- LEAST Function
-- The LEAST function returns the smallest value from a list of arguments.

-- Syntax
-- LEAST(value1, value2, ..., value_n)

-- Example 3: Using LEAST

-- Tables:
-- products: id, price1, price2, price3

-- Query: Select the product ID and the lowest price among three price columns.
SELECT id, LEAST(price1, price2, price3) AS lowest_price
FROM products;

-- Explanation:
-- 1. Uses the LEAST function to return the lowest value among price1, price2, and price3.
-- 2. Returns the product ID and the lowest price for each product.

-- ISNULL Function
-- The ISNULL function returns 1 if the argument is NULL, otherwise, it returns 0.

-- Syntax
-- ISNULL(expression)

-- Example 4: Using ISNULL

-- Tables:
-- employees: id, name, salary, commission

-- Query: Select the name and a flag indicating whether the commission is NULL.
SELECT name, ISNULL(commission) AS commission_is_null
FROM employees;

-- Explanation:
-- 1. Uses the ISNULL function to check if the commission is NULL.
-- 2. Returns the name and 1 if the commission is NULL, otherwise returns 0.

-- Additional Examples

-- Example 5: Using COALESCE with Multiple Columns

-- Tables:
-- customers: id, phone1, phone2

-- Query: Select the customer ID and the first non-NULL phone number.
SELECT id, COALESCE(phone1, phone2) AS contact_number
FROM customers;

-- Explanation:
-- 1. Uses the COALESCE function to return the first non-NULL phone number (phone1 or phone2).
-- 2. Returns the customer ID and the contact number.

-- Example 6: Using GREATEST and LEAST with Dates

-- Tables:
-- projects: id, start_date, end_date, review_date

-- Query: Select the project ID, the earliest, and the latest date among three date columns.
SELECT id, LEAST(start_date, end_date, review_date) AS earliest_date, GREATEST(start_date, end_date, review_date) AS latest_date
FROM projects;

-- Explanation:
-- 1. Uses the LEAST function to return the earliest date among start_date, end_date, and review_date.
-- 2. Uses the GREATEST function to return the latest date among start_date, end_date, and review_date.
-- 3. Returns the project ID, earliest date, and latest date.

-- Summary
-- Comparison functions such as COALESCE, GREATEST, LEAST, and ISNULL are used to perform specific comparisons and return results based on those comparisons.
-- COALESCE returns the first non-NULL value in a list of arguments.
-- GREATEST returns the greatest value from a list of arguments.
-- LEAST returns the smallest value from a list of arguments.
-- ISNULL returns 1 if the argument is NULL, otherwise, it returns 0.


-- Control Flow Functions in MySQL

-- Introduction
-- The control flow functions allow you to add if-then-else logic to SQL queries without using procedural code.
-- Common control flow functions include CASE, IF, IFNULL, and NULLIF.

-- CASE Function
-- The CASE function returns the corresponding result in the THEN branch if the condition in the WHEN branch is satisfied, otherwise, it returns the result in the ELSE branch.

-- Syntax
-- CASE
--     WHEN condition1 THEN result1
--     WHEN condition2 THEN result2
--     ...
--     ELSE result
-- END

-- Example 1: Using CASE

-- Tables:
-- employees: id, name, salary

-- Query: Select the name and salary grade based on salary ranges.
SELECT name,
    CASE
        WHEN salary < 30000 THEN 'Low'
        WHEN salary BETWEEN 30000 AND 60000 THEN 'Medium'
        ELSE 'High'
    END AS salary_grade
FROM employees;

-- Explanation:
-- 1. Uses the CASE function to evaluate the salary column.
-- 2. Returns 'Low' if the salary is less than 30000, 'Medium' if it is between 30000 and 60000, and 'High' otherwise.
-- 3. Returns the name and the calculated salary_grade.

-- IF Function
-- The IF function returns a value based on a given condition.

-- Syntax
-- IF(condition, value_if_true, value_if_false)

-- Example 2: Using IF

-- Tables:
-- employees: id, name, salary

-- Query: Select the name and a flag indicating whether the salary is above 50000.
SELECT name,
    IF(salary > 50000, 'Above 50000', '50000 or Below') AS salary_flag
FROM employees;

-- Explanation:
-- 1. Uses the IF function to evaluate the salary column.
-- 2. Returns 'Above 50000' if the salary is greater than 50000, otherwise returns '50000 or Below'.
-- 3. Returns the name and the calculated salary_flag.

-- IFNULL Function
-- The IFNULL function returns the first argument if it is not NULL, otherwise it returns the second argument.

-- Syntax
-- IFNULL(expression1, expression2)

-- Example 3: Using IFNULL

-- Tables:
-- employees: id, name, salary, commission

-- Query: Select the name and compensation (salary + commission), using 0 if commission is NULL.
SELECT name, salary + IFNULL(commission, 0) AS compensation
FROM employees;

-- Explanation:
-- 1. Uses the IFNULL function to return the commission if it is not NULL.
-- 2. If the commission is NULL, it returns 0.
-- 3. Adds the salary to the result of IFNULL to calculate the total compensation.

-- NULLIF Function
-- The NULLIF function returns NULL if the first argument is equal to the second argument, otherwise it returns the first argument.

-- Syntax
-- NULLIF(expression1, expression2)

-- Example 4: Using NULLIF

-- Tables:
-- employees: id, name, salary, bonus

-- Query: Select the name and adjusted bonus (nullify bonus if it is zero).
SELECT name, NULLIF(bonus, 0) AS adjusted_bonus
FROM employees;

-- Explanation:
-- 1. Uses the NULLIF function to compare the bonus column with the value 0.
-- 2. Returns NULL if the bonus is 0, otherwise returns the bonus value.
-- 3. Returns the name and the adjusted_bonus.

-- Additional Examples

-- Example 5: Using CASE with Multiple Conditions

-- Tables:
-- orders: id, order_date, amount

-- Query: Select the order ID, order date, and order status based on amount ranges.
SELECT id, order_date,
    CASE
        WHEN amount < 100 THEN 'Small'
        WHEN amount BETWEEN 100 AND 500 THEN 'Medium'
        ELSE 'Large'
    END AS order_status
FROM orders;

-- Explanation:
-- 1. Uses the CASE function to evaluate the amount column.
-- 2. Returns 'Small' if the amount is less than 100, 'Medium' if it is between 100 and 500, and 'Large' otherwise.
-- 3. Returns the order ID, order date, and the calculated order_status.

-- Example 6: Using IF with Nested Conditions

-- Tables:
-- students: id, name, score

-- Query: Select the name and result based on score.
SELECT name,
    IF(score >= 60, 'Pass', 'Fail') AS result
FROM students;

-- Explanation:
-- 1. Uses the IF function to evaluate the score column.
-- 2. Returns 'Pass' if the score is greater than or equal to 60, otherwise returns 'Fail'.
-- 3. Returns the name and the calculated result.

-- Example 7: Using IFNULL with Default Values

-- Tables:
-- customers: id, phone1, phone2

-- Query: Select the customer ID and the first non-NULL phone number.
SELECT id, IFNULL(phone1, phone2) AS contact_number
FROM customers;

-- Explanation:
-- 1. Uses the IFNULL function to return the first non-NULL phone number (phone1 or phone2).
-- 2. Returns the customer ID and the contact number.

-- Example 8: Using NULLIF with Conditional Defaults

-- Tables:
-- sales: id, amount, discount

-- Query: Select the sale ID and adjusted discount (nullify discount if it is zero).
SELECT id, NULLIF(discount, 0) AS adjusted_discount
FROM sales;

-- Explanation:
-- 1. Uses the NULLIF function to compare the discount column with the value 0.
-- 2. Returns NULL if the discount is 0, otherwise returns the discount value.
-- 3. Returns the sale ID and the adjusted_discount.

-- Summary
-- Control flow functions such as CASE, IF, IFNULL, and NULLIF are used to add if-then-else logic to SQL queries.
-- CASE returns the corresponding result in the THEN branch if the condition in the WHEN branch is satisfied, otherwise, it returns the result in the ELSE branch.
-- IF returns a value based on a given condition.
-- IFNULL returns the first argument if it is not NULL, otherwise it returns the second argument.
-- NULLIF returns NULL if the first argument is equal to the second argument, otherwise it returns the first argument.


select bit_or(sal) from emp;

select sal from emp;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    permissions INT
);

INSERT INTO users (id, name, permissions) VALUES
(1, 'Alice', 3), -- Read and Write (0011)  
(2, 'Bob', 5),   -- Read and Execute (0101)
(3, 'Charlie', 7); -- Read, Write, and Execute (0111)

SELECT BIT_AND(permissions)&1 FROM users;  
-- Result: 1 (indicating all users have read permission)

SELECT BIT_OR(permissions) FROM users;
-- Result: 7 (indicating at least one user has Read, Write, and Execute permissions)

select ename from emp;

select group_concat(ename) from emp;

select json_arrayagg(ename) from emp;

select json_objectagg(empno,ename) from emp;

select stddev(sal) from emp;

select sal,comm from emp;

select greatest(sal,comm) from emp;

select least(sal,comm) from emp;	

select coalesce(null,null,null,2,1);

select coalesce(comm,(select avg(sal) from emp)) from emp;

select isnull(comm) from emp;


/* comprison function
greatest 
least
coalesce
isnull
*/

/*
COntrol flow functions
*/

-- select *,
-- case
-- 	when sal<1000 then 'least'
--     when sal>1500 then 'greatest'
--     else 'okok'
-- end as sal_description
-- from emp;

select *, if(job = 'clerk', 'Earning_comm','not_eqarning_comm')as comm_descrtp from emp;
-- if (condition,true,false)

select *, ifnull(comm, 100) from emp;

select nullif(10,2);

select nullif(10,10);


