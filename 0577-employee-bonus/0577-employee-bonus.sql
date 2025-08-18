# Write your MySQL query statement below
SELECT name, bonus 
FROM Employee E
LEFT JOIN Bonus B
ON B.empId = E.empId 
WHERE bonus < 1000 OR bonus IS NULL;