use hometask9;

select * from calendar;

start transaction;

select @min_day:= cur_day from calendar 
order by cur_day desc
limit 1
offset 4;

delete from calendar
where cur_day < @min_day;

commit;

select * from calendar order by cur_day desc;