DROP DATABASE IF EXISTS example;
CREATE DATABASE example;

USE example;

CREATE TABLE users 
( id SERIAL , name VARCHAR(20) );

INSERT  INTO users (name) VALUES
( 'Sergey' ),
( 'Timofey');

SHOW TABLES;

SELECT * FROM users;


