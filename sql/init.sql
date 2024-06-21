drop table if exists coffee_repositories;
create table if not exists coffee_repositories (
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
    brewing_date text,

    temperature integer,
    ratio text,
    dose real,
    water real,
    grinder text,
    grinding_size real,
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
