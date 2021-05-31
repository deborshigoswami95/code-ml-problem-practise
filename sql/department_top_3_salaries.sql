# Problem: https://leetcode.com/problems/department-top-three-salaries/
with top3_sal as (
    select
    sal.Salary,
    sal.DepartmentId,
    rank() over (
        partition by sal.DepartmentId
        order by sal.Salary desc
        ) salary_rank
    from (select distinct salary, DepartmentId 
          from Employee) sal
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
    from top3_sal 
    where Employee.Salary = top3_sal.Salary
    and Employee.DepartmentId = top3_sal.DepartmentId
    and salary_rank <= 3
    );
