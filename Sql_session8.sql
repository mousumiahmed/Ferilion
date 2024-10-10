-- White Space Functions in MySQL

--	Introduction
-- White space functions in MySQL are used to manipulate and manage spaces and characters in strings.
-- Common white space functions include SPACE, ASCII, and CHAR.

-- SPACE Function
-- The SPACE function returns a string consisting of a specified number of space characters.

-- Syntax
-- SPACE(count)

-- Example 1: Using SPACE

-- Query: Select a string with 10 space characters.
SELECT CONCAT('Hello', SPACE(10), 'World') AS spaced_string;

-- Explanation:
-- 1. Uses the SPACE function to generate a string of 10 spaces.
-- 2. Concatenates 'Hello', 10 spaces, and 'World' to create the spaced_string.

-- ASCII Function
-- The ASCII function returns the ASCII value of the leftmost character of a string.

-- Syntax
-- ASCII(str)

-- Example 2: Using ASCII

-- Query: Select the ASCII value of the character 'A'.
SELECT ASCII('A') AS ascii_value;

-- Explanation:
-- 1. Uses the ASCII function to get the ASCII value of 'A'.
-- 2. Returns the ASCII value as ascii_value.

-- CHAR Function
-- The CHAR function returns the character for each integer passed as an argument.

-- Syntax
-- CHAR(N,... [USING charset_name])

-- Example 3: Using CHAR

-- Query: Select the character corresponding to ASCII value 65.
SELECT CHAR(65) AS character;

-- Explanation:
-- 1. Uses the CHAR function to get the character for the ASCII value 65.
-- 2. Returns the character 'A' as character.

-- Length and Count Functions in MySQL

-- Introduction
-- Length and count functions in MySQL are used to determine the length or number of characters or bits in strings.
-- Common length and count functions include LENGTH, CHAR_LENGTH, OCTET_LENGTH, BIT_LENGTH, CHARACTER_LENGTH, BIT_COUNT, and STRCMP.

-- LENGTH Function
-- The LENGTH function returns the length of a string in bytes.

-- Syntax
-- LENGTH(str)

-- Example 4: Using LENGTH

-- Query: Select the length of the string 'Hello'.
SELECT LENGTH('Hello') AS byte_length;

-- Explanation:
-- 1. Uses the LENGTH function to get the byte length of 'Hello'.
-- 2. Returns the byte length as byte_length.

-- CHAR_LENGTH Function
-- The CHAR_LENGTH function returns the length of a string in characters.

-- Syntax
-- CHAR_LENGTH(str)

-- Example 5: Using CHAR_LENGTH

-- Query: Select the character length of the string 'Hello'.
SELECT CHAR_LENGTH('Hello') AS char_length;

-- Explanation:
-- 1. Uses the CHAR_LENGTH function to get the character length of 'Hello'.
-- 2. Returns the character length as char_length.

-- OCTET_LENGTH Function
-- The OCTET_LENGTH function returns the length of a string in bytes.

-- Syntax
-- OCTET_LENGTH(str)

-- Example 6: Using OCTET_LENGTH

-- Query: Select the octet length of the string 'Hello'.
SELECT OCTET_LENGTH('Hello') AS octet_length;

-- Explanation:
-- 1. Uses the OCTET_LENGTH function to get the byte length of 'Hello'.
-- 2. Returns the byte length as octet_length.
	
-- BIT_LENGTH Function
-- The BIT_LENGTH function returns the length of a string in bits.

-- Syntax
-- BIT_LENGTH(str)

-- Example 7: Using BIT_LENGTH

-- Query: Select the bit length of the string 'Hello'.
SELECT BIT_LENGTH('Hello') AS bit_length;

-- Explanation:
-- 1. Uses the BIT_LENGTH function to get the bit length of 'Hello'.
-- 2. Returns the bit length as bit_length.

-- CHARACTER_LENGTH Function
-- The CHARACTER_LENGTH function returns the length of a string in characters.

-- Syntax
-- CHARACTER_LENGTH(str)

-- Example 8: Using CHARACTER_LENGTH

-- Query: Select the character length of the string 'Hello'.
SELECT CHARACTER_LENGTH('Hello') AS char_length;

-- Explanation:
-- 1. Uses the CHARACTER_LENGTH function to get the character length of 'Hello'.
-- 2. Returns the character length as char_length.

