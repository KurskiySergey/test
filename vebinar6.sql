use vk;


-- Поиск человека который чаще всего общался с пользователем user_id = 1

select count(from_user_id) as total_messages , from_user_id , firstname , lastname from messages , users where -- вывести кол-во сообщений посланных пользователем from_user_id с именем fn и фамилией ln
-- из таблиц messages и users
messages.to_user_id = 1 -- кому послали сообщение (user_id = 1)
and (select status from friend_requests where friend_requests.target_user_id = messages.from_user_id) = 'approved' -- отбираем только друзей
and messages.from_user_id = users.id -- находим имя и фамилию по from_user_id
group by from_user_id -- группировка по from_user_id
having total_messages >= 0 -- сортировка по количеству сообщений в убывающем порядке
order by total_messages desc
limit 1; -- выводим только самого первого



-- Подсчитать общее количество лайков для всех пользователей меньше 10 лет

select count(likes.user_id) as total from likes where -- считаем likes в таблице likes
likes.media_id in (select media.id from media where  -- media_id лежат в таком промежутке  что пользователи разместившие эти новости меньше 10 лет
media.user_id in(select users.id from users , profiles where year(now()) - year(profiles.birthday) < 10 and profiles.user_id = users.id));



-- определить кто больше поставил лайков(всего ) - мужчины или женщины

select count(likes.user_id) as total , profiles.gender from likes , profiles where -- вывести количество лайков для каждого gender
likes.user_id = profiles.user_id
group by profiles.gender -- группируем по gender
having total >=0 
order by total desc; -- сортируем по убыванию 
