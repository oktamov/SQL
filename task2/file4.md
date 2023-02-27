1. From the following table, write a SQL query to calculate total purchase amount of all orders. Return total purchase
   amount

```sql
SELECT SUM(purch_amt)
FROM orders
```

![img_27.png](img_27.png)

#   

2. From the following table, write a SQL query to calculate the average purchase amount of all orders. Return average
   purchase amount.
```sql
SELECT AVG(purch_amt) FROM orders
```
![img_28.png](img_28.png)
#   

3. From the following table, write a SQL query that counts the number of unique salespeople. Return number of salespeople.
```sql
SELECT COUNT (DISTINCT salesman_id) 
FROM orders;
```
![img_29.png](img_29.png)
#   

4. From the following table, write a SQL query to count the number of customers. Return number of customers.
```sql
SELECT COUNT (DISTINCT customer_id) 
FROM customer;
```
![img_30.png](img_30.png)
#  

5. From the following table, write a SQL query to determine the number of customers who received at least one grade for their activity.
```sql
SELECT COUNT (ALL grade) 
FROM customer;
```
![img_31.png](img_31.png)
#   

6. From the following table, write a SQL query to find the maximum purchase amount.    Go to the editor
```sql
SELECT max(purch_amt) 
FROM orders;
```
![img_32.png](img_32.png)
#   








