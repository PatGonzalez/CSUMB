USE rewards;

Insert Into award_type Values
	(100, '100 Visits free Dinner for two'),
    (50, '50 dollor Gift Card');
    
SET AUTOCOMMIT =0;
INSERT INTO customers VALUES
	#(1, 'LastN1','FirstN1', '1980-01-01','2017-01-01','one@gmail.com','1112223333'),
	#(2, 'LastN2','FirstN2', '1980-02-01','2017-02-01','two@gmail.com','1112223333'),
	(3, 'LastN3','FirstN3', '1980-03-01','2017-03-01','three@gmail.com','1112223333'),
	(4, 'LastN4','FirstN4', '1980-04-01','2017-04-01','four@gmail.com','1112223333'),
	(5, 'LastN5','FirstN5', '1980-05-01','2017-05-01','five@gmail.com','1112223333'),
	(6, 'LastN6','FirstN6', '1980-06-01','2017-06-01','six@gmail.com','1112223333'),
	(7, 'LastN7','FirstN7', '1980-07-01','2017-07-01','seven@gmail.com','1112223333'),
	(8, 'LastN8','FirstN8', '1980-08-01','2017-08-01','eight@gmail.com','1112223333'),
	(9, 'LastN9','FirstN9', '1980-09-01','2017-09-01','nine@Gmail.com','1112223333'),
	(10, 'LastN10','FirstN10', '1980-10-01','2017-10-01','ten@gmail.com','1112223333');


INSERT INTO awards VALUES
	(null, 5, 