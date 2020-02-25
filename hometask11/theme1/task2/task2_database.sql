drop database if exists hometask11;
create database hometask11;

use hometask11;

drop table if exists users;
create table users(

id SERIAL primary key,
firstname varchar(20),
lastname varchar(20)

);

drop table if exists catalogs;
create table catalogs(

id SERIAL primary key,
name varchar(20)

);


drop table if exists products;
create table products(

id SERIAL primary key,
catalog_id bigint unsigned not null,
name varchar(15),

foreign key(catalog_id) references catalogs(id)

);

drop table if exists logs;
create table logs(
	
	id SERIAL,
	table_id bigint unsigned not null,
	table_name varchar(20),
	created_at timestamp default now(),
	name varchar(20)

) comment='Archive' engine=Archive;
