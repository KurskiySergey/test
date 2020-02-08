drop database if exists hometask7;
create database hometask7;

use hometask7;

drop table if exists catalogs;
create table catalogs(
	
	id SERIAL primary key,
	name varchar(15)
	
);

drop table if exists products;
create table products(
	id SERIAL primary key,
	catalog_id bigint unsigned not null,
	name varchar(30),
	
	foreign key(catalog_id) references catalogs(id)
	on update cascade
	on delete cascade

);