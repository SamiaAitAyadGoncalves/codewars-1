-- https://www.codewars.com/kata/594a8fa5a2db9e5f290000c3
--
-- Given the following table 'decimals':
--
-- decimals table schema
--
--     id
--     number1
--     number2
--
-- Return a table with one column (towardzero) where the values are the
-- result of number1 + number2 truncated towards zero.


select trunc(number1 + number2) as towardzero from decimals;
