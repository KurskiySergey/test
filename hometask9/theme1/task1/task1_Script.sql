
start transaction;

use shop;

select @firstname:= firstname , @lastname:= lastname from users where id = 1;

savepoint get_info;

use sample;

insert into users(firstname , lastname) values(

@firstname,

@lastname

);

savepoint insert_info;

use shop;

delete from users where id = 1;

commit;
