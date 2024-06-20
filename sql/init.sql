drop table if exists coffee_respository;
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
    price integer,
    flavors text,
    image_note blob,
    agtron integer,
    comments text
);

drop table if exists baristas;
create table if not exists baristas(
    id integer primary key,
    name text,
    email text,
    join_community_date text
);

