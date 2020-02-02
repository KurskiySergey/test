 drop database if exists hometask5;
 create database hometask5;

use hometask5;

drop table if exists catalogs;
create table catalogs(
	id SERIAL primary key,
	catalog_id int unsigned not null,
	name varchar(20)
);


INSERT INTO `catalogs` VALUES ('1','5','ut'),
('2','0','nemo'),
('3','1','doloribus'),
('4','2','sit'),
('5','3','voluptatibus'),
('6','1','qui'),
('7','2','blanditiis'),
('8','2','cumque'),
('9','4','dolorem'),
('10','0','ut'); 

select Round(exp(sum(log(id)))) as multiplication_of_id  from catalogs;