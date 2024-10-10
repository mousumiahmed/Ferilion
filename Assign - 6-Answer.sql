use mysqlsampledatabase;
show tables;
-- select * from customers;

show databases;
use classicmodels;
show tables;
select * from customers;
use assignment_1;
CREATE TABLE dept1 (
    deptno INT(2),
    dname VARCHAR(14),
    loc VARCHAR(13),
    PRIMARY KEY (deptno)
);

insert into dept1 (deptno, dname, loc) 
values(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON');



CREATE TABLE emp1 (
    empno INT(4),
    ename VARCHAR(10),
    job VARCHAR(9),
    mgr INT(4),
    hiredate DATE,
    sal DECIMAL(7,2),
    comm DECIMAL(7,2),
    deptno INT(2),
    PRIMARY KEY (empno),
    FOREIGN KEY (deptno) REFERENCES dept1 (deptno)
);

INSERT INTO emp1
VALUES
(7839, 'KING', 'PRESIDENT', NULL, STR_TO_DATE('17-11-1981', '%d-%m-%Y'), 5000, NULL, 10),
(7698, 'BLAKE', 'MANAGER', 7839, STR_TO_DATE('1-5-1981', '%d-%m-%Y'), 2850, NULL, 30),
(7782, 'CLARK', 'MANAGER', 7839, STR_TO_DATE('9-6-1981', '%d-%m-%Y'), 2450, NULL, 10),
(7566, 'JONES', 'MANAGER', 7839, STR_TO_DATE('2-4-1981', '%d-%m-%Y'), 2975, NULL, 20),
(7788, 'SCOTT', 'ANALYST', 7566, STR_TO_DATE('13-07-1987', '%d-%m-%Y') - INTERVAL 85 DAY, 3000, NULL, 20),
(7902, 'FORD', 'ANALYST', 7566, STR_TO_DATE('3-12-1981', '%d-%m-%Y'), 3000, NULL, 20),
(7369, 'SMITH', 'CLERK', 7902, STR_TO_DATE('17-12-1980', '%d-%m-%Y'), 800, NULL, 20),
(7499, 'ALLEN', 'SALESMAN', 7698, STR_TO_DATE('20-2-1981', '%d-%m-%Y'), 1600, 300, 30),
(7521, 'WARD', 'SALESMAN', 7698, STR_TO_DATE('22-2-1981', '%d-%m-%Y'), 1250, 500, 30),
(7654, 'MARTIN', 'SALESMAN', 7698, STR_TO_DATE('28-9-1981', '%d-%m-%Y'), 1250, 1400, 30),
(7844, 'TURNER', 'SALESMAN', 7698, STR_TO_DATE('8-9-1981', '%d-%m-%Y'), 1500, 0, 30),
(7876, 'ADAMS', 'CLERK', 7788, STR_TO_DATE('13-07-1987', '%d-%m-%Y') - INTERVAL 51 DAY, 1100, NULL, 20),
(7900, 'JAMES', 'CLERK', 7698, STR_TO_DATE('3-12-1981', '%d-%m-%Y'), 950, NULL, 30),
(7934, 'MILLER', 'CLERK', 7782, STR_TO_DATE('23-1-1982', '%d-%m-%Y'), 1300, NULL, 10);

select * from emp1;  
select * from dept1;
-- Aggregate Functions
-- MAX: What is the highest salary (`sal`) among all employees?
select max(sal) as highest_salary from emp1;
-- min: What is the lowest salary (`sal`) in the `emp` table?
select min(sal) as lowest_salary from emp1;
-- avg:What is the average salary (`sal`) of employees in department 30?
select avg(sal) from emp1 where deptno = 30;
-- Sum :What is the total salary (`sal`) for all employees in department 20?
select sum(sal) from emp1 where deptno = 20;
-- COUNT: How many employees are there in each department?
select deptno,count(empno) from emp1 group by deptno ;
-- JSON_ARRAYAGG: What is the JSON array of all employee names (`ename`) in department 10?
select json_arrayagg(ename) from emp1 where deptno = 10;
-- JSON_OBJECTAGG: What is the JSON object with `empno` as keys and `ename` as values for employees in department 30?
select json_objectagg(empno,ename) from emp1 where deptno = 30;
-- GROUP_CONCAT: What are the names (`ename`) of employees in department 20, concatenated into a single string?
select group_concat(ename) from emp1 where deptno = 20;

-- Comparison Functions
-- COALESCE: What is the salary (`sal`) of employees in department 20, showing 0 for employees with NULL salaries?
select deptno,coalesce(sal,0) from emp1 where deptno = 20;
-- GREATEST: What is the highest salary (`sal`) among the employees in departments 10 and 20?
select max(sal) from emp1 where deptno = 10 or deptno = 20;
-- LEAST: What is the lowest salary (`sal`) among the employees in departments 30 and 40?
select min(sal) from emp1 where deptno = 30 or deptno = 40;
-- ISNULL: What is the result when checking if the `comm` value for each employee is NULL?
select isnull(comm) from emp1;

-- Control Flow Functions
-- CASE: Provide a list of employee names (`ename`) and their salary (`sal`), showing 'High' if the salary is greater than 2500 and 'Low' otherwise.
select ename,
		sal,
		case when sal>2500 then "High"
		else "Low"
    end from emp1;
-- IF:Show the name (`ename`) and salary (`sal`) of employees with a salary greater than 3000, and state 'High' if true, 'Not High' if false.
    
select ename ,sal as salary , if(sal>3000, "High" ,"Not high") from emp1 ;
-- IFNULL: Display the salary (`sal`) for employees, replacing NULL salaries with 1000.
select ifnull(sal,1000) as salary from emp1;
-- NULLIF: Show the salary (`sal`) for each employee, replacing salaries of 1000 with NULL.
select nullif(sal,1000) from emp1;

--  String Functions
-- SUBSTRING: Extract the first 3 characters of the employee names (`ename`).
select left(ename,3) from emp1;
select substring(ename,1,3) from emp1;
-- SUBSTRING_INDEX: Get the department names (`dname`) with only the first 3 characters.
-- select substring_index(dname,"",1) from dept1; will not work 
select substr(dname,1,3) from dept1;
-- CONCAT_WS: Concatenate `ename` and `sal` of employees in department 10, separated by a hyphen (`-`).
select concat_ws("-", ename, sal) from emp1 where deptno = 10;
-- CONCAT: Combine `ename` and `job` for each employee into a single string.
select concat(ename,job) from emp1;
-- LOCATE: Find the position of 'A' in employee names (`ename`).
select locate('A',ename) as position from emp1;
-- INSERT: Insert 'XX' at the 2nd position of each employee name (`ename`).
select insert(ename,2,0,'xx') from emp1;
-- POSITION: Find the position of 'E' in the employee names (`ename`).
select position('E' in ename) from emp1;
-- REPLACE: Replace 'CLERK' with 'JUNIOR CLERK' in the job titles (`job`)
select replace(job,'CLERK','JUNIOR CLERK') from emp1;
-- REVERSE: Display the reversed employee names (`ename`).
select reverse(ename) from emp1;
-- Extract -- Domain from Email: If there were an email column, how would you extract the domain part (e.g., example.com) from the email addresses?
select substring_index("mdvfdfmv@gmail.com","@",-1);
 -- Get the First Character of Each Name: Extract the first character from each employee name (ename). (left)
 select left(ename,1) from emp1;
 -- Replace Multiple Characters: Replace all occurrences of 'A' with 'X' and 'E' with 'Y' in employee names (ename).
 select replace(replace(ename,'A','X'),'E','Y' ) from emp1;
 -- select ename.replace('A','X').replace('E','y') from emp1; Not working
 
--  Reverse and Capitalize: Reverse the employee names (ename) and convert them to uppercase.
select reverse(upper(ename)) from emp1;
-- Count Occurrences of a Character: Count how many times the character 'S' appears in each employee name (ename)
select ename,length(ename),length(REPLACE(ename, 'S', '')),length(ename)-length(REPLACE(ename, 'S', '')) as no_of_occ_of_S from emp1;

-- GROUP BY
-- GROUP BY: Show the total salary (`sal`) for each department.
select deptno,sum(sal) as total_salary from emp1 group by deptno;
-- GROUP BY with Multiple Columns: Display the total salary (`sal`) and average salary (`sal`) by job title (`job`) and department (`deptno`).
select deptno,job,sum(sal) as total_salary, avg(sal) as average_salary from emp1 group by deptno , job;
-- Total and Average Salary by Job Title: Show the total salary (sal) and average salary (sal) for each job title (job), and include only job titles where the total salary exceeds 5000.
select job as job_title,sum(sal) as total_salary,avg(sal) as average_salary
 from emp1 group by job having total_salary>5000;
 -- Count and Maximum Salary by Department: List each department (deptno) along with the number of employees and the maximum salary (sal) in that department, and sort the results by the department number.
select deptno,count(empno) as number_of_emp,max(sal) as maximum_sal from emp1 group by deptno order by deptno asc;
-- Department with More Than Two Distinct Jobs: Find departments that have more than two distinct job titles (job).
select deptno,job,count(distinct job) from emp1 group by deptno having count(distinct job)>2;

-- HAVING
-- HAVING: List departments where the total salary (`sal`) is more than 5000.
select deptno,sum(sal) as total_salary from emp1 group by deptno having total_salary>5000;
-- HAVING with Aggregation: Show departments where the number of employees is greater than 3 and the average salary is above 2000.
select deptno,count(empno),avg(sal) from emp1 group by deptno having count(empno)>3 and avg(sal)>2000;
-- HAVING with Multiple Conditions: List departments where the total salary is greater than 5000 and the maximum salary is less than 3000.
select deptno,sum(sal),max(sal) from emp1 group by deptno having sum(sal)>5000 and max(sal)<3000;
-- Departments with High Salary Disparity: List departments where the difference between the highest and lowest salary (sal) is greater than 2000
select deptno,max(sal)-min(sal) as sal_difference from emp1 group by deptno having sal_difference>2000;
-- Departments with More Than One Employee Earning Above 3000: Find departments where more than one employee has a salary (sal) greater than 3000.
select deptno ,count(empno) from emp1 where sal>3000 group by deptno having count(empno)>1;
-- Departments with High Average Salary and Low Employee Count: Show departments where the average salary (sal) is above 4000 but the number of employees is 3 or fewer.
select deptno, avg(sal),count(empno) from emp1 group by deptno having avg(sal)>4000 and count(empno)<=3;
-- WHERE Clause
-- WHERE: Find all employees who have a salary greater than 2500.
select * from emp1 where sal>2500;
-- ORDER BY 
-- ORDER BY: List all employees sorted by their salary (`sal`) in descending order
select * from emp1 order by sal desc;
-- ORDER BY with Multiple Columns: Sort employees first by department number (`deptno`) and then by salary (`sal`) in ascending order
select * from emp1 order by deptno,sal asc ;
-- Rank Employees by Salary: List employees (ename) and their salaries (sal), along with their rank based on salary in descending order. Use RANK to handle ties.
-- Window Functions: 
select ename,sal,deptno, rank() over(order by sal desc)  as rank_no from emp1;
-- select ename,sal,deptno, rank() over(partition by deptno order by sal desc)  as rank_no from emp1;
-- Dense Rank of Employees by Salary: Provide the dense rank of employees based on their salary (sal), where ties receive the same rank and no ranks are skipped. Use DENSE_RANK.
select ename,sal,deptno, dense_rank() over(order by sal desc)  as dense_rank_no from emp1;
-- Row Number within Department: Assign a unique row number to employees within each department (deptno) ordered by salary (sal). Use ROW_NUMBER
select sal,deptno,row_number() over(partition by deptno order by sal desc) as number_of_row from emp1;
-- Next Salary of Each Employee: Display each employeeâ€™s salary (sal) and the salary of the employee who comes immediately after them in the salary order using LEAD.
select ename,sal,lead(sal) over(order by sal asc) as lead_salary from emp1;
-- Previous Salary of Each Employee: Show each employeeâ€™s salary (sal) and the salary of the employee who came immediately before them using LAG
select ename,sal,lag(sal) over(order by sal asc) as lag_salary from emp1;
-- Nth Highest Salary: Find the 3rd highest salary (sal) in the emp table using NTH_VALUE.
-- SELECT  DISTINCT NTH_VALUE(sal, 3) OVER (ORDER BY sal DESC) AS third_highest_salary,sal FROM emp1; //not working 
select sal,nth_value(sal, 3) over (order by sal desc) as third_highest_salary
from (select distinct sal from emp1) subtable;
-- First Salary in Each Department: Show the first salary (sal) recorded in each department (deptno) using FIRST_VALUE.
select deptno, ename, sal, first_value(sal) over (partition by deptno) as first_salary from emp1;
-- Salary Distribution in Buckets: Divide employees into 4 equal groups based on their salary (sal) using NTILE
select ename, sal, ntile(4) over (order by sal desc) as salary_group from emp1;
-- Rank Employees by Salary within Job Title: Provide the rank of employees within each job title (job) based on salary (sal), using RANK
select deptno,job,sal,rank() over(partition by job order by sal desc) as job_rank from emp1;
-- Lag of Sales Commission for Salesmen: If there were a comm column representing commission, show each salesmanâ€™s commission (comm) and the commission of the previous salesman using LAG.
select ename, comm, LAG(comm) over (partition by job order by hiredate) as previous_commission
from emp1 where job = 'SALESMAN';

-- Compare Each Employeeâ€™s Salary to the Average Salary: For each employee, show their salary (sal) compared to the average salary of their department using LEAD.
	WITH department_avg AS (
    SELECT deptno, AVG(sal) AS avg_department_salary
    FROM emp1
    GROUP BY deptno
	)
	SELECT e.ename, e.sal, d.avg_department_salary,
		   LEAD(d.avg_department_salary) OVER (ORDER BY e.ename) AS next_avg_department_salary
	FROM emp1 e
	JOIN department_avg d ON e.deptno = d.deptno;

















