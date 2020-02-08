drop database if exists hometask7;
create database hometask7;

use hometask7;

drop table if exists flights;
create table flights(
	id SERIAL primary key,
	`from` varchar(20),
	`to` varchar(20)

);

drop table if exists cities;
create table cities(
	
	label varchar(20),
	name varchar(20)
);

