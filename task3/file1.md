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

