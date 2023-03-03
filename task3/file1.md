# 1
```sql
SELECT E.first_name , E.last_name , 
       E.department_id , D.department_name 
        FROM employees E 
         JOIN departments D 
          ON E.department_id = D.department_id;
```
![img.png](img.png)
 

# 2.
```sql
 select E.first_name,E.last_name, 
   D.department_name, L.city, L.state_province
   from employees E
   join departments D
   on E.department_id = D.department_id
   join locations L
   on D.location_id = L.location_id
```
![img_1.png](img_1.png)

# 3
```sql
SELECT E.first_name, E.last_name, E.salary, J.grade_level
 FROM employees E 
   JOIN job_grades J
     ON E.salary BETWEEN J.lowest_sal AND J.highest_sal;
```
![img_2.png](img_2.png)

#   4
```sql
select E.first_name,
       E.last_name,
       E.department_id,
       D.department_name
from departments D
         join employees E
              on E.department_id = D.department_id and E.department_id in (40, 80)
```
![img_3.png](img_3.png)

# 5
```sql
select E.first_name,
        E.last_name,
        D.department_name,
        L.city,
        L.state_province
from employees E
          join departments D
               on E.department_id = D.department_id
          join locations L
               on D.location_id = L.location_id
where E.first_name like '%z%';
```
![img_4.png](img_4.png)

# 6 
```sql
SELECT E.first_name, E.last_name, D.department_id, D.department_name 
 FROM employees E 
   RIGHT OUTER JOIN departments D
     ON E.department_id = D.department_id;
```
![img_3.png](img_3.png)

# 7
```sql
SELECT E.first_name, E.last_name, E.salary 
  FROM employees E 
   JOIN employees S
     ON E.salary < S.salary 
      AND S.employee_id = 182;
```
![img_5.png](img_5.png)

# 8 
```sql
SELECT E.first_name AS "Employee Name", 
   S.first_name AS "Manager" 
  FROM employees E 
   JOIN employees S
     ON E.MANAGER_ID = S.EMPLOYEE_ID
```
![img_6.png](img_6.png)

# 9 
```sql
select D.department_name, L.city, L.state_province
from departments D
join locations L
on D.location_id = L.location_id;
```
![img_7.png](img_7.png)     

# 10.
```sql
SELECT E.first_name, E.last_name, E.department_id, D.department_name 
  FROM employees E 
   LEFT OUTER JOIN departments D 
     ON E.department_id = D.department_id;
```
![img_8.png](img_8.png)

# 11

```sql
SELECT E.first_name AS "Employee Name",
   M.first_name AS "Manager"
    FROM employees E 
      LEFT OUTER JOIN employees M
       ON E.manager_id = M.employee_id;
```
![img_9.png](img_9.png)

# 12. 
```sql
SELECT E.first_name, E.last_name, E.department_id 
  FROM employees E 
  JOIN employees S 
     ON E.department_id = S.department_id
and S.last_name= 'Taylor';
```
![img_10.png](img_10.png)

# 13.  
```sql
SELECT job_title, department_name, first_name || ' ' || last_name AS Employee_name, start_date 
	FROM job_history 
		JOIN jobs USING (job_id) 
			JOIN departments USING (department_id) 
				JOIN  employees USING (employee_id) 
					WHERE start_date>='1993-01-01' AND start_date<='1997-08-31';
```
![img_11.png](img_11.png)




