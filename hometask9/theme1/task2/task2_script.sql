use hometask9;

create view product_info(catalog_name , product_name) as select ct.name , pr.name from catalogs as ct , products as pr where ct.id = pr.catalog_id;

select * from product_info;

drop view if exists product_info;