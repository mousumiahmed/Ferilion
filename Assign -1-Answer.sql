-- Assignment_1

-- 1. Create the following emp table
create database assignment_1;
use assignment_1;
create table emp(
empno int primary key not null,
ename varchar(10),
job varchar(9),
mgr int,
hiredate date,
sal decimal(7,2),
comm decimal(7,2),
deptno int,
index(deptno)

);
alter table emp
modify column empno int not null,
modify column ename varchar(10),
modify column job varchar(9),
modify column hiredate date,
modify column sal decimal(7,2),
modify column comm decimal(7,2),
modify column deptno int 
;
alter table emp
add mgr int;


describe emp;
drop table emp;
-- 2. Create the following dept table
create table dept(
deptno int primary key not null,
dname varchar(200) not null,
loc varchar(200) not null
);
alter table dept
modify column dname varchar(14),
modify column loc varchar(13);

describe dept;

insert into emp (empno,ename,job,mgr,hiredate,sal,comm,deptno) values (7369,"smith","clerk",7902,"1980-12-17",800,null,20),
(7499,"allen","salesman",7698,"1981-12-17",1600,300,30),(7521,"ward","salesman",7698,"1981-02-17",1250,500,30),
(7566,"jones","manager",7839,"1981-04-02",2975,500,20),(7568,"jones","manager",7839,"1981-04-02",1600,500,20);
insert into emp (empno,ename,job,mgr,hiredate,sal,comm,deptno) values (7568,"jones","manager",7839,"1981-04-02",1600,500,20);

select * from emp;
-- 3.1 Fetch the details of the employees along with the annual salary deduction with 10%
select empno,ename,sal,sal-(10/100)*sal as sal_after_deduction,(10/100)*sal as deducted_sal from emp;
-- 3.2 Fetch details of the employees who works in department 10 and 20
select * from emp where deptno = 20 or deptno = 10;
-- 3.3 Fetch the details of the employees whose name starts with char ‘A’ and has exactly 6 characters in their names
select * ,length(ename) from emp where ename like "a_____" ;
select * from emp where ename like "a%" and length(ename) = 5;

-- 4. Fetch the details of the employees whose salary is less 3000 and who earns no comm
select * from emp where sal < 3000 and comm is null;
select * from emp where sal < 3000 AND (comm IS NULL OR comm = 0);

-- Fetch the department number if the department consists of at least 2 employees

select empno from emp group by deptno having count(deptno)>=2;

-- Fetch the total salary need to pay to all the employees in each department
select *,sal+comm as total_salary from emp;
-- Query to show number of employees and average salary of each department
select * ,count(empno) as no_of_emp, avg(sal) from emp group by deptno ;
-- Query to show the salaries which is repeated
select *,count(sal) from emp group by sal having count(sal)>1 ;
-- Query to display max sal of each department if the if the max sal is more thann 1000
select max(sal) from emp group by deptno having max(sal)>1000;






