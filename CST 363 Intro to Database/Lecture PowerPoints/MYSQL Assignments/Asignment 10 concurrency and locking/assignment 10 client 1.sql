#1
set autocommit =0;
set transaction isolation level repeatable read ;
select @@autocommit, @@tx_isolation;

#2 client 2

#3
select inventoryCount
from inventory
where id = 1;

select inventoryCount
from inventory
where id =2;

update inventory 
set inventoryCount =0
where id=1 ;

update inventory 
set inventoryCount =0
where id=2;

#4 client 2


#5
select *
from inventory;
commit;







#reset
update inventory 
set inventoryCount =2
where id between 1 and 3;
commit;