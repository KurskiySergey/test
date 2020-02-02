 drop database if exists hometask5;
 create database hometask5;

use hometask5;

drop table if exists users_new;
create table users_new (
	id SERIAL primary key,
	name varchar(20),
	created_at varchar(20),
	updated_at varchar(20)
);

insert into users_new(name , created_at , updated_at) values
( 'sergey' , '2018-01-05 10:30:49' , '2018-01-05 12:30:58'),
('ivan' , '2018-01-05 10:30:49' , '2018-01-05 12:30:58'),
('oleg' , '2018-01-05 10:30:49' , '2018-01-05 12:30:58');


describe users_new;

alter table users_new modify column created_at datetime;
alter table users_new modify column updated_at datetime;

describe users_new;