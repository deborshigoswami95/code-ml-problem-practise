# https://leetcode.com/problems/rank-scores/


with distinct_score as (
    select distinct Score from Scores
),
r as (
    select Rank() over (
        order by Score desc
    ) 'Rank',
    Score
    from distinct_score
)
select
s.Score,
r.Rank
from 
Scores as s
join
r
on r.Score = s.Score
order by r.Rank asc
