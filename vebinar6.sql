use vk;


-- ����� �������� ������� ���� ����� ������� � ������������� user_id = 1

select count(from_user_id) as total_messages , from_user_id , firstname , lastname from messages , users where -- ������� ���-�� ��������� ��������� ������������� from_user_id � ������ fn � �������� ln
-- �� ������ messages � users
messages.to_user_id = 1 -- ���� ������� ��������� (user_id = 1)
and (select status from friend_requests where friend_requests.target_user_id = messages.from_user_id) = 'approved' -- �������� ������ ������
and messages.from_user_id = users.id -- ������� ��� � ������� �� from_user_id
group by from_user_id -- ����������� �� from_user_id
having total_messages >= 0 -- ���������� �� ���������� ��������� � ��������� �������
order by total_messages desc
limit 1; -- ������� ������ ������ �������



-- ���������� ����� ���������� ������ ��� ���� ������������� ������ 10 ���

select count(likes.user_id) as total from likes where -- ������� likes � ������� likes
likes.media_id in (select media.id from media where  -- media_id ����� � ����� ����������  ��� ������������ ������������ ��� ������� ������ 10 ���
media.user_id in(select users.id from users , profiles where year(now()) - year(profiles.birthday) < 10 and profiles.user_id = users.id));



-- ���������� ��� ������ �������� ������(����� ) - ������� ��� �������

select count(likes.user_id) as total , profiles.gender from likes , profiles where -- ������� ���������� ������ ��� ������� gender
likes.user_id = profiles.user_id
group by profiles.gender -- ���������� �� gender
having total >=0 
order by total desc; -- ��������� �� �������� 
