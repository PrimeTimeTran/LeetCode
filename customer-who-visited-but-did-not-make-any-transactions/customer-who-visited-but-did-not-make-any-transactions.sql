# SELECT customer_id, COUNT(v.visit_id) as count_no_trans 
# FROM Visits v
# LEFT JOIN Transactions t ON v.visit_id = t.visit_id
# WHERE transaction_id IS NULL
# GROUP BY customer_id;

select customer_id, count(v.visit_id) as count_no_trans
from visits v
left join transactions t
on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id