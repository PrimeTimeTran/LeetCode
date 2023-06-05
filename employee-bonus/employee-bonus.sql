# Write your MySQL query statement below

select name, bonus 
from employee e 
LEFT join bonus using(empId)
where coalesce(bonus, 0) < 1000