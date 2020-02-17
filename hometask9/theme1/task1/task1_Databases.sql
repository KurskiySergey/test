drop database if exists shop;
create database shop;

use shop;

drop table if exists users;
create table users(

id SERIAL primary key,
firstname varchar(30),
lastname varchar(30)

);

drop database if exists sample;
create database sample;

use sample;

drop table if exists users;
create table users(

id SERIAL primary key,
firstname varchar(30),
lastname varchar(30)

);