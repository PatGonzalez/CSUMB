## client 2 

##  step 2 

set autocommit=0;
set transaction isolation level repeatable read;
select @@autocommit, @@tx_isolation;
select population from cst438.city where id=1820;

## pause here. go to step 3 at client 1

## step 4.  change isolation level to Read Commited.

commit;
set transaction isolation level read committed;
select population from cst438.city where id=1820;

## pause here.  Go to step 5 at client 1.

## step 5.  re-read the population data.
## you should see the same value even though client 1 has updated it.
## why?  client 1 has not commited the change yet.

select population from cst438.city where id=1820;

## pause here.  go to step 6 in client 1

## step 7.  re read the population.  This time you see the new value.
select population from cst438.city where id=1820;

commit;


