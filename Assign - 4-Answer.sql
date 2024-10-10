-- Replace all occurrences of 'Java' with 'Python' in the string 'Java is a programming language'.
select replace('Java is a programming language','Java','Python') as new_string;
-- Trim the leading and trailing spaces from the string '   Hello, World!   '.
select trim('   Hello, World!   ') as after_trim;
-- Repeat the string . three times
select repeat('OpenAI',3) as repeated_string;
-- Reverse the string 'MySQL'
select reverse('MySQL');
-- Insert the substring 'nice ' after the fifth character of the string 'Hello World'.
select insert('Hello World',6,0,'nice');

-- Convert the string 'DATABASE' to lowercase.
select lower('DATABASE');
-- Convert the string 'programming LANGUAGE' to uppercase.
select upper('programming LANGUAGE');
-- Convert the mixed-case string 'OpenAI' to uppercase.
select upper('OpenAI');
-- Convert the lowercase string 'python' to uppercase.
select upper('python');
-- Convert the uppercase string 'MYSQL' to lowercase.
select lower('MYSQL');
-- Find the first three characters from the string 'Database'.
select left('Database',3);
-- Get the last four characters from the string 'Programming'.
select right('Programming',4);
-- Extract the middle five characters from the string 'OpenAI'
select substring('OpenAI',2,5);
-- Retrieve the leftmost four characters from the string 'Artificial'
select left('Artificial',4);
-- Extract the rightmost seven characters from the string 'MachineLearning'
select right('MachineLearning',7);
-- Combine the strings 'Open' and 'AI' into a single string.
select concat('Open','AI');
-- Join the strings 'apple', 'banana', and 'orange' with a space separator
select concat_ws(" ",'apple', 'banana','orange');
-- Create a sentence by concatenating the strings 'My', 'name', 'is', and 'John'.
select concat_ws(" ",'My', 'name', 'is','John');
-- Combine the strings 'SQL' and 'is' with a hyphen separator.
select concat_ws("-",'SQL','is');
-- Concatenate the strings 'Today is' and the current date.
select concat('Today is ',curdate());