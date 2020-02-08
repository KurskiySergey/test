use hometask7;

select products.catalog_id , products.id , products.name from products join catalogs
order by products.catalog_id;