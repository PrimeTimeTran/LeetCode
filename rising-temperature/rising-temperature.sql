# Write your MySQL query statement below
SELECT w1.id
FROM Weather w2, Weather w1
WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate, w2.recordDate) = 1