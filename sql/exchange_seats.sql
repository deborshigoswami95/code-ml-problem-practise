-- https://leetcode.com/problems/exchange-seats/

with count_seat as (
            select count(*) as counts from seat
        )
select
    case
        when mod(id,2)!=0 and id=count_seat.counts then id
        when mod(id,2)!=0 and id!=count_seat.counts then id+1
        else id-1
    end as id,
    student
from
seat,count_seat
order by id asc
