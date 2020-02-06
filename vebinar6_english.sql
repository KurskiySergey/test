use vk;


-- Searching a person who has been writing to user with user_id = 1 more often then others

select count(from_user_id) as total_messages , from_user_id , firstname , lastname from messages , users where -- count ammount of messages from every user to person with user_id = 1
messages.to_user_id = 1 -- to whom the message was sent (user_id = 1)
and (select status from friend_requests where friend_requests.target_user_id = messages.from_user_id) = 'approved' -- choose only friends
and messages.from_user_id = users.id -- find firstname and lastname according to from_user_id
group by from_user_id -- making groups by from_user_id
having total_messages >= 0 -- descending sort by total_messages
order by total_messages desc
limit 1; -- print only first one



-- Count total likes which were sent to all users with age less then 10 years

select count(likes.user_id) as total from likes where -- count likes in table likes
likes.media_id in (select media.id from media where  -- choose media_id that were posted by users with age less then 10 years 
media.user_id in(select users.id from users , profiles where year(now()) - year(profiles.birthday) < 10 and profiles.user_id = users.id));



-- Who sent more likes in total? man or woman?

select count(likes.user_id) as total , profiles.gender from likes , profiles where -- print number of likes for each gender
likes.user_id = profiles.user_id
group by profiles.gender -- group by gender
having total >=0 
order by total desc; -- descendind sort by total 
