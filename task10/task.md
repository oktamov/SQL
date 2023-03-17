# task1
```sql
create or replace function get_model_value(model jsonb, lang varchar)
    returns text
    language plpgsql
as
$$
begin
    return model ->> lang;
end;
$$;

select aircraft_code, get_model_value(model, 'ru'), range
from aircrafts_data;
```
![img.png](img.png)
#  

# task2
```sql
create or replace function timezone_func(key varchar(100))
    returns text
    language plpgsql
as
$$
declare
    val text;
begin
    select airport_name
    into val
    from airports_data
    where timezone = key;
    return val;
end;
$$;

select timezone_func('Asia/Yakutsk')
```
![img_1.png](img_1.png)

# task3
```sql
create or replace function task3(key varchar(100))
    returns text
    language plpgsql
as
$$
declare
    val text;
begin
    select city::json ->> key
    into val
    from airports_data;
    return upper(val);
end;
$$;

select task3('en')
```
![img_2.png](img_2.png)