-- BIT_COUNT Function
-- The BIT_COUNT function returns the number of bits that are set in the argument.

-- Syntax
-- BIT_COUNT(N)

-- Example 9: Using BIT_COUNT

-- Query: Select the number of bits set to 1 in the number 5.
SELECT BIT_COUNT(5) AS bit_count;

-- Explanation:
-- 1. Uses the BIT_COUNT function to get the number of bits set to 1 in the binary representation of 5.
-- 2. Returns the bit count as bit_count.

-- STRCMP Function
-- The STRCMP function compares two strings.

-- Syntax
-- STRCMP(str1, str2)

-- Example 10: Using STRCMP

-- Query: Compare the strings 'Hello' and 'World'.
SELECT STRCMP('Hello', 'World') AS comparison_result;

-- Explanation:
-- 1. Uses the STRCMP function to compare 'Hello' and 'World'.
-- 2. Returns -1 if str1 is less than str2, 0 if they are equal, and 1 if str1 is greater than str2 as comparison_result.

-- Padding String Functions in MySQL

-- Introduction
-- Padding string functions in MySQL are used to pad strings to a certain length with a specified character.
-- Common padding string functions include LPAD and RPAD.

-- LPAD Function
-- The LPAD function pads the left side of a string with a specified character to a certain length.

-- Syntax
-- LPAD(str, len, padstr)

-- Example 11: Using LPAD

-- Query: Pad the string 'Hello' to a length of 10 with '*'.
SELECT LPAD('Hello', 10, '*') AS padded_string;

-- Explanation:
-- 1. Uses the LPAD function to pad the left side of 'Hello' with '*' to a length of 10.
-- 2. Returns the padded string as padded_string.

-- RPAD Function
-- The RPAD function pads the right side of a string with a specified character to a certain length.

-- Syntax
-- RPAD(str, len, padstr)

-- Example 12: Using RPAD

-- Query: Pad the string 'Hello' to a length of 10 with '*'.
SELECT RPAD('Hello', 10, '*') AS padded_string;

-- Explanation:
-- 1. Uses the RPAD function to pad the right side of 'Hello' with '*' to a length of 10.
-- 2. Returns the padded string as padded_string.

-- Window Functions in MySQL

-- Introduction
-- Window functions in MySQL perform calculations across a set of table rows related to the current row.
-- Common window functions include ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG, FIRST_VALUE, NTH_VALUE, NTILE, and PERCENT_RANK.

-- ROW_NUMBER Function
-- The ROW_NUMBER function assigns a unique number to each row within the partition of a result set.

-- Syntax
-- ROW_NUMBER() OVER (PARTITION BY column ORDER BY column)

-- Example 13: Using ROW_NUMBER

-- Tables:
-- employees: id, name, department, salary

-- Query: Assign a unique number to each employee within each department based on salary.
SELECT id, name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM employees;

-- Explanation:
-- 1. Uses the ROW_NUMBER function to assign a unique number to each employee within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the row number as row_num.

-- RANK Function
-- The RANK function assigns a rank to each row within the partition of a result set.

-- Syntax
-- RANK() OVER (PARTITION BY column ORDER BY column)

-- Example 14: Using RANK

-- Tables:
-- employees: id, name, department, salary

-- Query: Assign a rank to each employee within each department based on salary.
SELECT id, name, department, salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

-- Explanation:
-- 1. Uses the RANK function to assign a rank to each employee within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the rank as rank.

-- DENSE_RANK Function
-- The DENSE_RANK function assigns a rank to each row within the partition of a result set without gaps in the ranking.

-- Syntax
-- DENSE_RANK() OVER (PARTITION BY column ORDER BY column)

-- Example 15: Using DENSE_RANK

-- Tables:
-- employees: id, name, department, salary

-- Query: Assign a dense rank to each employee within each department based on salary.
SELECT id, name, department, salary,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Explanation:
-- 1. Uses the DENSE_RANK function to assign a dense rank to each employee within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the dense rank as dense_rank.

-- LEAD Function
-- The LEAD function provides access to a row at a specified physical offset following the current row within the partition.

-- Syntax
-- LEAD(expression, offset, default) OVER (PARTITION BY column ORDER BY column)

