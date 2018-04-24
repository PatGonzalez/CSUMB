## client 1 
##  step 1 
set autocommit=0;
set transaction isolation level repeatable read;
select @@autocommit, @@tx_isolation;

##  pause here.  go to step 2 at client 2
##  step 3 
##  the next update statement should hang and if you
##  wait several seconds, it will timeout.
##  why?  client has a lock on the record for id=1820.

update cst438.city set population=population+1000 where id=1820;

##  go to step 4 at client 2 

##  step 5.  Change isolation to read committed.
rollback;
set transaction isolation level read committed;

##  the update statement will not hang because of read committed.

update cst438.city set population=population+1000 where id=1820;
select population from cst438.city where id=1820;

## pause here.  go to step 5 in client 2. 

## step 6.  Now commit the transaction.

commit;

## go to step 7 in client 2
