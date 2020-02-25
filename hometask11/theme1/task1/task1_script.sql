
use hometask11;

drop trigger if exists save_user_info;
drop trigger if exists save_catalogs_info;
drop trigger if exists save_products_info;


delimiter //
create trigger save_user_info after insert on users
for each row
	begin
		insert into logs(table_id , table_name , name ) values(new.id , 'users' , new.firstname);
	end//

create trigger save_catalogs_info after insert on catalogs
for each row
	begin
		insert into logs(table_id , table_name , name ) values(new.id , 'catalogs' , new.name);
	end//
	
create trigger save_products_info after insert on products
for each row
	begin
		insert into logs(table_id , table_name , name ) values(new.id , 'products' , new.name);
	end//
	
delimiter ;


insert into users(firstname , lastname) values('login' , 'password');
insert into catalogs(name) values('tables');
insert into products(catalog_id , name) values(1 , 'table-01');
