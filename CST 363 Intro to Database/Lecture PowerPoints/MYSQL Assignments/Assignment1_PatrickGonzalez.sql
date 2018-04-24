/*
CH.3 Exercieses 6-12
CH.5 1-9
By: Patrick Gonzalez
12/30/17
*/

#3.6
SELECT vendor_name, vendor_contact_last_name, vendor_contact_first_name
FROM vendors
ORDER BY vendor_contact_last_name, vendor_contact_first_name;

#3.7
SELECT concat(vendor_contact_last_name, ', ',vendor_contact_first_name) AS full_name
FROM vendors
WHERE vendor_contact_last_name regexp '^[ABCE]'
ORDER BY vendor_contact_last_name, vendor_contact_first_name;

#3.8
SELECT invoice_due_date as 'Due Date' , invoice_total as 'Invoice Total' , 
	round(0.1*invoice_total,2) as '10%' , round(0.1*invoice_total+invoice_total, 2) as 'Plus 10%'
FROM invoices
WHERE invoice_total between 500 and 1000
ORDER BY invoice_due_date desc; 

#3.9
SELECT	invoice_number, invoice_total, payment_total+credit_total AS payment_credit_total,
		invoice_total-payment_total-credit_total AS balance_due  
FROM invoices
WHERE invoice_total-payment_total-credit_total > 50
order by balance_due desc
LIMIT 5;

#3.10
SELECT invoice_number, invoice_date, invoice_total-payment_total-credit_total AS balance_due, payment_date
FROM invoices 
WHERE payment_date is NULL;

#3.11
SELECT date_format(current_date(), '%m-%d-%Y') AS 'CURRENT_DATE';

#3.12
SELECT 50000 AS starting_principal, round(0.065*50000,2) AS interest, 50000+round(0.065*50000,2) AS principal_plus_interest;

######################################################################################################

#5.1
INSERT INTO terms(terms_id, terms_description, terms_due_days)
VALUES (6, 'Net due 120 days', 120);

#5.2
UPDATE terms
SET terms_description='Net due 125 days', terms_due_days=125
WHERE terms_id = 6;

#5.3
DELETE 	FROM terms
WHERE terms_id = 6;

#5.4
INSERT INTO invoices
VALUES(default,32, 'AX-014-027', '2014-08-01', 434.58,0,0,2,'2014-08-31',NULL);

#5.5
INSERT INTO invoice_line_items
VALUES (115, 1, 160, 180.23, 'Hard drive'), 
		(115, 2, 527, 254.35, 'Exchange server update');

#5.6
UPDATE invoices
SET credit_total=0.1*invoice_total, payment_total=0.90*invoice_total
WHERE invoice_id=115;

#5.7
UPDATE vendors
SET default_account_number=403
WHERE vendor_id=44;

#5.8
UPDATE invoices
SET terms_id=2
WHERE vendor_id = (SELECT vendor_id 
					FROM vendors
					WHERE default_terms_id=2);
                    
#5.9
DELETE FROM invoices
WHERE invoice_id=115;

DELETE FROM invoice_line_items
WHERE invoice_id=115;




