delete from coffee_respository;
insert into coffee_respository 
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
    "v60",
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
    "v60",
    "[00:00]40g;[00:40]120g;[01:25]200g",
    151,
    166.9,
    1.34,
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
    "v60",
    "[00:00]30g;[00:30]70g;[01:00]110g;[01:30]160g;[02:00]200g",
    181,
    167.9,
    1.33,
    null,
    16,
    2
);
select * from brewings;