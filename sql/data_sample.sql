delete from baristas;
insert into baristas
values(
    null,
    "yelei",
    "dingyelei@gmail.com",
    '$2b$10$L1cXycvd4ksgPNMmBpV.g.QNAz0lFXlB8eqIsjPgWEo5K8Gm0tILC',
    '/baristas/1.jpg',
    "2024-04-01"
);
select * from baristas;

delete from coffees;
insert into coffees 
values (
    null,
    "El Salvador",
    "Chalatenango",
    "Finca Santa Rosa",
    "Pacamara",
    "Honey",
    "aoma",
    "2024-06-22",
    100,
    138,
    "cherry,apple,pomegranate,honey",
    '/coffees/1_coffee_1.jpg', -- readfile('sql/coffee_1.jpg'),
    73,
    null,
    1
);
insert into coffees 
values (
    null,
    "Bolivia",
    "Yanacachi",
    "Finca Takesi",
    "Geisha",
    "Washed",
    "Coffee Collective",
    "2024-06-09",
    120,
    298,
    "melon,bergamot,peach",
    '/coffees/1_coffee_2.jpg', 
    70,
    null,
    1
);
select * from coffees;
-- select writefile('sql/tmp.jpeg', image_note) from coffee_repositories where id = 1;

delete from brewings;
insert into brewings
values(
    null,
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
    0,
    1,
    1
);
insert into brewings
values(
    null,
    "2024-06-01",
    91,
    "13:200",
    13.0,
    200.6,
    "c40",
    28.0,
    "V60",
    "[00:00]40g;[00:40]120g;[01:25]200g",
    155,
    167.,
    1.36,
    null,
    1,
    1
);
insert into brewings
values(
    null,
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
    1,
    1,
    1
);
insert into brewings
values(
    null,
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
    1,
    1,
    1
);
insert into brewings
values(
    null,
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
    1,
    1,
    1
);
insert into brewings
values(
    null,
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
    0,
    1,
    1
);
insert into brewings
values(
    null,
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
    1,
    1,
    1
);
select * from brewings;