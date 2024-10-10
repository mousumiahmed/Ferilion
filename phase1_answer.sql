show databases;
use classicmodels;
show tables;
-- 1. find the names of customers who have placed an order where the total order amount is greater than 10000
select customerName from customers where customernumber in
(select customerNumber from orders where orderNumber in 
(select orderNumber from orderdetails group by orderNumber having 
sum(quantityOrdered * priceEach)>10000));
-- 2.List of products that have never been ordered
select productName from products where productCode not in( select productCode from orderDetails);
-- 3.Find the employees who do not have any customers assigned to them
select firstName,lastName from employees where employeeNumber not in(select salesRepemployeeNumber from customers where salesRepemployeeNumber is not null );
-- 4.Get the offices that do not have any employees working on them
select * from offices
where officeCode not in(select officeCode from employees);
-- 5.List the products with a higher than average price (MSRP)
select * from products where msrp > (select avg(msrp) from products);
-- 6.Find the employee who report to "Marry Patterson"
select firstName,lastName from employees 
where reportsto = (select employeeNumber from employees where firstName like "Mary" and lastName like "Patterson");

-- 7.List of customer who have placed more than 5 order
select customerName from customers 
where customerNumber in 
(select customerNumber from orders group by customerNumber having count(orderNumber)>5);
-- 8.Get the names of customers who have made payment greater than 5000
select customerName from customers where customerNumber in (select customerNumber from payments where amount >5000);
-- 9.Find customer who have not placed any order in last year
select customerName from customers where customerNumber not in(select customerNumber from orders where orderDate > date_sub(curdate(), interval 1 year));
-- 10.Find the products ordered by customer
select productName from products where productCode in ( select productCode from orderdetails where orderNumber >0);
-- 11.Get the list of customers who have orderes but no payments
select customerName from customers where customerNumber in ( select customerNumber from orders where orderNumber > 0 
and customerNumber in (select customerNumber from payments where amount = 0));

-- 12.Find the name of customers who have placed an order in current month
select customerName from customers where customerNumber in (select customerNumber from orders where month(orderDate) = month(current_date())
and year(orderDate) = year(current_date()));

-- 13.List the employees who works in the same office as "Laslie Jennings"
select firstName,lastName,officeCode from employees where officeCode =(select officeCode from employees where firstName = "Laslie" and lastName = "Jennings");
-- select * from employees;
-- 14.Get the name of customers who have made a payment in last 7 days.
select customerName from customers where customerNumber in (select customerNumber from payments where paymentDate >= current_date() - interval 7 day );

-- 15.Find the product lines that have more than 50 products
select productLine from products group by productLine having sum(quantityInStock) > 50;
-- 16.List the name of employees who are managers(have other employee reporting to them
select concat(firstName," ",lastName) as Name,jobTitle from employees where employeeNumber in (select reportsTo from employees);
-- 17.Get the list of product codes for products that have been ordered more than 100 times
select json_arrayagg(productCode) from products where productCode in(select productCode from orderdetails group by productCode having sum(quantityOrdered)>100);
-- 18
describe customers ;
select c.customerName from customers c where c.customerNumber not in (select customerNumber from payments where paymentDate is not null);
select c.customerNumber,c.customerName,p.customerNumber,p.paymentDate from customers c left join payments p 
on c.customerNumber = p.customerNumber where p.customerNumber is null;

-- 19
select e.employeeNumber,e.firstName from employees e
where employeenumber in (select salesRepEmployeeNumber from customers c 
where customerNumber in (select customerNumber from orders o where o.customerNumber = c.customerNumber and orderNumber is null ));

-- 20
-- select * from employees;
-- select * from offices o where officeCode in
 -- select e.officeCode,e.employeeNumber from employees e where e.employeeNumber in (select salesRepEmployeeNumber from customers
--  where customerNumber in (select customerNumber from payments group by customerNumber having sum(amount)>50000)) ;

select * from employees where employeeNumber in
(select salesRepEmployeeNumber from customers where customerNumber in 
( select customerNumber  from payments group by customerNumber having sum(amount)>50000));

select * from employees e inner join customers c inner join payments p 
on e.employeeNumber = c.salesRepEmployeeNumber and c.customerNumber = p.customerNumber
group by p.customerNumber having sum(p.amount)>50000;
-- 21
-- select p.productCode,p.productName from products p where productCode in (select o.productCode from orderDetails o 
-- where p.productCode = o.productCode
select p.productCode,o1.customerNumber,o.quantityOrdered,count(distinct o1.customerNumber) from products  p inner join  orderDetails o on p.productCode = o.productCode inner join orders o1 on o.orderNumber = o1.orderNumber
group by o.productCode having count(distinct o1.customerNumber)>10 order by o1.customerNumber;

-- 31
select *,e.officeCode,count(employeeNumber) from employees e group by e.officeCode having count(employeeNumber)>5;

SELECT * FROM classicmodels.orders;
use classicmodels;
-- 23
select customerNumber,orderDate , year(orderDate),quarter(orderDate) as quarter_c  from orders ;
select customerNumber, year(orderDate) as order_year
from orders group by customerNumber, year(orderDate)
having count(distinct quarter(orderDate)) = 4
order by customerNumber;

select date_sub(curdate(), interval 1 year);




-- 24
select productCode,productName,buyPrice from products group by productCode having buyPrice < avg(buyPrice);
-- 25
select customerNumber ,customerName,count(distinct salesRepEmployeeNumber) from customers 
group by salesRepEmployeeNumber having  count(distinct salesRepEmployeeNumber)>1 ;
-- 26
select productLine,buyPrice ,min(buyPrice),productCode from products group by productLine having min(buyPrice)>20  ;


-- 27
select orderNumber,count(distinct productCode) from orderDetails group by orderNumber having count(distinct productCode)>5;
-- 28
select employeeNumber from employees where employeeNumber in ( select salesRepEmployeeNumber from customers group by salesRepEmployeeNumber having count(distinct customerNumber)>0 order by count(distinct customerNumber) desc  );
select e.employeeNumber,count(distinct customerNumber) from employees e inner join customers c on e.employeeNumber = c.salesRepEmployeeNumber
group by salesRepEmployeeNumber having count(distinct customerNumber)>0 order by count(distinct customerNumber) desc;

-- 29
select o.orderNumber from orders o where o.orderNumber in (
select o1.orderNumber from orderdetails o1 group by o1.productCode having avg(o1.priceEach)>200 );

select *,sum(o1.priceEach),avg(priceEach) from orders o inner join orderdetails o1 on o.orderNumber = o1.orderNumber
group by productCode having avg(priceEach)>150 ;








