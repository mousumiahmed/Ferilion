-- ================================================================
-- Types of Subqueries with Examples and Explanations
-- ================================================================

-- 1. Single-Row Subquery
-- This subquery returns a single row and is used with comparison operators.
-- Example: Find employees who work in the 'Sales' department.
SELECT employee_id, first_name, last_name
FROM employees
WHERE department_id = (
    SELECT department_id
    FROM departments
    WHERE department_name = 'Sales'
);

-- 2. Multiple-Row Subquery
-- This subquery returns multiple rows and is used with operators like IN,ANY,ALL,EXISTS
-- Example: Find employees who work in any department located in location_id 1700.
SELECT employee_id, first_name, last_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location_id = 1700
);

-- 3. Multiple-Column Subquery
-- This subquery returns multiple columns and is used in the WHERE clause.
-- Example: Find employees who have the same department_id and job_id as in the job_history table for employee_id 101.
SELECT employee_id, first_name, last_name
FROM employees
WHERE (department_id, job_id) IN (
    SELECT department_id, job_id
    FROM job_history
    WHERE employee_id = 101
);

-- 4. Correlated Subquery
-- This subquery refers to columns from the outer query and is evaluated for each row.
-- Example: Find employees whose salary is greater than the average salary of their department.
SELECT employee_id, first_name, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);

-- 5. Scalar Subquery
-- This subquery returns a single value and can be used in places where a single value is expected.
-- Example: Find employees and their department name.
use B1213;
SELECT first_name, last_name,department_id,
       (SELECT department_name
        FROM departments
        WHERE department_id = e.department_id) AS department_name
FROM employees e;

select * from employees;
select * from departments;

-- 6. Inline View
-- This subquery is used in the FROM clause and treated as a table.
-- Example: Find employees and their department names for departments in location_id 1700.
SELECT e.employee_id, e.first_name, d.department_name
FROM employees e,
     (SELECT department_id, department_name
      FROM departments
      WHERE location_id = 1700) d
WHERE e.department_id = d.department_id;



-- 7. Subqueries in the SELECT Clause
-- This subquery is used directly within the SELECT clause to compute values.
-- Example: Find employees and their department names.
SELECT employee_id, first_name,
       (SELECT department_name
        FROM departments
        WHERE department_id = e.department_id) AS department_name
FROM employees e;

-- 8. Subqueries in the HAVING Clause
-- This subquery is used in the HAVING clause to filter groups.
-- Example: Find departments with an average salary greater than the average salary of department_id 60.
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = 60
);

-- ================================================================
--  Examples
-- ================================================================

-- Example 1: Find employees who have the same job title as 'IT_PROG' job_id.
SELECT employee_id, first_name, last_name
FROM employees
WHERE job_id = (
    SELECT job_id
    FROM jobs
    WHERE job_title = 'IT_PROG'
);

-- Example 2: Find employees who earn more than the average salary in their department.
SELECT employee_id, first_name, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);

-- Example 3: Find employees who work in departments with a budget greater than $500,000.
SELECT employee_id, first_name, last_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE budget > 500000
);

-- Example 4: Find departments where the number of employees is greater than 5.
SELECT department_id
FROM employees
GROUP BY department_id
HAVING COUNT(employee_id) > 5;

-- Example 5: Find the department with the highest average salary.
SELECT department_id,avg(salary)
FROM employees
GROUP BY department_id
ORDER BY AVG(salary) DESC
LIMIT 1;

-- Single-Row Subquery
SELECT first_name, last_name 
FROM employees 
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Sales');

-- Multiple-Row Subquery
SELECT first_name, last_name 
FROM employees 
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name IN ('Sales', 'IT'));

-- Multiple-Column Subquery
SELECT first_name, last_name 
FROM employees 
WHERE (department_id, salary) IN (SELECT department_id, MAX(salary) FROM employees GROUP BY department_id);

-- Correlated Subquery
SELECT e.first_name, e.last_name 
FROM employees e 
WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);

-- Non-Correlated Subquery
SELECT first_name, last_name 
FROM employees 
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'IT');

-- Subquery in SELECT Clause
SELECT first_name, last_name, 
       (SELECT department_name FROM departments WHERE department_id = e.department_id) AS department 
FROM employees e;

-- Subquery in FROM Clause
SELECT emp.first_name, emp.last_name, sub.department_name 
FROM employees emp 
JOIN (SELECT department_id, department_name FROM departments) sub 
ON emp.department_id = sub.department_id;

-- Subquery in WHERE Clause
SELECT first_name, last_name 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in HAVING Clause
SELECT department_id, AVG(salary) 
FROM employees 
GROUP BY department_id 
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);

-- Subquery in INSERT Statement
create table high_earners (employee_id int, first_name varchar(30), last_name varchar(30), salary float);

INSERT INTO high_earners (employee_id, first_name, last_name, salary)
SELECT employee_id, first_name, last_name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

select * from high_earners;

-- Subquery in UPDATE Statement
UPDATE employees 
SET salary = salary * 1.1 
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'HR');

-- Subquery in DELETE Statement
DELETE FROM employees 
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Finance');

select * from emp;
select * from emp
where sal> (select sal from emp
where ename = 'smith');

select * from dept;
select * from emp
where deptno = (select deptno from dept
where dname = 'accounting');
	
select * from emp
where sal > all(select sal from emp
where deptno = 20);

select sal from emp
where deptno = 20;
select deptno from dept
where dname = 'accounting';




