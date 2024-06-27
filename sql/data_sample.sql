delete from coffee_repositories;
insert into coffee_repositories 
values (
    16,
    "Panama",
    "Boquete",
    "Hacienda La Esmeralda",
    "Geisha",
    "Washed",
    "SEY",
    "2024-01-16",
    100,
    366,
    "jasmin,orange",
    null,
    75,
    null
);
select * from coffee_respository;

delete from baristas;
insert into baristas
values(
    2,
    "yelei",
    "dingyelei@gmail.com",
    "2024-04-01"
);
select * from baristas;

delete from brewings;
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
    "V60",
    "[00:00]40g;[00:40]120g;[01:25]200g",
    154,
    166.5,
    1.35,
    null,
    16,
    2
);
insert into brewings
values(
    2,
    "2024-06-02",
    91,
    "13:200",
    13.0,
    199.8,
    "c40",
    28.0,
    "V60",
    "[00:00]40g;[00:40]120g;[01:25]200g",
    151,
    166.9,
    1.32,
    null,
    16,
    2
);
insert into brewings
values(
    3,
    "2024-06-03",
    91,
    "12:200",
    12.0,
    200.3,
    "c40",
    28.0,
    "Kalita Wave155",
    "[00:00]30g;[00:30]70g;[01:00]110g;[01:30]160g;[02:00]200g",
    181,
    167.9,
    1.32,
    null,
    16,
    2
);
insert into brewings
values(
    4,
    "2024-06-04",
    91,
    "12:200",
    12.1,
    200.4,
    "c40",
    28.0,
    "Kalita Wave155",
    "[00:00]30g;[00:30]70g;[01:00]110g;[01:30]160g;[02:00]200g",
    183,
    168.1,
    1.31,
    null,
    16,
    2
);
insert into brewings
values(
    5,
    "2024-06-05",
    91,
    "12:200",
    12.1,
    200.2,
    "c40",
    28.0,
    "April",
    "[00:00]100g;[00:35]200g",
    143,
    167.1,
    1.28,
    null,
    16,
    2
);
insert into brewings
values(
    6,
    "2024-06-06",
    91,
    "12:200",
    12.0,
    200.4,
    "c40",
    28.0,
    "April",
    "[00:00]100g;[00:35]200g",
    140,
    167.4,
    1.27,
    null,
    16,
    2
);
select * from brewings;