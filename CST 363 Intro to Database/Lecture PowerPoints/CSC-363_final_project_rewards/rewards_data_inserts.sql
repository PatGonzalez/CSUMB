/*
insert scripts
- award type
- customers
- transactions
- awards
- rewards
- summary
*/

/*
test
delete from summary;
delete from rewards;
delete from awards;
delete from transactions;
delete from customers;
delete from award_type;
*/

-- award_type
insert into award_type
(type_description)
values
('Transaction Award'),
('Birthday Award'),
('Special Offer'),
('Taco Tuesday'),
('Pizza Sunday'),
('Other');

-- retrieve the award type values into variables
select award_type_id from award_type where type_description = 'Transaction Award' into @txn_award_type;
select award_type_id from award_type where type_description = 'Birthday Award' into @bday_award_type;
select award_type_id from award_type where type_description = 'Special Offer' into @spo_award_type;
select award_type_id from award_type where type_description = 'Taco Tuesday' into @taco_award_type;
select award_type_id from award_type where type_description = 'Pizza Sunday' into @pizza_award_type;

-- insert customers records with the team names
insert into customers
(first_name, last_name, birthdate, enroll_date, email_address, phone_number)
values
('Mike', 'Loeser', STR_TO_DATE('1977-02-04','%Y-%m-%d'), STR_TO_DATE('2016-10-31','%Y-%m-%d'), 'mloeser@csumb.edu', '212-555-1234'),
('Patrick', 'Gonzalez', STR_TO_DATE('1995-05-10','%Y-%m-%d'), STR_TO_DATE('2017-06-01','%Y-%m-%d'), 'patgonzalez@csumb.edu', '212-555-9876'),
('Chris', 'Holmes', STR_TO_DATE('1989-08-08','%Y-%m-%d'), STR_TO_DATE('2016-11-26','%Y-%m-%d'), 'cholmes@csumb.edu', '212-555-7584'),
('Chris', 'Buckey', STR_TO_DATE('1997-11-15','%Y-%m-%d'), STR_TO_DATE('2018-01-25','%Y-%m-%d'), 'cbuckey@csumb.edu', '212-555-9999'),
('John', 'Seals', STR_TO_DATE('1990-04-05','%Y-%m-%d'), STR_TO_DATE('2017-04-05','%Y-%m-%d'), 'jseals@csumb.edu', '212-555-2683');

-- retrieve the newly inserted id values into variables
select customer_id from customers where last_name = 'loeser' into @loeser;
select customer_id from customers where last_name = 'gonzalez' into @gonzalez;
select customer_id from customers where last_name = 'holmes' into @holmes;
select customer_id from customers where last_name = 'buckey' into @buckey;
select customer_id from customers where last_name = 'seals' into @seals;

-- test query to check for the inserted customer id vars
-- select @loeser, @gonzalez, @holmes, @buckey, @seals;

-- insert transaction records for each of the customers
insert into transactions
(customer_id, purchase_amt, tax_amt, txn_date)
values
(@loeser, 35.75, 7.00, STR_TO_DATE('2016-10-31','%Y-%m-%d')),
(@loeser, 23.46, 5.50, STR_TO_DATE('2017-05-20','%Y-%m-%d')),
(@gonzalez, 44.65, 8.00, STR_TO_DATE('2017-06-01','%Y-%m-%d')),
(@gonzalez, 18.95, 3.00, STR_TO_DATE('2017-11-02','%Y-%m-%d')),
(@holmes, 27.97, 6.00, STR_TO_DATE('2016-11-26','%Y-%m-%d')),
(@holmes, 31.25, 6.75, STR_TO_DATE('2017-07-04','%Y-%m-%d')),
(@buckey, 48.55, 9.00, STR_TO_DATE('2018-01-25','%Y-%m-%d')),
(@buckey, 11.75, 2.55, STR_TO_DATE('2018-02-10','%Y-%m-%d')),
(@seals, 15.75, 2.80, STR_TO_DATE('2017-04-05','%Y-%m-%d')),
(@seals, 20.90, 3.25, STR_TO_DATE('2017-09-11','%Y-%m-%d'));

