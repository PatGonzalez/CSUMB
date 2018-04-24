# Ch.18 Pg.525

#2
CREATE USER ray@localhost IDENTIFIED BY 'temp';

GRANT select, insert, update
ON ap.vendors
TO ray@localhost
WITH GRANT OPTION;

GRANT select, insert, update
ON ap.invoices
TO ray@localhost
WITH GRANT OPTION;

GRANT select, insert
ON ap.invoice_line_items
TO ray@localhost
WITH GRANT OPTION;

#3
SHOW GRANTS FOR ray@localhost;

#8
GRANT update
ON ap.invoice_line_items
TO ray@localhost
WITH GRANT OPTION;

#9
GRANT select, insert, update
ON ap.*
TO dorothy@localhost IDENTIFIED BY 'sesame';