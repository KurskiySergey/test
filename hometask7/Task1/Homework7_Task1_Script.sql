use hometask7;

select firstname , lastname , count(item_id) as total_orders from users , orders 
where users.id = orders.user_id 
group by users.id
having total_orders > 0
order by total_orders desc;