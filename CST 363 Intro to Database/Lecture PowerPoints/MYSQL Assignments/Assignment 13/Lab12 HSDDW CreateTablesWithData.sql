/* HSD Data Warehouse star schema table */

DROP SCHEMA IF EXISTS hsddw;
CREATE SCHEMA hsddw;
USE hsddw;


create table timeline(
	timeid 		int 		not null auto_increment primary key,
	date   		date 		not null,
	monthid 	int		not null,
	monthtext 	char(15) 	not null,
	quarterid 	int		not null,
	quartertext 	char(10) 	not null,
	year		char(10)	not null
);

create table customer (
	customerid	int		not null primary key,
	customername	varchar(75)	not null,
	emaildomain	varchar(100)	not null,
	phoneareacode	char(6)		not null,
	city		char(35)	 null,
	state		char(2)		 null,
	zip		char(10)	 null
);

create table product (
	productnumber	char(35)	not null primary key,
	producttype	char(25)	not null,
	productname	varchar(75)	not null
);

create table product_sales (

		timeid		int		not null,

		customerid	int		not null,

		productnumber	char(35)	not null,

		quantity	int		not null,

		unitprice	numeric(9,2)	not null,

		total		numeric(9,2)	null,



	constraint product_sales_pk primary key (timeid, customerid, productnumber),


 
	constraint timeline_fk foreign key(timeid) references timeline(timeid) 
	
	 on delete no action on update no action,



       constraint customerid_fk foreign key(customerid) references customer(customerid) 
		
         on delete no action on update no action,



      constraint product_fk foreign key(productnumber) references product(productnumber)
	
        on delete no action	on update no action 


);


/*  months table used when loading timeline table */

create table months (
	monthid		int		not null,
	monthtext	char(15)	not null,
	quarterid	int		not null,
	quartertext	char(10)	not null
);


insert into months values
(1, 'January', 1, 'Qtr1'),
(2, 'February', 1, 'Qtr1'),
(3, 'March', 1, 'Qtr1'),
(4, 'April', 2, 'Qtr2'),
(5, 'May', 2, 'Qtr2'),
(6, 'June', 2, 'Qtr2'),
(7, 'July', 3, 'Qtr3'),
(8, 'August', 3, 'Qtr3'),
(9, 'September', 3, 'Qtr3'),
(10, 'October', 4, 'Qtr4'),
(11, 'November', 4,'Qtr4'),
(12, 'December', 4, 'Qtr4');

/*  load the timeline table from invoice data */

insert into hsddw.timeline (date, monthid, monthtext, quarterid, quartertext, year) 

select distinct a.invoicedate, month(a.invoicedate), b.monthtext, b.quarterid, b.quartertext, year(a.invoicedate)

from hsd.invoice a, hsddw.months b where month(a.invoicedate) = b.monthid; 
	
/* load the hsddw customer table from hsd customer */

insert into hsddw.customer 

(customerid, customername, emaildomain, phoneareacode, city, state, zip)
 
select customerid, concat( trim(lastname), ' ', trim(firstname)), substring(emailaddress, locate('@', emailaddress)+1),   
         substring(phone,1,3), city, state, zip 

from hsd.customer;

/* load hsddw product table from hsd product */

insert into hsddw.product select productnumber, producttype, productdescription from hsd.product;

/* load product sales */ 
/* multiple sales of the same product to the same customer on same date are combined */

insert into hsddw.product_sales 

 (timeid, customerid, productnumber, quantity, unitprice, total) 

select  c.timeid, a.customerid, b.productnumber, sum(b.quantity), min(b.unitprice), sum(b.total)
 
from  hsd.invoice a, hsd.line_item b, hsddw.timeline c  
 
where a.invoicenumber = b.invoicenumber and a.invoicedate=c.date
 
group by c.timeid, a.customerid, b.productnumber;


#Assignment 13 add on
CREATE TABLE SALES_FOR_RFM(
	TimeID	int			NOT NULL,
    CustomerID int		NOT NULL,
    InvoiceNumber Int	NOT NULL,
    PreTaxTotalSale Numeric(9,2)	NOT NULL,
    Constraint	SALES_FOR_RFM_PK
				PRIMARY KEY (TimeID, CustomerID, InvoiceNumber),
	Constraint	SRFM_Timeline_FK Foreign key(timeID)
					References Timeline(timeID)
						On Update No Action
                        On Delete No Action,
	Constraint	SRFM_Customer_FK Foreign Key(CustomerID)
					References Customer(CustomerID)
                    On Update No ACtion
                    On Delete No Action
	);
#5
Insert Into hsddw.SALES_FOR_RFM (TimeID, CustomerID, InvoiceNumber, PreTaxTotalSale)
Select t.TimeID, c.CustomerID, i.InvoiceNumber, i.SubTotal
From hsddw.timeline t, hsddw.customer c, hsd.invoice i
Order By  t.TimeID, c.CustomerID, i.InvoiceNumber;

#6
SELECT c.CustomerId, c.CustomerName, c.City, 
p.ProductNumber, p.ProductName,
t.Year,t.QuarterText, 
SUM(ps.Quantity) AS TotalQuantity
 FROM customer c, product_sales ps, product p,
      timeline t
WHERE c.CustomerId = ps.CustomerID 
      AND p.ProductNumber = ps.ProductNumber
      AND t.TimeId = ps.TimeID
GROUP BY c.CustomerId, c.CustomerName, c.City, 
         p.ProductNumber, p.ProductName, 
         t.QuarterText, t.Year
ORDER BY c.CustomerName, t.Year, t.QuarterText; 





SELECT c.CustomerId, c.CustomerName, c.City, 
p.ProductNumber, p.ProductName,
t.Year,t.QuarterText, 
SUM(ps.Quantity*ps.unitprice) as TotalAmount
 FROM customer c, product_sales ps, product p,
      timeline t
WHERE c.CustomerId = ps.CustomerID 
      AND p.ProductNumber = ps.ProductNumber
      AND t.TimeId = ps.TimeID
GROUP BY c.CustomerId, c.CustomerName, c.City, 
         p.ProductNumber, p.ProductName, 
         t.QuarterText, t.Year
ORDER BY c.CustomerName, t.Year, t.QuarterText; 

#7
Create View dollar_amount as
SELECT c.CustomerId, c.CustomerName, c.City, 
p.ProductNumber, p.ProductName,
t.Year,t.QuarterText, 
SUM(ps.Quantity*ps.unitprice) as TotalAmount
 FROM customer c, product_sales ps, product p,
      timeline t
WHERE c.CustomerId = ps.CustomerID 
      AND p.ProductNumber = ps.ProductNumber
      AND t.TimeId = ps.TimeID
GROUP BY c.CustomerId, c.CustomerName, c.City, 
         p.ProductNumber, p.ProductName, 
         t.QuarterText, t.Year
ORDER BY c.CustomerName, t.Year, t.QuarterText; 

#8
Select *
FRom dollar_amount;

#9
Create Table Payment_Type(
	Payment_ID 		int	not null auto_increment,
	Payment_Date 	datetime 		Not Null,
    Payment_Amount 	Int 			Not Null,
    PaymentType		Char(25) 	NOT NULL DEFAULT 'Cash',
	Constraint primary key(Payment_ID)); 


Insert Into hsddw.Payment_Type (Payment_Date,Payment_Amount,PaymentType)
Select t.date, i.total, i.PaymentType
From hsddw.timeline t, hsd.invoice i
Order By  t.TimeID;















