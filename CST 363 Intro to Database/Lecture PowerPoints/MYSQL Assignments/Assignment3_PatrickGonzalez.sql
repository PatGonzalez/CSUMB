/*
Assignment 3
Patrick Gonzalez
Ch.4 EX:1-7
CH.6 EX:1-7
Ch.7 All Ex.
*/

#### Chpater 4 #####################################

#1
SELECT *
FROM vendors INNER JOIN invoices 
		ON vendors.vendor_id=invoices.vendor_id;

#2
SELECT vendor_name, invoice_number, invoice_date, invoice_total-payment_total-credit_total AS balance_due
FROM  vendors v INNER JOIN invoices i 
		ON v.vendor_id = i.vendor_id
WHERE invoice_total-payment_total-credit_total > 0
ORDER BY vendor_name DESC;

#3
SELECT vendor_name, default_account_number AS default_account,account_description AS description
FROM vendors v INNER JOIN general_ledger_accounts gl 
		ON v.default_account_number = gl.account_number
ORDER BY account_description, vendor_name;

#4
SELECT vendor_name, invoice_date, invoice_number, invoice_sequence AS li_sequence, line_item_amount AS li_amount 
FROM vendors v 
	INNER JOIN invoices i
		ON v.vendor_id=i.vendor_id
    INNER JOIN invoice_line_items li 
		ON i.invoice_id=li.invoice_id
ORDER BY vendor_name, invoice_date, invoice_number, invoice_sequence; 

#5
SELECT v1.vendor_id, v1.vendor_name, CONCAT(v1.vendor_contact_first_name, ' ',v1.vendor_contact_last_name) AS contact_name
FROM vendors v1 JOIN vendors v2
		ON v1.vendor_id != v2.vendor_id
        AND v1.vendor_contact_last_name=v2.vendor_contact_last_name
ORDER BY v1.vendor_contact_last_name;

#6
SELECT gl.account_number, account_description, invoice_id
FROM general_ledger_accounts gl LEFT JOIN invoice_line_items li 
		ON gl.account_number=li.account_number
WHERE li.invoice_id IS NULL 
ORDER BY gl.account_number;

#7
	SELECT vendor_name, vendor_state
	FROM vendors
	WHERE vendor_state = 'CA'
UNION
	SELECT vendor_name, 'Outside CA'
	FROM vendors
	WHERE vendor_state != 'CA'
ORDER BY vendor_name;

#### Chpater 6 #####################################

#1
SELECT vendor_id, SUM(invoice_total) AS invoice_total_sum
FROM invoices
GROUP BY vendor_id;

#2
SELECT  vendor_name, SUM(payment_total) AS payment_total_sum
FROM vendors v JOIN invoices i
		ON v.vendor_id = i.vendor_id
GROUP BY vendor_name
ORDER BY payment_total_sum DESC;

#3
SELECT vendor_name, COUNT(*) AS invoice_count, SUM(invoice_total) AS invoice_total_sum
FROM vendors v JOIN invoices i
		ON v.vendor_id = i.vendor_id
GROUP BY vendor_name
ORDER BY  invoice_count DESC;

#4
SELECT account_description, COUNT(*) AS item_count, SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts gl JOIN invoice_line_items li 
		ON gl.account_number=li.account_number
GROUP BY account_description
HAVING item_count >1
ORDER BY line_item_amount_sum DESC;

#5
SELECT account_description, COUNT(*) AS item_count, SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts gl 
	JOIN invoice_line_items li 
		ON gl.account_number=li.account_number
	JOIN invoices i 
		ON li.invoice_id=i.invoice_id
WHERE invoice_date BETWEEN '2014-04-01' and '2014-06-30'
GROUP BY account_description
HAVING item_count >1
ORDER BY line_item_amount_sum DESC;

#6
#What is the total amount invoiced for each general ledger account number?
SELECT account_number, SUM(line_item_amount) AS line_item_amount_sum
FROM invoice_line_items li 
GROUP BY account_number WITH ROLLUP;

#7
#Which vendors are being paid from more than one account?
SELECT vendor_name, COUNT(DISTINCT li.account_number) AS number_of_accounts
FROM vendors v
	JOIN invoices i 
		ON v.vendor_id=i.vendor_id
	JOIN invoice_line_items li 
		ON i.invoice_id = li.invoice_id
GROUP BY vendor_name
HAVING number_of_accounts > 1
ORDER BY vendor_name;

#### Chpater 7 #####################################
 
#1
SELECT DISTINCT vendor_name
FROM vendors
WHERE vendor_id IN
	(SELECT vendor_id
	 FROM invoices)
ORDER BY vendor_name;

#2
/*Which invoices have a payment total that's greater than the 
average payment total for all invoices with a payment total greater than O?*/
SELECT invoice_number, invoice_total
FROM invoices
WHERE payment_total >
	(SELECT AVG(payment_total)
     FROM invoices
     Where payment_total>0)
ORDER BY invoice_total DESC;

#3
/*Return one row for each account number that has never been assigned to any
line item in the Invoice_Line_Items table.*/
SELECT account_number, account_description
FROM general_ledger_accounts gl
WHERE NOT EXISTS
	(SELECT *
     FROM invoice_line_items li
     WHERE li.account_number = gl.account_number)
ORDER BY account_number;

#4
/*Return a row for each line item of each invoice that has more than one line
item in the lnvoice_Line_Items table.*/
SELECT vendor_name, i.invoice_id, invoice_sequence, line_item_amount
FROM vendors v 
	JOIN invoices i 
		ON v.vendor_id=i.vendor_id
    JOIN invoice_line_items li 
		ON i.invoice_id=li.invoice_id
WHERE i.invoice_id IN 
	(SELECT DISTINCT invoice_id
     FROM invoice_line_items
     WHERE invoice_sequence >1);

#5
SELECT sum(max_invoice_total) AS sum_of_max_invoice_total
FROM (
	SELECT vendor_id, MAX(invoice_total) AS max_invoice_total
	FROM invoices
	Where invoice_total-credit_total-payment_total >0
	GROUP BY vendor_id
    ) t;

#6
SELECT vendor_name, vendor_city, vendor_state
FROM vendors
WHERE CONCAT(vendor_state, vendor_city) NOT IN
	(SELECT CONCAT(vendor_state, vendor_city) AS vendor_state_city
     FROM vendors
     GROUP BY vendor_state_city
     HAVING COUNT(*)>1)
ORDER BY vendor_state, vendor_city;

#7
SELECT vendor_name, invoice_number, invoice_date, invoice_total
FROM invoices i JOIN vendors v
	ON i.vendor_id=v.vendor_id
WHERE invoice_date =
	(SELECT MIN(invoice_date)
     FROM invoices
     WHERE vendor_id=i.vendor_id)
ORDER BY vendor_name;

#8
SELECT vendor_name, invoice_number, invoice_date, invoice_total
FROM invoices i 
	JOIN (SELECT vendor_id, MIN(invoice_date) AS oldest_invoice
		  FROM invoices
		  GROUP BY vendor_id) oi
		ON i.vendor_id=oi.vendor_id
		AND i.invoice_date = oi.oldest_invoice
    JOIN vendors v
		ON i.vendor_id=v.vendor_id
ORDER BY vendor_name;
