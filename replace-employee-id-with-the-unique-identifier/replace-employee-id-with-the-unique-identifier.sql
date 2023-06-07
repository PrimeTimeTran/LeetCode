select unique_id, name 
from employees e
left outer join employeeuni u
on e.id = u.id