use hometask7;

-- Изначальный запрос 

select * from flights;


-- Делаем замену на русские названия

-- 1) Создаем таблицу table которая состоит из объединения двух таблиц
-- Первый select join делает замену на руские слова только для from
-- Второй - только для to
-- После объединения получится таблица у которой в каждой строке переведено только from или to 
-- 2) Делаем join с table и cities и выбираем только те у которых совпадают to и label в таблице cities
-- 3) Сортируем по id

select distinct id , `from` , name as `to` from  (
( select id , name as `from` , `to` from 
hometask7.flights join hometask7.cities
on flights.`from` = cities.label ) 
union 
( select id , `from` , name as `to` from 
hometask7.flights join hometask7.cities
on flights.`to` = cities.label )
) as `table` join cities 
on `table`.`to` = cities.label
order by id;