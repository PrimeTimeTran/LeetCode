# select unique_id, name
# from employees as e
# LEFT OUTER JOIN employeeuni as u
# on e.id = u.id;

select unique_id, name
from employees
left join employeeuni
on employees.id = employeeuni.id