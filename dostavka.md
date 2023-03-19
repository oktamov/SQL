# Database for fast food delivery telegram bot



```sql
Table Admins {
  id serial [pk]
  username text [not null]
  telegram_id bigint [not null]
}

Table Customers {
  id serial [pk]
  telegram_id bigint [unique]
  name text [not null]
  phone_number text [not null]
  admins_id integer [ref: < Admins.id]
}

Table Delivery {
  id serial [pk]
  name text [not null]
  phone_number text [not null]
}

Table Menu_Items {
  id serial [pk]
  name text [not null]
  price integer [not null]
  description text
}

Table Orders {
  id serial [pk]
  customer_id integer [ref: > Customers.id]
  delivery_id integer [ref: > Delivery.id]
  order_time timestamp [not null]
  delivery_address text [not null]
  total_price integer [not null]
  status text [not null] 
}

Table Order_Items {
  id serial [pk]
  order_id integer [ref: > Orders.id]
  menu_item_id integer [ref: > Menu_Items.id]
  quantity integer [not null]
  item_price integer [not null]
}

```
![image](https://user-images.githubusercontent.com/122670933/226100603-00e45c30-64b7-40fc-9a13-d1b8cade578c.png)

