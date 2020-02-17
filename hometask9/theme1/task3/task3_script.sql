use hometask9;

start transaction;

set @start_day := 1;
set @end_day := 31;
set @august_day := '2018-08-01';


drop table if exists month_day;
create table  month_day(

id SERIAL primary key,

day_info datetime,
is_exist int default 1

);

prepare insert_data from 'insert into month_day(day_info) values (?)';
drop procedure if exists dowhile;

delimiter //
create procedure dowhile()
begin
	while @start_day <= @end_day do
		execute insert_data using @august_day;
		set @start_day = @start_day + 1;
		set @august_day := @august_day + interval 1 day;
	end while;
end; //
delimiter ;

call dowhile();

drop view if exists calendar;
create view calendar(created_at , is_exist ) as select created_at , is_exist 
from  month_day left join data_info on data_info.created_at = month_day.day_info;

update calendar 
set 
is_exist = 0
where created_at is null;

drop view if exists calendar;

select * from month_day;

drop table if exists month_day;

commit;