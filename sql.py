#second heighest
select * from (select first_name, customer_id, rank() over (order by customer_id desc)as rnk from Customers) where rnk = 2



SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > 1;
syn
