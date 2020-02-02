use vk;

alter table profiles add is_active int default 1;

update profiles 
set 
	is_active = 0
where year(current_date) - year(birthday) < 18;

