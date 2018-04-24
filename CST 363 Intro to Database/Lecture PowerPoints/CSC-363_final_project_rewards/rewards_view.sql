/*
reward view example
retrieves the customer details and summary information for display

-- test query using view
-- select * from CustomerDetailsSummary
*/
DROP VIEW IF EXISTS CustomerDetailsSummary;

CREATE VIEW CustomerDetailsSummary AS
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
            
SELECT * FROM CustomerDetailsSummary;