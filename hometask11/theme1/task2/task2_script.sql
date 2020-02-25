
use hometask11;

drop function if exists big_insert;

delimiter //

create function big_insert( rand_insert int )
returns int deterministic
begin
	declare i int default 0;
	while i < rand_insert do 
		insert into users(firstname , lastname) values (concat('firstname' , i) , concat('lastname' , i));
		set i = i + 1;
	end while;
	return 1;
end//

delimiter ;

select big_insert(1000000);