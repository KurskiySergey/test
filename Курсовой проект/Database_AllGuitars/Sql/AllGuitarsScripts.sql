
use allguitars;

-- 1) Вывод поставщиков гитар

select * from allguitars.suppliers;

-- 2) Организация записи в музыкальную школу

update users_info set
is_written_to_music_school = 1 where
users_info.user_id = 
(select users_registration_info.user_id from users_registration_info 

where users_registration_info.login = 'quia'
);

-- 3)Вывод информации о каждом поставщике

select distinct `body` from suppliers join suppliers_info 
on suppliers_info.supplier_id = 1;



-- 4) Вывод изображения для каждого поставщика

select distinct `path` from photos join suppliers 
join suppliers_info on  
suppliers_info.supplier_id = 1 AND suppliers_info.photo_id = photos.id AND suppliers_info.supplier_id = suppliers.id;

-- 5) Вывод список производимых гитар для каждого поставщика

select distinct guitars.id , model from suppliers join guitars on
guitars.supplier_id = suppliers.id and suppliers.id = 1;

-- 6) Вывод информации о каждой гитаре конкретного производителя (Цена  , материал , скидка , год изготовления  , модель , фото если есть )


SELECT DISTINCT * FROM guitars JOIN guitar_info JOIN discounts ON  
guitars.id = 1 AND guitars.id = guitar_info.id AND guitars.discount_id = discounts.id;

-- 7)  Вывод количества каждой гитары на складе

SELECT DISTINCT count(model) as models FROM guitars WHERE  
guitars.model = 'Dr.' AND guitars.is_bought = 0;


-- 8) Регистрация нового пользователя

drop procedure if exists registration;
delimiter //

create procedure registration()
begin
	declare u_id int default 0;
	if ((SELECT @ema_l in(SELECT email FROM users_info) as 'is_exist') = 1) or ((SELECT @log_n in(SELECT login FROM users_registration_info) as 'login_is_exist') = 1) then
		select 'Email or login already exists';
		rollback;
	else 
		INSERT INTO users(firstname , lastname) VALUES ( '$firstname' , '$lastname');
		set u_id:=(select users.id FROM users ORDER BY users.id DESC LIMIT 1 );
		INSERT INTO users_info(user_id , email) VALUES ( u_id , @emai_l );
		INSERT INTO users_registration_info(user_id , login , password) VALUES (u_id , @log_n , @pass); 
		select 'Registratiom is succsessful';
	end if;
end//

delimiter ;



start transaction;

set @ema_l:= 'vdaniel@example.org';
set @log_n:= 'log';
set @pass:= 'password';

-- Check email and login for existence

call registration();

commit;

-- 9)Вход для зарегистрированного пользователя
-- Аналогично 8 пункту




-- 10) Просмотр заказов для каждого пользователя

drop view if exists orders_info;
create view orders_info(model , status) as select model , status from orders join guitars join users_registration_info on orders.user_id = 1 
and orders.guitar_id = guitars.id 
and users_registration_info.user_id = orders.user_id;

select * from orders_info;

-- 11) Отправка сообщений в тех поддержу(админу)

-- По умолчанию письма отсылаются первому пользователю
INSERT INTO messages(who_send_id , body , send_at) VALUES (4 , '$text' , CURRENT_TIMESTAMP); 

-- 12)  Просмотр новых сообщений для каждого пользователя

drop view if exists message_info;
create view message_info(id , body , send_at , login ) 
as SELECT messages.id as id , body , send_at , login 
FROM messages 
JOIN users_registration_info ON is_read = '0' 
AND messages.to_whom_id = 1 
AND users_registration_info.user_id = messages.who_send_id 
ORDER BY send_at 
DESC;

select * from message_info;

-- 13) Просмотр всех не отвеченных сообщений для каждого пользователя

drop view if exists all_message_info;
create view all_message_info(id , body , send_at , login) as
SELECT messages.id as id , body , send_at , login 
FROM messages 
JOIN users_registration_info 
ON answered_at = '0000-00-00 00:00:00' 
AND messages.to_whom_id = 1 
AND users_registration_info.user_id = messages.who_send_id 
ORDER BY send_at 
DESC;

select * from all_message_info;




-- 14)Вывод информации о наличии новых сообщений у пользователя


drop view if exists  total_messages;
create view total_messages(total_messages) as 
select count(id) AS total FROM messages WHERE is_read = '0' AND messages.to_whom_id = 1;

select * from total_messages;

-- 15) Возможность оформить заказ

-- По умолчанию статус заказа send 
INSERT INTO orders(user_id , guitar_id) VALUES (1 , 1);
UPDATE guitars SET is_bought = '1' WHERE 1 = guitars.id;

-- 16) У админа реализовать возможность изменения статуса заказа

update orders set status = 'approved' where orders.id = 1;


