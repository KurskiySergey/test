use hometask9;

drop table if exists products;
create table products(

id SERIAL primary key,
name varchar(45) default null,
description varchar(45) default null

);

INSERT INTO `products`(name , description) VALUES ('ratione','Aut veniam harum inventore aut temporibus. Su'),
('ut','Quae ut sapiente blanditiis quo. Quisquam aut'),
('non','Corporis dolore nihil perspiciatis et labore '),
('consequatur','Quos deleniti delectus qui doloremque harum. '),
('ut','Soluta iste quasi aperiam ut aperiam quia quo'),
('consequatur','Magnam id sunt accusamus aliquam illo labore '),
('qui','Voluptate enim voluptatem qui sit in id. Quia'),
('ea','Quia dolorem modi aut eius dolorem officia ea'),
('non','Voluptas repellat molestias sapiente consequa'),
('aut','Dolorum suscipit atque distinctio corrupti et'); 

set @total = null;

drop trigger if exists check_insert;
delimiter //

create trigger check_insert after insert on products
for each row
	begin
		if (new.name is null and new.description is null) then
			set @total:= 1;
		end if;
	end//
delimiter ;

drop function if exists roll_back;
delimiter //

create function roll_back()
returns varchar(10)
begin
	if @total = 1 then 
		delete from products where name is null and description is null;
		return 'error';
	else
		return 'done';
	end if;
end//
delimiter ;

start transaction;
  	insert into products(name , description) values( null , null);
 	select roll_back();
 commit;
  