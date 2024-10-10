-- GROUP BY and HAVING Clauses in MySQL

-- Introduction
-- The GROUP BY clause is used to group rows that have the same values in specified columns into summary rows.
-- The HAVING clause is used to filter records that work on summarized GROUP BY results.

-- Syntax
-- The basic syntax of GROUP BY is:

-- SELECT column1, aggregate_function(column2)
-- FROM table_name
-- GROUP BY column1;

-- The basic syntax of HAVING is:

-- SELECT column1, aggregate_function(column2)
-- FROM table_name
-- GROUP BY column1
-- HAVING condition;

-- Example 1: Using GROUP BY to Group Data

-- Tables:
-- sales: id, product_id, quantity, sale_date
-- products: id, name, category

-- Query: Group sales by product and calculate the total quantity sold for each product.
SELECT product_id, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id;

-- Explanation:
-- 1. Selects product_id and the sum of quantity from the sales table.
-- 2. Groups the result by product_id, so the total quantity is calculated for each product.

-- Example 2: Using HAVING to Filter Groups

-- Query: Group sales by product and filter to show only products with total sales quantity greater than 100.
SELECT product_id, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id
HAVING total_quantity > 100;

-- Explanation:
-- 1. Selects product_id and the sum of quantity from the sales table.
-- 2. Groups the result by product_id, so the total quantity is calculated for each product.
-- 3. Filters the groups to include only those with total_quantity greater than 100.

-- Example 3: Grouping by Multiple Columns

-- Query: Group sales by product and sale_date, and calculate the total quantity sold for each group.
SELECT product_id, sale_date, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id, sale_date;

-- Explanation:
-- 1. Selects product_id, sale_date, and the sum of quantity from the sales table.
-- 2. Groups the result by both product_id and sale_date, so the total quantity is calculated for each product on each sale_date.

-- Example 4: Using HAVING with Multiple Conditions

-- Query: Group sales by product and filter to show products with total sales quantity greater than 100 and less than 500.
SELECT product_id, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id
HAVING total_quantity > 100 AND total_quantity < 500;

-- Explanation:
-- 1. Selects product_id and the sum of quantity from the sales table.
-- 2. Groups the result by product_id.
-- 3. Filters the groups to include only those with total_quantity greater than 100 and less than 500.


-- Example 6: Combining GROUP BY and HAVING with Aggregate Functions

-- Query: Group sales by product and calculate the average quantity sold for each product. Filter to show only products with an average quantity greater than 10.
SELECT product_id, AVG(quantity) AS average_quantity
FROM sales
GROUP BY product_id
HAVING average_quantity > 10;

-- Explanation:
-- 1. Selects product_id and the average of quantity from the sales table.
-- 2. Groups the result by product_id.
-- 3. Filters the groups to include only those with an average_quantity greater than 10.

-- Summary
-- The GROUP BY clause is used to group rows that have the same values into summary rows, like "total quantity sold per product".
-- The HAVING clause is used to filter groups based on aggregate calculations, like "products with total sales quantity greater than 100".
-- By using GROUP BY and HAVING, you can create powerful queries that summarize and filter data in various ways.


/*
1. from
2. where 
3. group by
4. having
5. select
*/

/*
Aggregate/ Multi_row_function / Group by functions :
*/
-- 14:44:15	select * from emp group by deptno LIMIT 0, 1000	Error Code: 1055. Expression #1 of 
-- SELECT list is not in GROUP BY clause and contains nonaggregated column 'demo.emp.empno' 
-- which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by	0.015 sec


select * from emp;

select deptno,max(sal) from emp
group by deptno;

select ename,deptno,max(sal) from emp
group by deptno,ename;

--  whose name has char 'A' and earns sal more than 1000 in each dept
select deptno from emp
where ename like '%A%' and sal > 1000
group by deptno;

-- departments which contains atlest 4 employees
select deptno, count(empno) from emp
group by deptno
having count(empno)>=4;

-- select * from emp
-- limit 3;

select * from emp;
-- What is the average sales amount per category, excluding categories with less than 3 products sold?
-- column_names --> sales_amount , category, product_id
-- select avg(sales_amount),category  from abc
-- group by category
-- having count(produt_id)>=3;

select * from emp;

select avg(sal),deptno from emp
group by deptno
having avg(sal) > 1000 and count(empno)>=4;

