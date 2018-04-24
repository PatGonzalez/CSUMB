/*
some example queries
*/

set @customer_id = 3;

-- select all award information for the given customer
SELECT a.award_id, 
	a.customer_id,
	a.award_type_id,
	a.txn_id,
	a.point_earn,
	a.points,
	a.award_date,
	t.purchase_amt,
	t.tax_amt,
	t.txn_date,
	p.type_description
FROM awards as a
	JOIN award_type as p
		ON p.award_type_id = a.award_type_id
	LEFT OUTER JOIN transactions as t
		ON t.txn_id = a.txn_id
WHERE a.customer_id = @customer_id 
ORDER BY a.award_date;

-- retrieve the rewards records
SELECT r.reward_id, 
	r.customer_id,
	r.points,
	r.reward_date
FROM rewards as r
WHERE r.customer_id = @customer_id 
ORDER BY r.reward_date;

-- retrieve the records from summary table
SELECT c.customer_id,
	c.first_name,
	c.last_name,
	c.birthdate,
	c.enroll_date,
	c.email_address,
	c.phone_number,
	s.points,
	s.total_rewards,
	s.total_awards,
	s.last_updated
FROM customers as c
	LEFT OUTER JOIN summary as s
		ON s.customer_id = c.customer_id
WHERE c.customer_id = @customer_id;

-- select daily transaction totals
-- possibly to be used in an admin display of daily transactions
select 
    txn_date,
    sum(purchase_amt),
    sum(tax_amt)
from transactions
group by txn_date
order by txn_date desc;

-- select all of the customer details and summary data for the customer records
SELECT c.customer_id,
	c.first_name,
	c.last_name,
	c.birthdate,
	c.enroll_date,
	c.email_address,
	c.phone_number,
	s.points,
	s.total_rewards,
	s.total_awards,
	s.last_updated
FROM customers as c
	LEFT OUTER JOIN summary as s
		ON s.customer_id = c.customer_id;

