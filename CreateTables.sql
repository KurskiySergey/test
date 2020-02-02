use vk;

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