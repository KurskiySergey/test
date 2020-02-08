drop database if exists hometask7;
create database hometask7;

use hometask7;

drop table if exists users;
create table users(
	
id SERIAL primary key,
firstname varchar(10),
lastname varchar (10)

);

drop table if exists items;
create table items(

	id SERIAL primary key,
	name varchar(30)

);


drop table if exists orders;
create table orders(
	
	id SERIAL primary key,
	user_id bigint unsigned not null,
	item_id bigint unsigned not null,
	created_at timestamp default current_timestamp,
	
	foreign key(user_id) references users(id),
	foreign key(item_id) references items(id)

);