-- Example 16: Using LEAD

-- Tables:
-- employees: id, name, department, salary

-- Query: Get the next employee's salary within each department.
SELECT id, name, department, salary,
    LEAD(salary, 1, 0) OVER (PARTITION BY department ORDER BY salary DESC) AS next_salary
FROM employees;

-- Explanation:
-- 1. Uses the LEAD function to access the salary of the next employee within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the next salary as next_salary, defaulting to 0 if there is no next row.

-- LAG Function
-- The LAG function provides access to a row at a specified physical offset before the current row within the partition.

-- Syntax
-- LAG(expression, offset, default) OVER (PARTITION BY column ORDER BY column)

-- Example 17: Using LAG

-- Tables:
-- employees: id, name, department, salary

-- Query: Get the previous employee's salary within each department.
SELECT id, name, department, salary,
    LAG(salary, 1, 0) OVER (PARTITION BY department ORDER BY salary DESC) AS prev_salary
FROM employees;

-- Explanation:
-- 1. Uses the LAG function to access the salary of the previous employee within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the previous salary as prev_salary, defaulting to 0 if there is no previous row.

-- FIRST_VALUE Function
-- The FIRST_VALUE function returns the first value in an ordered set of values.

-- Syntax
-- FIRST_VALUE(expression) OVER (PARTITION BY column ORDER BY column)

-- Example 18: Using FIRST_VALUE

-- Tables:
-- employees: id, name, department, salary

-- Query: Get the first salary within each department.
SELECT id, name, department, salary,
    FIRST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary DESC) AS first_salary
FROM employees;

-- Explanation:
-- 1. Uses the FIRST_VALUE function to get the first salary within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the first salary as first_salary.

-- NTH_VALUE Function
-- The NTH_VALUE function returns the value of the nth row in an ordered set of values.

-- Syntax
-- NTH_VALUE(expression, n) OVER (PARTITION BY column ORDER BY column)

-- Example 19: Using NTH_VALUE

-- Tables:
-- employees: id, name, department, salary

-- Query: Get the third highest salary within each department.
SELECT id, name, department, salary,
    NTH_VALUE(salary, 3) OVER (PARTITION BY department ORDER BY salary DESC) AS third_salary
FROM employees;

-- Explanation:
-- 1. Uses the NTH_VALUE function to get the third highest salary within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the third salary as third_salary.

-- NTILE Function
-- The NTILE function distributes the rows in an ordered partition into a specified number of approximately equal groups.

-- Syntax
-- NTILE(n) OVER (PARTITION BY column ORDER BY column)

-- Example 20: Using NTILE

-- Tables:
-- employees: id, name, department, salary

-- Query: Distribute employees into four groups within each department based on salary.
SELECT id, name, department, salary,
    NTILE(4) OVER (PARTITION BY department ORDER BY salary DESC) AS quartile
FROM employees;

-- Explanation:
-- 1. Uses the NTILE function to distribute employees into four groups within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the quartile as quartile.

-- PERCENT_RANK Function
-- The PERCENT_RANK function calculates the relative rank of a row within a partition as a percentage of the partition.

-- Syntax
-- PERCENT_RANK() OVER (PARTITION BY column ORDER BY column)

-- Example 21: Using PERCENT_RANK

-- Tables:
-- employees: id, name, department, salary

-- Query: Calculate the percent rank of each employee within each department based on salary.
SELECT id, name, department, salary,
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS percent_rank
FROM employees;

-- Explanation:
-- 1. Uses the PERCENT_RANK function to calculate the relative rank of each employee within each department.
-- 2. Orders the rows by salary in descending order.
-- 3. Returns the percent rank as percent_rank.

-- Summary
-- White space functions such as SPACE, ASCII, and CHAR are used to manage spaces and characters in strings.
-- Length and count functions such as LENGTH, CHAR_LENGTH, OCTET_LENGTH, BIT_LENGTH, CHARACTER_LENGTH, BIT_COUNT, and STRCMP are used to determine the length or number of characters or bits in strings.
-- Padding string functions such as LPAD and RPAD are used to pad strings to a certain length with a specified character.
-- Window functions such as ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG, FIRST_VALUE, NTH_VALUE, NTILE, and PERCENT_RANK are used to perform calculations across a set of table rows related to the current row.