-- retrieve the txn id values for use in awards
select txn_id into @loesertxn from transactions where customer_id = @loeser limit 1;
select txn_id into @gonzaleztxn from transactions where customer_id = @gonzalez limit 1;
select txn_id into @holmestxn from transactions where customer_id = @holmes limit 1;
select txn_id into @buckeytxn from transactions where customer_id = @buckey limit 1;
select txn_id into @sealstxn from transactions where customer_id = @seals limit 1;

-- test query - view the txn id values
-- select @loesertxn, @gonzaleztxn, @holmestxn, @buckeytxn, @sealstxn;

-- create some award records - one with txn and one non-txn for each customer
insert into awards
(customer_id, award_type_id, txn_id, point_earn, points, award_date)
values
(@loeser, @txn_award_type, @loesertxn, 1, 50, current_timestamp),
(@loeser, @bday_award_type, @loesertxn, 1, 20, current_timestamp),
(@gonzalez, @txn_award_type, @gonzaleztxn, 1, 30, current_timestamp),
(@gonzalez, @spo_award_type, @gonzaleztxn, 1, 10, current_timestamp),
(@holmes, @txn_award_type, @holmestxn, 1, 45, current_timestamp),
(@holmes, @taco_award_type, @holmestxn, 1, 15, current_timestamp),
(@buckey, @txn_award_type, @buckeytxn, 1, 25, current_timestamp),
(@buckey, @pizza_award_type, @buckeytxn, 1, 10, current_timestamp),
(@seals, @txn_award_type, @sealstxn, 1, 40, current_timestamp),
(@seals, @spo_award_type, @sealstxn, 1, 20, current_timestamp);

-- create some reward records with arbitrary point amounts - one for each customer
insert into rewards
(customer_id, points, reward_date)
values
(@loeser, 35, current_timestamp),
(@gonzalez, 27, current_timestamp),
(@holmes, 15, current_timestamp),
(@buckey, 33, current_timestamp),
(@seals, 21, current_timestamp);

-- retrieve the totals --
-- award sum totals per customer
select sum(points) into @loeserawardstotal from awards where customer_id = @loeser group by customer_id;
select sum(points) into @gonzalezawardstotal from awards where customer_id = @gonzalez group by customer_id;
select sum(points) into @holmesawardstotal from awards where customer_id = @holmes group by customer_id;
select sum(points) into @buckeyawardstotal from awards where customer_id = @buckey group by customer_id;
select sum(points) into @sealsawardstotal from awards where customer_id = @seals group by customer_id;

-- reward sum total per customer
select sum(points) into @loeserrewardstotal from rewards where customer_id = @loeser group by customer_id;
select sum(points) into @gonzalezrewardstotal from rewards where customer_id = @gonzalez group by customer_id;
select sum(points) into @holmesrewardstotal from rewards where customer_id = @holmes group by customer_id;
select sum(points) into @buckeyrewardstotal from rewards where customer_id = @buckey group by customer_id;
select sum(points) into @sealsrewardstotal from rewards where customer_id = @seals group by customer_id;

-- ensure summary is cleared - only 1 summary can exist per customer
truncate summary;

-- insert the summary records - one per customer - using the totals variables
insert into summary
(customer_id, points, total_rewards, total_awards, last_updated)
values
(@loeser, @loeserawardstotal - @loeserrewardstotal, @loeserrewardstotal, @loeserawardstotal, current_timestamp),
(@gonzalez, @gonzalezawardstotal - @gonzalezrewardstotal, @gonzalezrewardstotal, @gonzalezawardstotal, current_timestamp),
(@holmes, @holmesawardstotal - @holmesrewardstotal, @holmesrewardstotal, @holmesawardstotal, current_timestamp),
(@buckey, @buckeyawardstotal - @buckeyrewardstotal, @buckeyrewardstotal, @buckeyawardstotal, current_timestamp),
(@seals, @sealsawardstotal - @sealsrewardstotal, @sealsrewardstotal, @sealsawardstotal, current_timestamp);

-- inserts complete!