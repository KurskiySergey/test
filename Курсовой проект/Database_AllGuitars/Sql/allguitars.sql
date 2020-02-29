drop database if exists allguitars;
create database allguitars;
use allguitars;


-- all about suppliers, guitars and possible info about them

drop table if exists suppliers;
create table suppliers(
	id SERIAL primary key,
	name_of_supplier varchar(20),
	
	index(name_of_supplier)
);

drop table if exists photos;
create table photos(
	id SERIAL primary key,
	name varchar(10),
	`path` varchar(255),
	
	index (name)
);

drop table if exists discounts;
create table discounts(
	id SERIAL primary key,
	percent_of_discount int unsigned,
	info varchar(50)
);

drop table if exists suppliers_info;
create table suppliers_info(
	id SERIAL primary key,
	body text,
	supplier_id bigint unsigned not null,
	photo_id bigint unsigned not null,
	
	foreign key (supplier_id) references suppliers(id),
	foreign key (photo_id) references photos(id)
);

drop table if exists guitars;
create table guitars(
	id SERIAL primary key,
	model varchar(20),
	supplier_id bigint unsigned not null,
	photo_id bigint unsigned not null,
	discount_id bigint unsigned not null default 1,
	
	index(model),
	foreign key (supplier_id) references suppliers(id),
	foreign key (photo_id) references photos(id),
	foreign key (discount_id) references discounts(id)
);

drop table if exists guitar_info;
create table guitar_info(
	id SERIAL primary key,
	guitar_id bigint unsigned not null,
	info text,
	year_of_production datetime,
	front_deck_material varchar(30),
	back_deck_material varchar(30),
	
	foreign key (guitar_id) references guitars(id)
);

-- all about clients information

drop table if exists users;
create table users(
	id SERIAL primary key,
	firstname varchar(20),
	lastname varchar(20)
);

drop table if exists users_info;
create table users_info(
	id SERIAL primary key,
	user_id bigint unsigned not null,
	email varchar(50) unique,

	
	is_written_to_music_school int default 0,
	has_purshuases varchar(10) default 'false',
	
	foreign key(user_id) references users(id)
);

drop table if exists users_registration_info;
create table users_registration_info(
	id SERIAL primary key,
	user_id bigint unsigned not null,
	login varchar(20) unique,
	`password` varchar(30),
	
	foreign key (user_id) references users(id)
);

-- comminication

drop table if exists messages;
create table messages(
	id SERIAL primary key,
	who_send_id bigint unsigned not null,
	to_whom_id bigint unsigned not null default 1,
	body text,
	send_at datetime,
	answered_at datetime default '0000-00-00 00:00:00',
	-- status enum( 'is_sent' ,'is_written' , 'is_answered') default 'is_sent',
	
	foreign key (who_send_id) references users(id),
	foreign key (to_whom_id) references users(id)
);

-- orders

drop table if exists orders;
create table orders(
	id SERIAL primary key,
	user_id bigint unsigned not null,
	guitar_id bigint unsigned not null,
	status enum('send' , 'approved' , 'complete' , 'declined') default 'send',
	
	foreign key(user_id) references users(id),
	foreign key(guitar_id) references guitars(id)
);