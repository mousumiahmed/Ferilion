-- String Functions:

-- Concatenation Functions:

-- 1. CONCAT() Function:
-- Definition: Combines two or more strings into a single string.
-- Syntax: CONCAT(str1, str2, ...)
-- Example:
SELECT CONCAT('Hello', ' ', 'World') AS concatenated_string;

-- Explanation:
-- CONCAT() combines multiple strings into a single string.

-- 2. CONCAT_WS() Function:
-- Definition: Combines multiple strings into a single string with a specified separator.
-- Syntax: CONCAT_WS(separator, str1, str2, ...)
-- Example:
SELECT CONCAT_WS(', ', 'apple', 'banana', 'orange') AS concatenated_string;

-- Explanation:
-- CONCAT_WS() combines multiple strings into a single string with the specified separator.

-- Substring Functions:

-- 1. SUBSTRING() Function:
-- Definition: Extracts a substring from a given string.
-- Syntax: SUBSTRING(str, start, length)
-- Example:
SELECT SUBSTRING('Hello World', 7, 5) AS extracted_string;

-- Explanation:
-- SUBSTRING() extracts a substring from the given string.

-- 2. SUBSTRING_INDEX() Function:
-- Definition: Extracts a substring from a string using a delimiter.
-- Syntax: SUBSTRING_INDEX(str, delim, count)
-- Example:
SELECT SUBSTRING_INDEX('apple,banana,orange', ',', 2) AS substring_result;

-- Explanation:
-- SUBSTRING_INDEX() extracts a substring from the string using the specified delimiter.

-- 3. LEFT() Function:
-- Definition: Returns a specified number of characters from the beginning of a string.
-- Syntax: LEFT(str, length)
-- Example:
SELECT LEFT('Hello World', 5) AS left_string;
-- Explanation:
-- LEFT() returns a specified number of characters from the beginning of a string.

-- 4. RIGHT() Function:
-- Definition: Returns a specified number of characters from the end of a string.
-- Syntax: RIGHT(str, length)
-- Example:
SELECT RIGHT('Hello World', 5) AS right_string;

-- Explanation:
-- RIGHT() returns a specified number of characters from the end of a string.

-- 5. MID() Function:
-- Definition: Extracts a substring from the middle of a string.
-- Syntax: MID(str, start, length)
-- Example:
SELECT MID('Hello World', 7, 5) AS mid_string;

-- Explanation:
-- MID() extracts a substring from the middle of a string.

-- Case Conversion Functions:

-- 1. UPPER() Function:
-- Definition: Converts a string to uppercase.
-- Syntax: UPPER(str)
-- Example:
SELECT UPPER('hello world') AS uppercase_string;

-- Explanation:
-- UPPER() converts all characters in the string to uppercase.

-- 2. LOWER() Function:
-- Definition: Converts a string to lowercase.
-- Syntax: LOWER(str)
-- Example:
SELECT LOWER('HELLO WORLD') AS lowercase_string;

-- Explanation:
-- LOWER() converts all characters in the string to lowercase.

-- Character Manipulation Functions:

-- 1. REPLACE() Function:
-- Definition: Replaces all occurrences of a substring in a string.
-- Syntax: REPLACE(str, old_substring, new_substring)
-- Example:
SELECT REPLACE('hello world', 'world', 'universe') AS replaced_string;

-- Explanation:
-- REPLACE() replaces all occurrences of the old substring with the new substring in the string.

-- 2. TRIM() Function:
-- Definition: Removes leading and trailing spaces from a string.
-- Syntax: TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)
-- Example:
SELECT TRIM('   hello world   ') AS trimmed_string;

-- Explanation:
-- TRIM() removes leading and trailing spaces from the string.

-- 3. LTRIM() Function:
-- Definition: Removes leading spaces from a string.
-- Syntax: LTRIM(str)
-- Example:
SELECT LTRIM('   hello world   ') AS ltrimmed_string;

-- Explanation:
-- LTRIM() removes leading spaces from the string.

