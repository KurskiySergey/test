
use hometask9;


drop function if exists hello;

delimiter //
create function hello()
returns varchar(255) deterministic
begin
	 declare `time` int default hour(now());
	if `time` between 6 and 12 then
		return 'Доброе утро';
	elseif `time` between 12 and 18 then
		return 'Добрый день';
	elseif `time` between 18 and 23 then
		return 'Добрый вечер';
	else
		return 'Доброй ночи';
	end if;
end//
delimiter ;

select hello();
