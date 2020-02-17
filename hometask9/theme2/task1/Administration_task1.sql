drop database if exists shop;
create database shop;

create user 'shop_read'@'localhost';
revoke all on *.* from 'shop_read'@'localhost';
grant select on shop.* to 'shop_read'@'localhost'; 

create user 'shop'@'localhost';
revoke all on *.* from 'shop'@'localhost';
grant all on shop.* to 'shop'@'localhost';