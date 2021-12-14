alter table vendor add unique (username);
alter table buyer modify username varchar(100) not null;

alter table buyer modify pass varchar(100) not null;
alter table vendor modify pass varchar(100) not null;
alter table vendor modify username varchar(100) not null;

alter table items modify i_name varchar(100) not null;
alter table items modify listedon varchar(100) not null;
alter table items modify listedby int not null;
