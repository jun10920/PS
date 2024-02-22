with recursive time as (
    select 0 as hour
    union
    select hour+1 from time where hour<23
)

select time.hour, count(animal_id) as count
from (
    select *, hour(datetime) as hour
    from animal_outs) a
    right join time on a.hour=time.hour
group by time.hour
order by time.hour