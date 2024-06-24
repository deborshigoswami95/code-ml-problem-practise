/* 
LINK
    https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1

SQL FLAVOR
    PostgreSQL

PROBLEM STATEMENT
    Calculate each user's average session time. A session is defined as the time difference between a page_load and page_exit. 
    For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page_load and 
    earliest page_exit, with an obvious restriction that load time event should happen before exit time event . 

    Output the user_id and their average session time.


NOTES
Not entirely sure if this solution is the optimal one but it works.

*/

with 
  fb_dt as (
    select 
        f.*
        , f.timestamp::date as dt
    from facebook_web_log f
  )
, earliest_exit as (
    select * from (
        select *,
        rank() over (partition by user_id, dt order by timestamp asc) as rnk_e
        from fb_dt
        where action like 'page_exit'
    ) r where r.rnk_e = 1
)
, latest_load as (
    select f1.* from (
        select 
            f2.*
            , rank() over (partition by f2.user_id, f2.dt order by f2.timestamp desc) as rnk_l
        from (
            select distinct f.* from fb_dt f
            inner join earliest_exit e on f.user_id = e.user_id and f.dt = e.dt
            and f.timestamp < e.timestamp
            where f.action like 'page_load'
        ) f2
    ) f1 where f1.rnk_l = 1
)
, time_diff as (
    select
        l.user_id
        , extract(epoch from (e.timestamp - l.timestamp)) as session_time_seconds
        , l.dt
    from latest_load l
    inner join earliest_exit e 
    on l.user_id = e.user_id
    and l.dt = e.dt
)
select user_id, avg(session_time_seconds) as avg_session_duration
from time_diff
group by user_id
