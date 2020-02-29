use allguitars;

INSERT INTO `users` VALUES ('1','Peter','Braun'),
('2','Aracely','Schmeler'),
('3','Dayton','Luettgen'),
('4','Willard','Runte'),
('5','Devon','Hansen'); 

INSERT INTO `users_info` VALUES ('1','1','elna53@example.org', '0', 'false'),
('2','2','quitzon.travis@examp','0', 'false'),
('3','3','zulauf.cameron@examp','0', 'false'),
('4','4','qlarson@example.com', '0','false'),
('5','5','vdaniel@example.org','0', 'false'); 

INSERT INTO `users_registration_info` VALUES ('1','1','quia','ba09950dfac204b2ed6071072a5908'),
('2','2','repellendus','6b1aab0106766016483881dc0cbcf8'),
('3','3','sit','37f03645fc66ecfeb01981a51542f1'),
('4','4','qui','070f9375188df0c9d3625a40701d72'),
('5','5','hic','7181913000bc95856b4bacb13a8c8e'); 

INSERT INTO `messages` VALUES ('1','1','1','Est occaecati velit assumenda ipsum porro aut vel. Mollitia ipsam officiis necessitatibus aliquam voluptas et omnis. Cumque vero voluptas ratione. Deserunt reiciendis ut natus ab sunt.','2010-01-30 17:40:19','2009-06-08 08:36:34'),
('2','2','2','Et quos sunt provident ad. In architecto magnam inventore ut maiores saepe autem.','1991-04-12 05:13:20','2006-06-06 08:51:24'),
('3','3','3','Recusandae dicta voluptate libero omnis. Aliquid ut culpa ipsam. Sequi et molestiae ipsum occaecati voluptatem quas eaque. Perspiciatis saepe sit fugiat autem non repudiandae.','1993-10-31 22:55:57','1970-07-15 11:35:57'),
('4','4','4','Cumque qui debitis vel. Accusantium assumenda nulla corporis ex voluptates corrupti voluptas. Suscipit enim vitae ad est.','2009-09-26 20:48:03','1994-07-17 08:43:56'),
('5','5','5','Commodi veniam tempore dicta maxime quos necessitatibus. Assumenda sed hic nihil voluptatum autem.','1991-02-12 12:23:51','2013-12-25 04:37:12'); 

alter table messages add column is_read int default 0;


INSERT INTO `photos` VALUES ('1','cumque','img/supplier1.jpg'),
('2','earum','img/supplier2.jpg'),
('3','autem','img/supplier3.jpg'),
('4','maxime','img/supplier4.jpg'),
('5','ipsam','img/supplier5.jpg'); 

INSERT INTO `suppliers` VALUES ('1','beatae'),
('2','natus'),
('3','qui'),
('5','vitae'),
('4','voluptatem'); 

INSERT INTO `suppliers_info` VALUES ('1','Rerum quae rerum alias sed. Veritatis deserunt aut voluptatem laboriosam quis dolor. Esse perferendis et nostrum quibusdam incidunt. Dolorem quia veniam ut.','1','1'),
('2','Natus est voluptatem dolore quae. Quas quia omnis dolorum consequatur et consequatur. Eligendi ducimus rem quis.','2','2'),
('3','Ratione est voluptatem est maiores. Sed sit non magnam eum quasi magnam qui et. Nesciunt iste amet delectus dolorem. Velit neque enim molestiae nobis illo et dolorem repellat.','3','3'),
('4','Dignissimos error vel qui voluptate voluptatibus aliquam. Quaerat aliquam asperiores rem et aperiam consequatur. Facilis cumque ipsa autem mollitia culpa deserunt.','4','4'),
('5','Qui non similique similique dolores excepturi. Dicta explicabo esse aut. At provident recusandae ut officia.','5','5'); 

INSERT INTO `discounts` VALUES ('1','193',NULL),
('2','9976637',NULL),
('3','358697814',NULL),
('4','716',NULL),
('5','0',NULL); 

INSERT INTO `guitars` VALUES ('1','Dr.','1','1','1'),
('2','Mr.','1','2','2'),
('3','Ms.','3','3','3'),
('4','Prof.','4','4','4'),
('5','Prof.','5','5','5'); 

alter table `guitars` add column is_bought int default 0;

INSERT INTO `guitar_info` VALUES ('1','1','non','1971-05-20 07:12:12','consectetur','culpa'),
('2','2','cumque','1975-10-11 10:25:24','et','reprehenderit'),
('3','3','placeat','1986-11-02 09:48:35','amet','earum'),
('4','4','tempora','1974-12-15 15:32:00','sapiente','ipsam'),
('5','5','libero','1994-12-09 20:40:42','perferendis','inventore');

alter table `guitar_info` add column price int default 50;
