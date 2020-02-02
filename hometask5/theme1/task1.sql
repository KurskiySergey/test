 drop database if exists hometask5;
 create database hometask5;

use hometask5;

drop table if exists users;
create table users(
	id SERIAL primary key,
	name varchar(20),
	created_at datetime,
	updated_at datetime
);


insert into users(name) values
( 'sergey' ),
('ivan'),
('oleg');

select * from users;

update users
set
	created_at = now(),
	updated_at = now();
	
select * from users;