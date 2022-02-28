CREATE DATABASE flask_contacts;
use flask_contacts;


CREATE TABLE contacts (
	id int(3) NOT NULL AUTO_INCREMENT,
	fullname varchar(255) NOT NULL,
	phone varchar(12) NOT NULL,
	email varchar(100) NOT NULL,
	PRIMARY KEY (id)
);