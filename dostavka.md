# Database for fast food delivery telegram bot



```sql
Table admins {
  admin_id SERIAL [pk]
  telegram_id BIGINT [unique, not null]
  address VARCHAR(255) [ref:< Restaurants.restaurant_address]

}


Table Customers {
  customer_id SERIAL [pk]
  first_name VARCHAR(50) [not null]
  last_name VARCHAR(50) [not null]
  phone_number VARCHAR(20) [not null]
  telegram_id VARCHAR(20) [not null]
  created_at TIMESTAMP [default: `CURRENT_TIMESTAMP`]
  address VARCHAR(255) [unique, not null]
  admin_id INT [ref:< admins.admin_id]
}

Table Orders {
  order_id SERIAL [pk]
  delivery_address VARCHAR(255) [not null]
  order_time TIMESTAMP [default: `CURRENT_TIMESTAMP`]
  order_status VARCHAR(20) [not null]
  customer_id int [ref: < Customers.customer_id]
}

Table OrderItems {
  order_item_id SERIAL [pk]
  item_name VARCHAR(255) [not null]
  item_quantity INT [not null]
  item_price DECIMAL(10,2) [not null]
  order_id int [ref: < Orders.order_id]
}

Table Restaurants {
  restaurant_id SERIAL [pk]
  restaurant_name VARCHAR(255) [not null]
  restaurant_address VARCHAR(255) [not null]
  restaurant_phone VARCHAR(20) [not null]
}

Table MenuCategories {
  category_id SERIAL [pk]
  category_name VARCHAR(50) [not null]
}

Table MenuItems {
  item_id SERIAL [pk]
  item_name VARCHAR(255) [not null]
  item_description VARCHAR(255)
  item_price DECIMAL(10,2) [not null]
  category_id int [ref:< MenuCategories.category_id]
  restaurant_id int [ref:< Restaurants.restaurant_id]
}

Table DeliveryPersonnel {
  personnel_id SERIAL [pk]
  first_name VARCHAR(50) [not null]
  last_name VARCHAR(50) [not null]
  phone_number VARCHAR(20) [not null]
  restaurant_id INT [ref:< Restaurants.restaurant_id]
}

Table Deliveries {
  delivery_id SERIAL [pk]
  delivery_time TIMESTAMP [default: `CURRENT_TIMESTAMP`]
  order_id int [ref: < Orders.order_id]
  personnel_id int [ref:<  DeliveryPersonnel.personnel_id]
}

Table logs {
  id SERIAL [pk]
  name VARCHAR(255)
  detail TEXT
  old_data json
  new_data json
  table_name VARCHAR(255)
}



```
![image](https://user-images.githubusercontent.com/122670933/227492290-9c53b4f6-666c-4048-9efe-685d632f3d30.png)
