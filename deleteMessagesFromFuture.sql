use vk;

delete from messages
where createt_at > now();