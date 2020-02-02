drop database if exists vk;
create database vk;
use vk;

drop table if exists users;
create table users(
	id SERIAL primary key,
	firstname varchar(50),
	lastname varchar(50),
	email varchar(50) unique,
	`password` varchar(100),
	phone varchar(12),
	
	index users_phone_idx(phone),
	index (firstname , lastname)
);

drop table if exists profiles;
create table profiles(
	user_id SERIAL primary key,
	gender CHAR(1),
	birthday DATE,
	hometown varchar(100),
	created_at timestamp default now()
);

alter table profiles
add constraint fk_user_id
foreign key (user_id) references users(id)
on update cascade
on delete restrict;

drop table if exists messages;
create table messages(
	from_user_id bigint unsigned not null,
	to_user_id bigint unsigned not null,
	body Text,
	createt_at timestamp default now(),
	
	index (from_user_id),
	index (to_user_id),
	foreign key ( from_user_id) references users(id),
	foreign key ( to_user_id) references users(id)
);

drop table if exists friend_requests;
create table friend_requests(
	initiator_user_id bigint unsigned not null,
	target_user_id bigint unsigned not null,
	
	`status` enum('requested' , 'approved' , 'unfriended' , 'declined'),
	requested_at timestamp default now(),
	confirmed_at datetime,
	
	primary key (initiator_user_id , target_user_id ),
	index (target_user_id),
	index (initiator_user_id),
	foreign key ( initiator_user_id) references users(id),
	foreign key ( target_user_id) references users(id)
);

drop table if exists communities;
create table communities(
	id SERIAL primary key,
	name varchar(150)
);

drop table if exists users_communities;
create table users_communities(
	user_id bigint unsigned not null,
	community_id bigint unsigned not null,
	
	primary key (user_id , community_id),
	foreign key (user_id) references users(id),
	foreign key(community_id) references communities(id)
);

drop table if exists media_types;
create table media_types(
	id SERIAL primary key,
	name varchar(150)
);

drop table if exists media;
create table media(
	id SERIAL primary key,
	media_type_id bigint unsigned not null,
	user_id bigint unsigned not null,
	body text,
	filename varchar(255),
	`size` int,
	 -- metadata JSON,
	created_at datetime,
	updated_at timestamp default current_timestamp on update current_timestamp,
	
	index(user_id),
	foreign key (user_id) references users(id),
	foreign key (media_type_id) references media_types(id)
);

drop table if exists likes;
create table likes(
	id SERIAL primary key,
	user_id bigint unsigned not null,
	media_id bigint unsigned not null,
	created_at timestamp default now(),
	
	foreign key (user_id) references users(id),
	foreign key (media_id) references media(id)

);

drop table if exists photo_albums;
create table photo_albums (
	id SERIAL,
	name varchar(255) default null,
	user_id bigint unsigned default null,
	
	foreign key ( user_id ) references users(id),
	primary key (id)
);

drop table if exists photos;
create table photos (
	id SERIAL primary key,
	album_id bigint unsigned,
	media_id bigint unsigned not null,
	
	foreign key (album_id) references photo_albums(id),
	foreign key (media_id) references media(id)

);

drop table if exists music_albums;
create table music_albums(
	id SERIAL primary key,
	name varchar(150),
	user_id bigint unsigned not null,
	-- info about creation or last update
	updated_at timestamp default now() on update now(),
	
	-- for searching music_album
	index (name),
	
	foreign key (user_id) references users(id)

);

drop table if exists music;
create table music (
	id SERIAL primary key,
	-- album_id could be 0
	album_id bigint unsigned default null,
	name varchar(150),
	
	-- for searching by name
	index (name),
	
	foreign key (album_id) references music_albums(id)
	
);

drop table if exists music_info;
create table music_info(
	id SERIAL primary key,
	`size` int,
	who_upload_id bigint unsigned not null,
	upload_at timestamp default now(),
	-- metadata JSON
	
	foreign key (who_upload_id) references users(id),
	foreign key(id) references music(id)
);







