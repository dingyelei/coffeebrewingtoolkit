create table if not exists coffee_respository (
    id integer primary key,
    country text,
    region text,
    producer text,
    cultivar text,
    process text,
    roaster text,
    roast_date text,
    bag_size integer,
    flavors text,
    image_note blob,
    comments text
);

drop table coffee_respository;