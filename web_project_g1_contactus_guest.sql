-- auto-generated definition
create table contactus_guest
(
    id      int auto_increment
        primary key,
    name    varchar(50)  null,
    phone   decimal      null,
    email   varchar(100) null,
    contact varchar(300) null,
    constraint contactus_guest_id_uindex
        unique (id)
);


INSERT INTO `web-project-g1`.contactus_guest (id, name, phone, email, contact) VALUES (1, 'amit', 2432658960, 'amitganzi@gmail.com', 'asjdguef');
INSERT INTO `web-project-g1`.contactus_guest (id, name, phone, email, contact) VALUES (2, 'amit', 3456789210, 'amitganzi@gmail.com', 'kjadfis');
