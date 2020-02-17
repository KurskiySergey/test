drop database if exists hometask9;
create database hometask9;

use hometask9;

drop table if exists data_info;
create table data_info(

id SERIAL primary key,

created_at datetime

);

