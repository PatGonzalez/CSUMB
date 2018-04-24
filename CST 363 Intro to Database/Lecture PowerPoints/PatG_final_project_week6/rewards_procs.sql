/*
Stored procs for the Rewards database
- Customer awards display
- Customer rewards display
- Customer details pull

---- test statements
call GetCustomerAwardStatement(@customer_id=1);

call GetCustomerRewardStatement(@customer_id=1);

call GetCustomerDetails(@customer_id=1);

call SearchCustomer(@email_address='mike@test.com', @phone_number=null);

*/
DELIMITER $$

USE rewards$$


DROP PROCEDURE IF EXISTS GetCustomerAwardStatement$$

CREATE PROCEDURE GetCustomerAwardStatement(
	in `customer_id` int)
BEGIN
	-- Retrieve the customer data for award statement display
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
	WHERE a.customer_id = customer_id 
	ORDER BY a.award_date;

END$$

GRANT EXECUTE ON PROCEDURE GetCustomerAwardStatement TO 'root'@'localhost'$$

/*

*/

DROP PROCEDURE IF EXISTS GetCustomerRewardStatement$$

CREATE PROCEDURE GetCustomerRewardStatement(
	in `customer_id` int)
BEGIN
	-- Retrieve the customer data for reward statement display
	SELECT r.reward_id, 
		r.customer_id,
        r.points,
        r.reward_date
	FROM rewards as r
	WHERE r.customer_id = customer_id 
	ORDER BY r.reward_date;

END$$

GRANT EXECUTE ON PROCEDURE GetCustomerRewardStatement TO 'root'@'localhost'$$

/*

*/

DROP PROCEDURE IF EXISTS GetCustomerDetails$$

CREATE PROCEDURE GetCustomerDetails(
	in `customer_id` int)
BEGIN
	-- Retrieve the customer data for reward statement display
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
	WHERE c.customer_id = customer_id;

END$$

GRANT EXECUTE ON PROCEDURE GetCustomerDetails TO 'root'@'localhost'$$

/*

*/

DROP PROCEDURE IF EXISTS SearchCustomer$$

CREATE PROCEDURE SearchCustomer(
	in `email_address` varchar(100),
	in `phone_number` varchar(100))
BEGIN
	-- Retrieve the customer data for reward statement display
	SELECT c.customer_id,
		c.first_name,
        c.last_name,
        c.birthdate,
        c.enroll_date,
        c.email_address,
        c.phone_number
	FROM customers as c
	WHERE c.email_address = coalesce(email_address, c.email_address)
		AND c.phone_number = coalesce(phone_number, c.phone_number);

END$$

GRANT EXECUTE ON PROCEDURE SearchCustomer TO 'root'@'localhost'$$



