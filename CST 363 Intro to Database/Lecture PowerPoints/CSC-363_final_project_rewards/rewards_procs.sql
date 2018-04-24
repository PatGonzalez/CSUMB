/*
Stored procs for the Rewards database
- Customer awards display
- Customer rewards display
- Customer details pull

---- test statements
call GetCustomerAwardStatement(36);

call GetCustomerRewardStatement(36);

call GetCustomerDetails(36);

call SearchCustomer('mloeser@csumb.edu', null);

*/
DELIMITER $$

USE rewards$$


DROP PROCEDURE IF EXISTS GetCustomerAwardStatement$$

/*
proc: GetCustomerAwardStatement
takes a customer_id value as a param and retrieves all records from the awards table.
would be used to generate an award statement display page.
*/
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

/*
proc: GetCustomerRewardStatement
takes a customer_id value as a param and retrieves all records from the rewards table.
would be used to generate an reward statement display page.
*/
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

/*
proc: GetCustomerDetails
takes a customer_id value as a param and retrieves details from the customer and summary tables.
would be used in a customer detail display in UI or as a post login page to retrieve all customer
	information for caching.
*/
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

/*
proc: SearchCustomer
accepts optional params of email_address or phone_number and performs a search against the
	customer table to find matches.
the entry page for taking the search criteria should enforce format requirements for the inputs.
*/
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




