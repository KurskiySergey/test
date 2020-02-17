drop database if exists hometask9;
create database hometask9;

use hometask9;

drop function if exists fibonacci;

delimiter //

create function fibonnaci(value int)
returns int deterministic
	begin
		declare i int default value;
		declare fib int default 1;
		declare fib_pr int default 0;
		declare tmp int default 0;
	
		if value = 0 then
			return 0;
		end if;
	
		while i > 1 do
			set tmp = fib;
			set fib = fib + fib_pr;
			set fib_pr = tmp;
			set i = i - 1;
		end while;
	
		return fib;
	end//
delimiter ;

select fibonnaci(10);