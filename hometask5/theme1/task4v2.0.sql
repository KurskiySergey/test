 drop database if exists hometask5;
 create database hometask5;

use hometask5;


drop table if exists users;
create table users(
	id SERIAL primary key,
	name varchar(20),
	`month` enum('may' , 'august' , 'september')
);

insert into users(name , `month`) values
('serey' , 'may'),
('oleg' , 'september'),
('ira' ,'august');

select * from users
where `month` in('may' , 'august');