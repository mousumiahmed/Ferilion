-- Correlated Subqueries in MySQL

-- Introduction
-- A correlated subquery is a subquery that uses values from the outer query.
-- Unlike a regular subquery, a correlated subquery is executed repeatedly,
-- once for each row processed by the outer query. This can make correlated subqueries
-- more complex and potentially less efficient.

-- Syntax
-- The basic syntax of a correlated subquery is:

-- SELECT column1, column2, ...
-- FROM outer_table
-- WHERE column1 operator (SELECT column1
--                         FROM inner_table
--                         WHERE outer_table.column2 = inner_table.column2);

-- Example 1: Finding Employees with Above-Average Salaries in their department

-- Tables:
-- employees: id, name, salary, department_id
-- departments: id, name

-- Query
SELECT e.name, e.salary, e.department_id
FROM employees e
WHERE e.salary > (SELECT AVG(e2.salary)
                  FROM employees e2
                  WHERE e2.department_id = e.department_id);

-- Explanation:
-- 1. Outer Query: Selects name, salary, and department_id from employees.
-- 2. Inner Query: Calculates the average salary for the department of the current employee in the outer query.
-- 3. Correlation: The inner query references e.department_id from the outer query.
--    For each employee in the outer query, the inner query recalculates the average salary for that employee's department.

-- Execution Order Diagram:
-- 1. Outer Query (first row) -> employees
-- 2. Inner Query -> employees
--    - Correlated on department_id
-- 3. Compare salary > AVG(salary)
-- 4. Outer Query (next row) -> repeat

-- Example 2: Finding Products Priced Above the Average in Their Category

-- Tables:
-- products: id, name, price, category_id
-- categories: id, name

-- Query
SELECT p.name, p.price, p.category_id
FROM products p
WHERE p.price > (SELECT AVG(p2.price)
                 FROM products p2
                 WHERE p2.category_id = p.category_id);

-- Explanation:
-- 1. Outer Query: Selects name, price, and category_id from products.
-- 2. Inner Query: Calculates the average price for the category of the current product in the outer query.
-- 3. Correlation: The inner query references p.category_id from the outer query.
--    For each product in the outer query, the inner query recalculates the average price for that product's category.

-- Execution Order Diagram:
-- 1. Outer Query (first row) -> products
-- 2. Inner Query -> products
--    - Correlated on category_id
-- 3. Compare price > AVG(price)
-- 4. Outer Query (next row) -> repeat

-- Example of Optimization Using JOIN
-- The above example can be rewritten using a join:

SELECT p.name, p.price, p.category_id
FROM products p
JOIN (
    SELECT category_id, AVG(price) AS avg_price
    FROM products
    GROUP BY category_id
) cat_avg
ON p.category_id = cat_avg.category_id
WHERE p.price > cat_avg.avg_price;

-- Explanation:
-- 1. Derived Table: The subquery calculates the average price for each category and returns a derived table cat_avg.
-- 2. Join: The outer query joins the products table with the cat_avg derived table on category_id.
-- 3. Filter: The outer query filters products whose price is greater than the average price for their category.

-- Additional Examples

-- Example 3: Finding Students with Scores Above the Class Average

-- Tables:
-- students: id, name, score, class_id
-- classes: id, name

-- Query
SELECT s.name, s.score, s.class_id
FROM students s
WHERE s.score > (SELECT AVG(s2.score)
                 FROM students s2
                 WHERE s2.class_id = s.class_id);

SELECT s.name, s.score, s.class_id
FROM students s join(
select class_id, avg(score) average from students
group by class_id) as avg_score
on s.class_id = avg_score.class_id
where s.score > avg_score.average;

-- Execution Order Diagram:
-- 1. Outer Query (first row) -> students
-- 2. Inner Query -> students
--    - Correlated on class_id
-- 3. Compare score > AVG(score)
-- 4. Outer Query (next row) -> repeat

-- Example 4: Finding Orders Above the Average Value Per Customer

-- Tables:
-- orders: id, customer_id, order_value
-- customers: id, name

select o.id, o.customer_id, o.order_value from orders o
where o.order_value > (select avg(o2.order_value) from orders o2
where o.customer_id = o2.customer_id);

select o.id, o.customer_id, o.order_value from orders o
join(
select customer_id, avg(order_value) average from orders
group by customer_id) as avg_order
on o.customer_id = avg_order.custoer_id
where o.order_value > avg_order.average;



-- Query
SELECT o.id, o.order_value, o.customer_id
FROM orders o
WHERE o.order_value > (SELECT AVG(o2.order_value)
                       FROM orders o2
                       WHERE o2.customer_id = o.customer_id);

-- Execution Order Diagram:
-- 1. Outer Query (first row) -> orders
-- 2. Inner Query -> orders
--    - Correlated on customer_id
-- 3. Compare order_value > AVG(order_value)
-- 4. Outer Query (next row) -> repeat

-- Summary
-- Correlated subqueries are powerful tools for row-wise comparisons but can be less efficient due to repeated execution.
-- By understanding their structure and considering performance optimizations like indexing and query rewriting,
-- you can effectively use correlated subqueries in your MySQL queries.

-- details of the employees with above average salary of their department
select e1.ename, e1.sal, e1.deptno from emp e1
where e1.sal>(select avg(e2.sal) from emp e2
where e2.deptno = e1.deptno);

select deptno, avg(sal) from emp
group by deptno;

select e1.ename, e1.sal, e1.deptno from emp e1
join(
select deptno, avg(sal) average from emp
group by deptno)
avg_sal
on e1.deptno = avg_sal.deptno
where e1.sal>avg_sal.average;

SELECT p.name, p.price, p.category_id
FROM products p
JOIN (
    SELECT category_id, AVG(price) AS avg_price
    FROM products
    GROUP BY category_id
) cat_avg
ON p.category_id = cat_avg.category_id
WHERE p.price > cat_avg.avg_price;

select distinct deptno from emp;

select * from emp;

-- employees details who has hired before their own department manager
-- employee with manager 


use demo;
select avg(sal) from emp
where deptno = 30;

select * from emp
where sal > any(select sal from emp
where deptno = 30);

select min(sal) from emp
where deptno = 30;

select * from emp e1
where sal > (select avg(sal) from emp
where emp.deptno = e1.deptno);


use classicmodels;
