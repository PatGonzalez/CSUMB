/****************************************************************************/
/*																			*/
/*	Kroenke and Auer - Database Concepts (7th Edition)						*/
/*																			*/
/*	James River Jewelry Database Create Tables								*/
/*																			*/
/*	These are the MySQL 5.6 SQL code solutions								*/
/*																			*/
/****************************************************************************/
# uncomment to re-run script
#drop schema JRJ;

CREATE SCHEMA JRJ;
USE JRJ;

CREATE TABLE CUSTOMER(
	CustomerID			Int					NOT NULL auto_increment,
	LastName			Char(35)			NOT NULL,
	FirstName			Char(25)			NOT NULL,
	Phone				Char(12)			NULL,
	Email				VarChar(100)		NULL,
	CONSTRAINT			CUSTOMER_PK			PRIMARY KEY(CustomerID)
	);

CREATE TABLE ITEM(
	ItemNumber			Int					NOT NULL auto_increment,
	ItemDescription		VarChar(255)		NOT NULL,
	Cost				Numeric(9,2)		NOT NULL,
	ArtistLastName		Char(35)			NULL,
	ArtistFirstName		Char(25)			NULL,
	CONSTRAINT			ITEM_PK				PRIMARY KEY(ItemNumber)
	);

CREATE TABLE PURCHASE(
	InvoiceNumber		Int					NOT NULL auto_increment,
	InvoiceDate			Date				NOT NULL,
	PreTaxAmount		Numeric(9,2)		NOT NULL,
	CustomerID			Int					NOT NULL,
	CONSTRAINT			PURCHASE_PK			PRIMARY KEY(InvoiceNumber),
	CONSTRAINT 			PURCHASE_CUSTOMER_FK  FOREIGN KEY (CustomerID)
								REFERENCES CUSTOMER(CustomerID)
										ON DELETE NO ACTION
	);

CREATE TABLE PURCHASE_ITEM (
	InvoiceNumber		Int					NOT NULL,
	InvoiceLineNumber	Int					NOT NULL,
	ItemNumber			Int					NOT NULL,
	RetailPrice			Numeric(9,2)		NOT NULL,
	CONSTRAINT 			PURCHASE_ITEM_PK	
							PRIMARY KEY(InvoiceNumber, InvoiceLineNumber),
	CONSTRAINT			PURCHASE_ITEM_PURCHASE_FK  
							FOREIGN KEY (InvoiceNumber)
								REFERENCES PURCHASE(InvoiceNumber)
										ON DELETE CASCADE,
	CONSTRAINT			PURCHASE_ITEM_ITEM_FK  FOREIGN KEY (ItemNumber)
								REFERENCES ITEM(ItemNumber)
										ON DELETE NO ACTION
	);

/********************************************************************/
/********************************************************************************/
/* null is inserted in not-null auto_increment fields to generate next value.	*/
/*****   CUSTOMER DATA   ********************************************************/

INSERT INTO CUSTOMER VALUES(
	null,'Stanley', 'Elizabeth','555-236-7789', 'Elizabeth.Stanley@somewhere.com');
INSERT INTO CUSTOMER VALUES(
	null,'Price', 'Fred', '555-236-0091', 'Fred.Price@somewhere.com');
INSERT INTO CUSTOMER VALUES(
	null,'Becky', 'Linda', '555-236-0392', 'Linda.Becky@somewhere.com');
INSERT INTO CUSTOMER VALUES(
	null,'Birch', 'Pamela', '555-236-4493', 'Pamela.Birch@somewhere.com');
INSERT INTO CUSTOMER VALUES(
	null,'Romez', 'Ricardo', '555-236-3334', 'Ricardo.Romez@somewhere.com');
INSERT INTO CUSTOMER VALUES(
	null,'Jackson', 'Samantha', '555-236-1095', 'Samantha.Jackson@somewhere.com');

/*****   ITEM DATA   ************************************************************/

INSERT INTO ITEM VALUES(null,'Gold Bracelet', 120.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Gold Necklace', 160.00, 'Baker', 'Samantha');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 50.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Gold Bracelet', 180.00, 'Baker', 'Samantha');
INSERT INTO ITEM VALUES(null,'Silver Necklace', 135.00, 'Baxter', 'Sam');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 25.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 22.50, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Gold Earrings', 50.00, 'Lintz', 'John');
INSERT INTO ITEM VALUES(null,'Gold Necklace', 160.00, 'Lintz', 'John');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 20.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 35.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 45.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Gold Necklace', 225.00, 'Lintz', 'John');
INSERT INTO ITEM VALUES(null,'Silver Earrings', 55.00, 'Lintz', 'John');
INSERT INTO ITEM VALUES(null,'Gold Bracelet', 200.00, 'Lintz', 'John');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 25.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Bead Earrings', 45.00, 'Josephson', 'Mary');
INSERT INTO ITEM VALUES(null,'Gold Bracelet', 210.00, 'Baker', 'Samantha');
INSERT INTO ITEM VALUES(null,'Silver Necklace', 165.00, 'Baxter', 'Sam');

/*****   PURCHASE   *************************************************************/

INSERT INTO PURCHASE VALUES(null,'2014-05-05', 155.00, 1);
INSERT INTO PURCHASE VALUES(null,'2014-05-07', 203.00, 2);
INSERT INTO PURCHASE VALUES(null,'2014-05-11', 75.00, 3);
INSERT INTO PURCHASE VALUES(null,'2014-05-15', 67.00, 4);
INSERT INTO PURCHASE VALUES(null,'2014-05-15', 330.00, 5);
INSERT INTO PURCHASE VALUES(null,'2014-05-16', 25.00, 1);
INSERT INTO PURCHASE VALUES(null,'2014-05-26', 45.00, 3);
INSERT INTO PURCHASE VALUES(null,'2014-06-06', 445.00, 1);
INSERT INTO PURCHASE VALUES(null,'2014-06-07', 72.00, 6);

/*****   PURCHASE_ITEM DATA   ***************************************************/

INSERT INTO PURCHASE_ITEM VALUES(1, 1, 1, 155.00);
INSERT INTO PURCHASE_ITEM VALUES(2, 1, 2, 120.00);
INSERT INTO PURCHASE_ITEM VALUES(3, 1, 3, 75.00);
INSERT INTO PURCHASE_ITEM VALUES(4, 1, 6, 35.00);
INSERT INTO PURCHASE_ITEM VALUES(4, 2, 7, 32.00);
INSERT INTO PURCHASE_ITEM VALUES(5, 1, 4, 240.00);
INSERT INTO PURCHASE_ITEM VALUES(5, 2, 8, 90.00);
INSERT INTO PURCHASE_ITEM VALUES(6, 1, 10, 25.00);
INSERT INTO PURCHASE_ITEM VALUES(7, 1, 11, 45.00);
INSERT INTO PURCHASE_ITEM VALUES(8, 1, 5, 175.00);
INSERT INTO PURCHASE_ITEM VALUES(8, 2, 9, 215.00);
INSERT INTO PURCHASE_ITEM VALUES(8, 3, 12, 55.00);
INSERT INTO PURCHASE_ITEM VALUES(9, 1, 14, 72.00);

/*********************************************************************************/

