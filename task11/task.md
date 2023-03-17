```sql
create table logs
(
    id         serial primary key,
    name       varchar(255),
    detail     text,
    old_data   json,
    new_data   json,
    table_name varchar(255)
);





create or replace function airport_update_trigger_func()
    returns trigger
    language plpgsql
as
$$
BEGIN
    if tg_op = 'UPDATE' THEN
        insert into logs(detail, old_data, new_data, table_name)
        values ('Updated.', row_to_json(OLD), row_to_json(NEW), 'airports_data');
        return NEW;
    elsif tg_op ='DELETE' THEN
        insert into logs(detail, old_data, table_name)
        values ('DELETED.', row_to_json(OLD), 'airports_data');
        return OLD;
    END IF;
end;
$$;






create or replace trigger airport_update_trigger
    after update or delete
    on airports_data
    for each row
execute procedure airport_update_trigger_func();






create or replace trigger aircrafts_update_trigger
    after update or delete
    on aircrafts_data
    for each row
execute procedure airport_update_trigger_func();



create or replace trigger boarding_update_trigger
    after update or delete
    on boarding_passes
    for each row
execute procedure airport_update_trigger_func();




create or replace trigger bookings_update_trigger
    after update or delete
    on bookings
    for each row
execute procedure airport_update_trigger_func();





create or replace trigger flights_update_trigger
    after update or delete
    on flights
    for each row
execute procedure airport_update_trigger_func();





create or replace trigger seat_update_trigger
    after update or delete
    on seats
    for each row
execute procedure airport_update_trigger_func();





create or replace trigger tickets_flight_update_trigger
    after update or delete
    on ticket_flights
    for each row
execute procedure airport_update_trigger_func();





create or replace trigger tickets_update_trigger
    after update or delete
    on tickets
    for each row
execute procedure airport_update_trigger_func();


```