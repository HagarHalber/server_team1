-- auto-generated definition
create table contactus
(
    email     varchar(100) not null,
    contact   varchar(500) not null,
    user_name varchar(50)  not null,
    constraint ContactUs_users_email_fk
        foreign key (email) references users (email)
);

INSERT INTO `web-project-g1`.contactus (email, contact, user_name) VALUES ('mommy@gmail.com', 'hiiii', 'mommy');