-- 4. RTRIM() Function:
-- Definition: Removes trailing spaces from a string.
-- Syntax: RTRIM(str)
-- Example:
SELECT RTRIM('   hello world   ') AS rtrimmed_string;

-- Explanation:
-- RTRIM() removes trailing spaces from the string.

-- 5. REPEAT() Function:
-- Definition: Repeats a string a specified number of times.
-- Syntax: REPEAT(str, count)
-- Example:
SELECT REPEAT('hello ', 3) AS repeated_string;

-- Explanation:
-- REPEAT() repeats the string a specified number of times.

-- 6. REVERSE() Function:
-- Definition: Reverses the characters in a string.
-- Syntax: REVERSE(str)
-- Example:
SELECT REVERSE('hello world') AS reversed_string;

-- Explanation:
-- REVERSE() reverses the characters in the string.

-- 7. INSERT() Function:
-- Definition: Replaces a substring within a string with a new substring.
-- Syntax: INSERT(str, pos, len, newstr)
-- Example:
SELECT INSERT('hello world', 6, 0, 'beautiful ') AS inserted_string;

-- Explanation:
-- INSERT() inserts a new substring into the string at the specified position.


-- Demonstrating the usage of LOCATE, POSITION, and INSTR functions in MySQL

-- LOCATE function
-- Syntax: LOCATE(substring, string, start_position])
-- Description: Returns the position of the first occurrence of the `substring` in the `string`, starting from `start_position` if specified. The position is 1-based.

-- Example 1: Finding the position of 'world' in 'Hello world!'
SELECT LOCATE('', 'Hello world!') AS position1; //1

select locate('abc','xyab');
-- Result: 0

-- Example 2: Finding the position of 'world' in 'Hello world!' starting from position 8
SELECT LOCATE('world', 'Hello world!', 2) AS position2;
-- Result: 0 (since 'world' starts before position 8)


-- POSITION function
-- Syntax: POSITION(substring IN string)
-- Description: Returns the position of the first occurrence of the `substring` in the `string`. This function does not accept a `start_position` argument. The position is 1-based.

-- Example: Finding the position of 'world' in 'Hello world!'
SELECT POSITION('Hello' IN 'Hello world!') AS position3;
-- Result: 7


-- INSTR function
-- Syntax: INSTR(string, substring)
-- Description: Returns the position of the first occurrence of the `substring` in the `string`. The position is 1-based. Similar to `LOCATE`, but the order of arguments is reversed, and it does not accept a `start_position` argument.

-- Example: Finding the position of 'world' in 'Hello world!'
SELECT INSTR('Hello world!', 'world') AS position4;
-- Result: 7

-- Key Differences:
-- 1. Argument Order:
--    - LOCATE(substring, string)
--    - INSTR(string, substring)
-- 2. Optional Start Position:
--    - LOCATE allows specifying a `start_position`.
--    - POSITION and INSTR do not allow specifying a `start_position`.
-- 3. Syntax Style:
--    - POSITION uses POSITION(substring IN string).
--    - LOCATE and INSTR use a more traditional function call syntax.


-- Summary:
-- Use LOCATE when you need the flexibility to specify a starting position for the search.
-- Use POSITION if you prefer the POSITION(substring IN string) syntax and do not need a starting position.
-- Use INSTR if you prefer the reversed argument order compared to LOCATE.

select ifnull(null,2); # 2

select ifnull(2,3); # 2

select coalesce(null,null,2,3); # 2

select coalesce(2,null,null,2,3); #2

select nullif(2,2); # null

select nullif(2,3); # 2

select nullif(mgr,empno) from emp;

select concat_ws('-',18,7,2024);

select concat(18,'-',7,'-',2024);

select substring('MySQL is easy',2,5);

select substring_index('abc, xyz. abc.','a',2);


select * from emp;

describe emp;

select substring_index(sal,0,1) from emp;

use classicmodels;
select * from employees;

select firstname, replace(firstname,firstname,lastname) from employees;

select Trim('    ads     ');

select insert('abcd xyz',3,10,'pqrstuvxyz');


select insert(firstname,2,3,'firstname') from employees;


