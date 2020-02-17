drop database if exists shop;
create database shop;

use shop;

drop table if exists accounts;
create table accounts(

	id SERIAL primary key,
	name varchar(30),
	`password` varchar(255)

);


drop view if exists username;
create view username as select id , name from accounts;

create user 'user_read'@'localhost';
revoke all on *.* from 'user_read'@'localhost';
grant all on shop.username to 'user_read'@'localhost';
