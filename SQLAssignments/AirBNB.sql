use test_airbnb;
create table air_bnb(
	listing_id int,
    dates varchar(15),
    available varchar(1),
    price varchar(10));
    
select * from air_bnb;

alter table air_bnb add date_from_dates date;
SET SQL_SAFE_UPDATES = 0;
UPDATE air_bnb SET date_from_dates = STR_TO_DATE(dates, '%Y-%m-%d');
SET SQL_SAFE_UPDATES = 1;

SELECT Min(date_from_dates) AS DATE_MIN, Max(date_from_dates) AS DATE_MAX, DateDiff(Max(date_from_dates),Min(date_from_dates)) 
AS TimePeriod FROM air_bnb;

SELECT listing_id,dates, COUNT(*) as count
FROM air_bnb
GROUP BY listing_id, dates
HAVING count(*)>1;

DELETE t1 FROM (SELECT *, ROW_NUMBER() OVER(partition by listing_id)  as rownum  FROM air_bnb) t1  
INNER JOIN (SELECT *, ROW_NUMBER() OVER(partition by listing_id)  as rownum FROM air_bnb) t2   
WHERE  
    t1.dates = t2.dates AND  
    t1.listing_id = t2.listing_id AND
    t1.rownum < t2.rownum;  
    
create table availability (
	listing_id int primary key,
    available int,
    not_available int,
    total int,
    percentage decimal(5,2));
    
insert into availability
	select listing_id, sum(available = 't'), sum(available = 'f'), count(*), sum(available = 't')/count(*)*100 
    from air_bnb group by listing_id;
    
select count(*) as available_days from availability where percentage>50;
select count(*) as available_days from availability where percentage>75;

SET SQL_SAFE_UPDATES=0;
UPDATE air_bnb SET price=NULL WHERE price='';
UPDATE air_bnb SET price=TRIM(LEADING '$' FROM price); 
SET SQL_SAFE_UPDATES=1;
ALTER TABLE air_bnb MODIFY price DECIMAL(5,2);

CREATE TABLE price_range(
	id int PRIMARY KEY,
    min_price DECIMAL(5,2),
    max_price DECIMAL(5,2),
    avg_price DECIMAL(5,2)
);
    
insert into price_range
	select listing_id,
    min(price), 
    max(price), 
    avg(price)
    from air_bnb group by listing_id;
    
    
select * from price_range where avg_price>500;
