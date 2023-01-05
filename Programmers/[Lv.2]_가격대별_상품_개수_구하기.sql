
select sum(ks."Close") as "close" , sum(ks."Change") as "change" , split_part(ks.date::varchar, '-', 1) as date, ss.value as sector 
from kospi_sql ks 
join sector_sql ss on ss.code = ks.code 
group by 3,4
order by 4,3

select ks."Close" as "close" , ks."Change" as "change" , split_part(ks.date::varchar, '-', 1) as date, ss.value as sector, ks.code 
from kospi_sql ks 
join sector_sql ss on ss.code = ks.code 


select sum(ks."Close") as "close" , sum(ks."Change") as "change" , split_part(ks.date::varchar, '-', 1) as date, ss.value as sector 
from kosdaq_sql ks  
join sector_sql ss on ss.code = ks.code 
group by 3,4
order by 4,3

select ks."Close" as "close" , ks."Change" as "change" , split_part(ks.date::varchar, '-', 1) as date, ss.value as sector, ks.code 
from kosdaq_sql ks 
join sector_sql ss on ss.code = ks.code 