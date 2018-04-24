/******************************************************************************/
/*										                                      */
/*	Kroenke and Auer - Database Concepts (7th Edition)			           	  */
/*										                                      */
/*	Pet-Database Create Tables												  */
/*										                                      */
/*	These are the MYSQL 5.6 Database SQL code solutions							*/
/*										                                      */
/******************************************************************************/


CREATE TABLE PET_OWNER(
	OwnerID					      Int				NOT NULL auto_increment,
	OwnerLastName			      Char(25)		    NOT NULL,
	OwnerFirstName				Char(25)	  	  NOT NULL,
	OwnerPhone				      Char(12)		    NULL,
	OwnerEmail				      VarChar(100)	  NULL,
	CONSTRAINT				      OWNER_PK		    PRIMARY KEY(OwnerID)
	);
  
 

CREATE TABLE BREED(
	BreedName				        VarChar(100)	  NOT NULL,
	MinWeight				        Numeric(4,1)	  NULL,
	MaxWeight				        Numeric(4,1)	  NULL,
	AverageLifeExpectancy	  		Numeric(4,1)	  NULL,
	CONSTRAINT				      BREED_PK		    PRIMARY KEY(BreedName)
	);

CREATE TABLE PET (
	PetID					        Int					auto_increment  NOT NULL,
	PetName					        Char (50)		    NOT NULL,
	PetType					        Char (25)		    NOT NULL,
	PetBreed				        VarChar(100)	  	NULL,
	PetDOB					        Date           		 NULL,
	OwnerID					        Int				     NOT NULL,
	CONSTRAINT				      PET_PK			    PRIMARY KEY(PetID),
	CONSTRAINT 				      PET_OWNER_FK 	  FOREIGN KEY(OwnerID)
                REFERENCES PET_OWNER(OwnerID)
											ON DELETE CASCADE
	);
  
  

CREATE TABLE PET_3(
	PetID					        Int					auto_increment  NOT NULL,
	PetName					        Char (50)		    NOT NULL,
	PetType					        Char (25)		    NOT NULL,
	PetBreed				        VarChar(100)	  NULL,
	PetDOB					        Date		        NULL,
	PetWeight				        Numeric(4,1)	  NULL,
	OwnerID					        Int				      NOT NULL,
	CONSTRAINT				PET_3_PK		          PRIMARY KEY(PetID),
	CONSTRAINT 				PET_3_OWNER_FK	FOREIGN KEY(OwnerID)
                REFERENCES PET_OWNER(OwnerID)
											ON DELETE CASCADE
	);


ALTER TABLE PET
	ADD CONSTRAINT PET_BREED_FK FOREIGN KEY(PetBreed)
		REFERENCES BREED(BreedName)
		ON UPDATE CASCADE;

ALTER TABLE PET_3
	ADD CONSTRAINT PET_3_BREED_FK FOREIGN KEY(PetBreed)
		REFERENCES BREED(BreedName)
		ON UPDATE CASCADE; 




/********************************************************************************/

/******************************************************************************/
/*										                            	        */
/*	Kroenke and Auer - Database Concepts (7th Edition) Chapter 03	         	*/
/*											                                    */
/*  Pet-Database Data								                            */
/*											                                    */
/*	These are the MYSQL 5.6 SQL code solutions	 			                 */
/*																				                                    */
/******************************************************************************/

/*****   PET_OWNER DATA   *****************************************************/

INSERT INTO PET_OWNER VALUES( 
    null,'Downs', 'Marsha', '555-537-8765', 'Marsha.Downs@somewhere.com');
INSERT INTO PET_OWNER VALUES(
    null,'James', 'Richard', '555-537-7654', 'Richard.James@somewhere.com');
INSERT INTO PET_OWNER VALUES( 
    null,'Frier', 'Liz', '555-537-6543', 'Liz.Frier@somewhere.com');
INSERT INTO PET_OWNER (OwnerID, OwnerLastName, OwnerFirstName, OwnerEmail) VALUES
    (null, 'Trent', 'Miles', 'Miles.Trent@somewhere.com');



/*****   BREED DATA   ***********************************************************/

INSERT INTO BREED VALUES('Std. Poodle', 22.5, 30.0, 18);
INSERT INTO BREED VALUES('Cashmere', 10.0, 15.0, 12);
INSERT INTO BREED VALUES('Collie Mix', 17.5, 25.0, 18);
INSERT INTO BREED VALUES('Border Collie', 15.0, 22.5, 20);
INSERT INTO BREED(BreedName) VALUES('Unknown');



/*****   PET DATA   *************************************************************/

INSERT INTO PET VALUES(
    null,'King', 'Dog', 'Std. Poodle', '2011-02-27', 1);
    
INSERT INTO PET VALUES(
    null,'Teddy', 'Cat', 'Cashmere', '2012-02-01', 2);
INSERT INTO PET VALUES(
    null,'Fido', 'Dog', 'Std. Poodle', '2010-07-17', 1);
INSERT INTO PET VALUES(
    null,'AJ', 'Dog', 'Collie Mix', '2011-05-05', 3);
INSERT INTO PET VALUES(
    null,'Cedro', 'Cat', 'Unknown', '2009-06-06', 2);

INSERT INTO PET (PetID, PetName, PetType, PetBreed, OwnerID) VALUES(
	null, 'Wooley', 'Cat', 'Unknown', 2);

INSERT INTO PET VALUES(
    null,'Buster', 'Dog', 'Border Collie', '2008-12-11', 4);
    


/*****   PET_3 DATA   ***********************************************************/

INSERT INTO PET_3 VALUES(
    null,'King', 'Dog', 'Std. Poodle', '2011-02-27', 25.5, 1);
    
INSERT INTO PET_3 VALUES(
    null,'Teddy', 'Cat', 'Cashmere', '2012-02-01', 10.5, 2);
INSERT INTO PET_3 VALUES(
    null,'Fido', 'Dog', 'Std. Poodle', '2010-07-17', 28.5, 1);
INSERT INTO PET_3 VALUES(
    null,'AJ', 'Dog', 'Collie Mix', '2011-05-05', 20.0, 3);
INSERT INTO PET_3 VALUES(
    null,'Cedro', 'Cat', 'Unknown', '2009-06-06', 9.5, 2);

INSERT INTO PET_3 (PetID, PetName, PetType, PetBreed, PetWeight, OwnerID)
  VALUES(null, 'Wooley', 'Cat', 'Unknown', 9.5, 2);

INSERT INTO PET_3 VALUES(
    null,'Buster', 'Dog', 'Border Collie', '2008-12-11', 25.0, 4);
    


/****************************************************************************************/