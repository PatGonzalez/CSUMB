#2
set autocommit =0;
set transaction isolation level repeatable read ;
select @@autocommit, @@tx_isolation;

#3 client 1

#4
select inventoryCount
from inventory
where id = 1;

select inventoryCount
from inventory
where id =3;

update inventory 
set inventoryCount =0
where id=1 ;

update inventory 
set inventoryCount =0
where id=3;

#check inventory
select *
from inventory;
commit;