# Write your MySQL query statement below

select name, bonus 
from employee e 
LEFT join bonus b
on e.empId = b.empId
where b.bonus < 1000 or bonus IS null

# SELECT name, bonus
# FROM Employee LEFT JOIN Bonus
# ON Employee.empID=Bonus.empID
# WHERE bonus<1000 OR bonus IS NULL