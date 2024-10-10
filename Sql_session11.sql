/*
Joins --  To combine the rows form multiple tables, based on a related columns between them.
 (Process of retrieval of data from multiple tables simultaneously)

Advantages
Combines Data from Multiple Tables:
	Advantage: Joins enable you to combine related data from different tables into a single result set.
	Benefit: This is essential for querying and analyzing data that is distributed across multiple tables.

Efficient Data Retrieval:
	Advantage: Joins allow for efficient retrieval of data by linking tables based on common columns, reducing the need for complex queries.
	Benefit: This improves query performance and reduces data redundancy.
	
Flexible Querying:
	Advantage: Joins allow you to filter, sort, and manipulate data from different tables based on relationships.
	Benefit: This provides greater flexibility in querying and presenting data.
    
Facilitates Complex Queries:
	Advantage: Joins make it possible to perform complex queries involving multiple tables.
	Benefit: This allows for sophisticated data analysis and reporting.

Types of Joins in MySQL:
Inner Join: Returns the records that have matching values in both the tables
	Syntax: 
		select exprn/column_name/* from table1 aliase inner join table2 aliase 
		on table_aliase.columN_name = table2_aliase.column_name;

		select exprn/col/* from table1,table2
		where table1.column_name=table2.column_name;
		
Left Join: Returns all records from left table and only matching records from right table
			If no match is found, NULL values are returned for columns from the right table.
	Syntax:
		select col/exprn/* from table1 t1 left join/ left outer join table2 t2
			on t1.column_name = t2.column_name;
			
Right Join: Returns all records from right table and only matching records from left table
			If no match is found, NULL values are returned for columns from the left table.
	Syntax:
		select col/* from table1 t1 right join/ right outer join table2 t2
        on t1.column_name = t2.column_name;
		
Cross Join: Returns all records from both the tables. (rarely used , because they produce very large result sets)
	Syntax:
		select col/expr/* from table1 cross join table 2;
		
		select col/exprn/* from table1,table2;
		
--> whenever need unmatched records from left table
	Syntax:
		select
		<select list> from table1 t1 left join table2 t2
		on t1.key = t2.key
		where t2.key is null;

--> whenever need unmatched records from right table
	syntax:
		select <select list> from table1 t1 right join table2 t2
		on t1.key = t2.key
		where t1.key is null;

--> Whenever need unamtched records from both left and right table except common
	Syntax:
		select <select list> from table1 t1 left join table2 t2
		on t1.key = t2.key
		union
		select <select list> from table1 t1 right join table2 t2
		on t1.key = t2.key
		where t1.key is null or 
		t2.key is null;
*/


use demo;
select e.ename as emp_names, e1.ename as rep_mgr, e2.ename as sup_mgr_names from emp e left join emp e1
on e.mgr = e1.empno left join emp e2
on e1.mgr = e2.empno;
select * from emp;

select ename from emp
union all
select ename from emp;

select * from emp e inner join dept d
on e.deptno = d.deptno;

select * from emp e, dept d
where e.deptno = d.deptno;

select * from emp e left join dept d
on e.deptno = d.deptno;



use classicmodels;
select * from employees e right join customers c
on e.employeeNumber = c.salesRepEmployeeNumber;

select * from employees e left join customers c
on e.employeeNumber = c.salesRepEmployeeNumber
union
select * from employees e right join customers c
on e.employeeNumber = c.salesRepEmployeeNumber;

select count(*) from employees;

select * from employees cross join customers;

select 122*23;