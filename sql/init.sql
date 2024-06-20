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

drop table if exists brewings;
create table if not exists brewings(
    id integer primary key,
    date text,

    temperature integer,
    ratio text,
    dose real,
    water real,
    grinder text,
    griding_size real,
    dripper text,

    brewing_method text,
    brewing_time integer,
    coffee real,

    tds real,
    pe real,

    coffee_id integer,
    barista_id integer,
    foreign key (coffee_id) references coffee_respository(id),
    foreign key (barista_id) references baristas(id)
);

insert into brewings
values(
    1,
    "2024-06-01",
    91,
    "13:200",
    13.0,
    200.6,
    "c40",
    28.0,
    "v60",
    "[00:00]40g;[00:40]120g;[01:25]200g",
    181,
    167.9,
    1.33,
    null,
    16,
    2
);
