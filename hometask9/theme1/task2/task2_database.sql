drop database if exists hometask9;
create database hometask9;

use hometask9;

drop table if exists catalogs;
create table catalogs(

id SERIAL primary key,
name varchar(30)

);

drop table if exists products;
create table products(

id SERIAL primary key,
name varchar(30),
catalog_id bigint unsigned not null,
price int,

foreign key (catalog_id) references catalogs(id)

);


