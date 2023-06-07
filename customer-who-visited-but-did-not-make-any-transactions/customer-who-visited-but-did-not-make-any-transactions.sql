# SELECT customer_id, COUNT(v.visit_id) as count_no_trans 
# FROM Visits v
# LEFT JOIN Transactions t ON v.visit_id = t.visit_id
# WHERE transaction_id IS NULL
# GROUP BY customer_id;

select customer_id, count(visits.visit_id) as count_no_trans

from visits
LEFT join transactions
ON visits.visit_id = transactions.visit_id
where transaction_id IS NULL
group by customer_id