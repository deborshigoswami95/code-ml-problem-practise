/* 
leetcode 175. Combine Two Tables
https://leetcode.com/problems/combine-two-tables/
*/

select 
t1.FirstName, 
t1.LastName, 
t2.City, 
t2.State
from Person t1
left outer join Address t2
on t1.PersonId = t2.PersonId
