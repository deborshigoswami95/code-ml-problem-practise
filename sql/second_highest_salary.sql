# https://leetcode.com/problems/second-highest-salary/

with t as (
        select distinct Salary from Employee
        order by Salary desc
        limit 2
)
select 
case 
    when count(*)<2 then null
    else min(t.Salary) 
end as SecondHighestSalary 
from t
