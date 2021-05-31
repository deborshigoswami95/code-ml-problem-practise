# PROBLEM: https://leetcode.com/problems/department-highest-salary/

with max_sal as (
    select max(Salary) as max_sal, DepartmentId as dept_id
    from Employee
    group by DepartmentId
    )
select 
Department.Name as Department,
Employee.Name as Employee,
Employee.Salary as Salary
from Employee
join Department
on Employee.DepartmentId = Department.Id
where exists (
    select * 
    from max_sal 
    where Employee.Salary = max_sal.max_sal
    and Employee.DepartmentId = max_sal.dept_id);
