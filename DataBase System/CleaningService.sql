CREATE TABLE Dog (
	dog_ID INT not null,
	dog_name char(30),
	dog_size char(30),
	breed char(30),
	owner_ID INT not null,
	primary key(dog_ID)
);

insert into Dog values (501, 'Pinky', 'M', 'French Bulldong', 101);
insert into Dog values (301, 'Fin', 'S', 'Shih Tzu', 102);
insert into Dog values (701, 'Coffee', 'L', 'Puddle', 103);
insert into Dog values (302, 'Lychee', 'S', 'Yorkshire terrier', 104);
insert into Dog values (702, 'Shiro', 'L', 'Shiba Inu', 105);
insert into Dog values (303, 'Kuma', 'S', 'Yorkshire terrier', 106);
insert into Dog values (304, 'Lego', 'S', 'Shih Tzu', 102);

select * from Dog;



create table Salon_Service (
    s_ID char(13),
    dog_size char(13),
    service char(13),
    price int not null, 
    primary key (s_ID),
    check (price >= 0 )
);


insert into salon_service values ('S01', 'S', 'Grooming', 350);
insert into salon_service values ('S02', 'S', 'Bathing', 300);
insert into salon_service values ('S03', 'S', 'Hotel', 390);
insert into salon_service values ('S04', 'S', 'Nail clipping', 50);
insert into salon_service values ('S05', 'M', 'Grooming', 450);
insert into salon_service values ('S06', 'M', 'Bathing', 400);
insert into salon_service values ('S07', 'M', 'Hotel', 490);
insert into salon_service values ('S08', 'M', 'Nail clipping', 50);
insert into salon_service values ('S09', 'L', 'Grooming', 550);
insert into salon_service values ('S10', 'L', 'Bathing', 500);
insert into salon_service values ('S11', 'L', 'Hotel', 590);
insert into salon_service values ('S12', 'L', 'Nail clipping', 50);

select * from salon_service;

--Q1 
select dog_size, service, price
from salon_service;

--Q2
select dog_size, service, price
from salon_service
where dog_size in ('S','L') and price > 350;

--Q3
select dog_id
from Dog, salon_service
where dog.dog_size = salon_service.dog_size and service = 'grooming'

union

select dog_id
from Dog, salon_service
where dog.dog_size = salon_service.dog_size and service = 'bathing';
